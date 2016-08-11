#-------------------------------------------------------------------------------
# Name:        Je sais pas encore
# Purpose:     Shoot em up
# Author:      Tom LaPomme | Les Studios LaPomme
#
# Created:     05/08/2016
# Copyright:   (c) TLP 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame as pg
import os
from Settings import *
from Sprites import *
class Game :
      def __init__(self) :
          # initialisation des parametres
          pg.init()
          pg.mixer.init()
          self.screen = pg.display.set_mode((width, height))
          pg.display.set_caption(title)
          pg.display.set_icon(icone)
          self.clock = pg.time.Clock()
          self.running = True
          self.font_name = pg.font.match_font(font)
          pass

      def new(self) :
          # Creer une partie (creation des objets)
          self.all_sprites = pg.sprite.Group()
          self.mobs_list = pg.sprite.Group() ## mobs = tout objets mobile non jouables
          self.bullet_player = pg.sprite.Group() ## mobs = tout objets mobile non jouables
          self.player = Player(self.mobs_list)
          ## Liste de tout les spawn point du jeu
          ## un y negatif permet de laisser un temps d'apparition
          ## a faire --> automatise a partir d'un fichier text
          ## pour eviter de prendre de la place
          self.Spawn_point("triangle",droite-25,0,-1)
          self.Spawn_point("solo",droite-25,-500,-1)
          self.Spawn_point("solo",0,-500,1)
          self.Spawn_point("diagonal",droite-40,-1550,-1.2)
          self.Spawn_point("lineaire",width/2,-1500,0)

          self.pannel = Driver_pannel()
          for i in range (8):
              self.meteor = Meteor()
              self.all_sprites.add(self.meteor)
              self.mobs_list.add(self.meteor)

          self.all_sprites.add(self.player,self.pannel)
          self.run()
          pass

      def run(self) :
          # boucle du jeu - mecaniques
          self.playing = True
          while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()
          pass

      def update(self) :
          # boucle du jeu - update
          self.all_sprites.update()
          self.mobs_list.update()
          pass

      def events(self) :
          # boucle du jeu - gestion des evenements
          if pg.sprite.spritecollideany(self.player,self.mobs_list, False) :
                 self.player.life += -10
                 print( self.player.life )
                 if  self.player.life <= 0 :
                    self.player.kill()
          if pg.sprite.groupcollide(self.bullet_player,self.mobs_list, True,True) :
                 self.player.life += -10
                 print( self.player.life )
                 if  self.player.life <= 0 :
                    self.player.kill()
          for event in pg.event.get():
            # verification fenetre fermer
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_SPACE]:
                    self.player.tir(self,self.bullet_player)
                    shoot.play()

          pass

      def draw(self) :
          # boucle du jeu - affichage
          self.screen.fill(background_color)
          self.all_sprites.draw(self.screen)
          pg.display.flip()
          pass

      def show_splashscreen(self):
        # Affichage de la splashscreen
        beat.play()
        self.fadeout_img(logo,0,0,3000,BLACK)
        self.fadeout_text(BLACK,"Un jeu amateur",40,WHITE, width/2, height/2,3000)
        self.press_key()
        pass

      def show_endscreen(self):
       # Affichage de l'ecran de game over
        pass

      def menu(self):
          self.screen.fill(background_color)
          self.draw_text(title, 40, WHITE, width/2 ,  height/4 )
          self.draw_text("Appuie sur une touche", 18, WHITE, width/2 ,  height/2 )
          self.draw_text("(c) Les Studios LaPomme / code : Tom LaPomme / musique : Anate Y / Graphisme : Clement Chroma, Doreen, Henijay", 15, WHITE, width/2.85 ,  height -40 )
          self.draw_text("Avec les voix de BlueTroelix, Floriant Soret et Branlito", 15, WHITE, width/5 ,  height -30 )
          pg.display.flip()
          self.press_key()
          pass

      def press_key(self):
        # Continue apres avoir presser une touche
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

      def Spawn_ennemie(self,x,y,vx,vy):
         self.ennemie = Ennemie(self.player,self,self.mobs_list,x,y,vx,vy)
         self.all_sprites.add(self.ennemie)
         self.mobs_list.add(self.ennemie)

      def Spawn_point(self,formation,x,y,vx):

              if formation =="triangle" :
                 self.Spawn_ennemie(x,y,vx,1)
                 self.Spawn_ennemie(x+25,y+30,vx,1)
                 self.Spawn_ennemie(x+50,y,vx,1)
              if formation =="lineaire" :
                 self.Spawn_ennemie(x,y,vx,1)
                 self.Spawn_ennemie(x+25,y,vx,1)
                 self.Spawn_ennemie(x+50,y,vx,1)
              if formation =="diagonal":
                 self.Spawn_ennemie(x,y,vx,1)
                 self.Spawn_ennemie(x+25,y+30,vx,1)
                 self.Spawn_ennemie(x+50,y+60,vx,1)
              if formation =="solo" :
                 self.Spawn_ennemie(x,y,vx,1)

      def draw_text(self, text, size, color, x, y):
        # Affichage d'un texte a l'ecran
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


      def fadeout_text(self,background, text, size, color, x , y, delay) :
          self.screen.fill(background)
          self.draw_text(text, size, color, x , y )
          pg.time.delay (delay)
          pg.display.flip()

      def fadeout_img(self,image, x , y, delay,background) :
          self.screen.fill(background)
          self.screen.blit(image,(x,y))
          pg.time.delay (delay)
          pg.display.flip()






g = Game()
##g.show_splashscreen()
g.menu()
while g.running:
      g.new()

      g.show_endscreen()

pg.mixer.quit()
pg.quit()