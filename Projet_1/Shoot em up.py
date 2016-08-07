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
          self.player = Player()
          self.pannel = Driver_pannel()
          for i in range (8):
              self.meteor = Meteor()
              self.all_sprites.add(self.meteor)
              meteor_list = pg.sprite.Group()
              meteor_list.add(self.meteor)

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
          pass

      def events(self) :
          # boucle du jeu - gestion des evenements
          for event in pg.event.get():
            # verification fenetre fermer
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_SPACE]:
                    self.player.tir(self)
                    #shoot.play()

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
        self.fadeout_img(logo,0,0,3000)
        self.fadeout_text(BLACK,"Un jeu amateur",40,WHITE, width/2, height/2,4000)
        self.fadeout_text(BLACK,credits,15,WHITE, width/2, height/2,4000)
        self.press_key()
        pass

      def show_endscreen(self):
       # Affichage de l'ecran de game over
        pass

      def menu(self):
          self.screen.fill(background_color)
          self.draw_text(title, 40, WHITE, width/2 ,  height/4 )
          self.draw_text("Appuie sur une touche", 15, WHITE, width/2 ,  height/2 )
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
          for i in range(255):
               self.screen.set_alpha(255-i)
          pg.display.flip()

      def fadeout_img(self,image, x , y, delay) :
          self.screen.blit(image,(x,y))
          pg.time.delay (delay)
          for i in range(255):
               self.screen.set_alpha(255-i)
          pg.display.flip()





g = Game()
#g.show_splashscreen()
g.menu()
while g.running:
      g.new()

      g.show_endscreen()

pg.mixer.quit()
pg.quit()