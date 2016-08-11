#-------------------------------------------------------------------------------
# Name:        Sprites
# Purpose:     Creations et parametrage des sprites
#
# Author:      Tom LaPomme | Les Studios LaPomme
#
# Created:     05/08/2016
# Copyright:   (c) TLP 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame as pg
import random
from Settings import *

"""class Spritesheet:

    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):

        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        return image"""


class Player(pg.sprite.Sprite):

    def __init__(self,group):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = player_initial_pos
        self.vx  = 0
        self.vy  = 0
        self.life = player_life
        self.groups = group

    def update(self):
        self.vx = 0
        self.vy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx= -5
        if keys[pg.K_RIGHT]:
            self.vx = 5
        if keys[pg.K_UP]:
            self.vy = -5
        if keys[pg.K_DOWN]:
            self.vy = 5

        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.x > droite:
            self.rect.x = droite
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

    def tir(self,game,groups):
       self.bullet = Bullet(game,self, -5,player_bullet_size)
       groups.add(self.bullet)
       self.bullet.update()

    def bouclier(self):
        pass

    def load_img():
        pass

    def animate() :
        pass

class Bullet(pg.sprite.Sprite) :

      def __init__(self,game,player,speed,size) :
           pg.sprite.Sprite.__init__(self)
           game.all_sprites.add(self)
           self.image = pg.Surface(size)
           self.image.fill(YELLOW)
           self.rect = self.image.get_rect()
           self.rect.center = player.rect.center
           self.speed = speed


      def update(self) :
          self.rect.y += self.speed


class Ennemie(pg.sprite.Sprite) :

      def __init__(self,player,game,group,x,y,vx,vy):
          pg.sprite.Sprite.__init__(self)
          self.image = pg.Surface(ennemie_size)
          self.image.fill(RED)
          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y
          self.vx   = vx
          self.vy   = vy
          self.game = game
          self.groups = group
          self.cadence = cadence_ennemie


      def update(self):
          self.cadence += 1
          if self.cadence >= cadence_ennemie :
             self.cadence = 0
             self.tir(self.game,self.groups)
          if self.rect.y < 0 :
             self.rect.y += 1
          else :
                  self.rect.x += self.vx
                  self.rect.y += self.vy
          if self.rect.top > height + self.rect.width or self.rect.left < - self.rect.width or self.rect.right >  droite + 50:
              self.kill()

      def tir(self,game,groups):
          if self.rect.y >= 0 :
             bullet = Bullet(game,self, random.randrange(5, 10),ennemie_bullet_size)
             groups.add(bullet)
             bullet.update()

class Meteor(pg.sprite.Sprite) :

      def __init__(self) :
          pg.sprite.Sprite.__init__(self)
          self.image = pg.Surface((meteor_size))
          self.image.fill(WHITE)
          self.rect = self.image.get_rect()
          self.rect.x = random.randrange(300 - self.rect.width)
          self.rect.y = random.randrange(-150, -100)
          self.vy = random.randrange(1, 2)
          self.vx = random.randrange(-3, 3)

      def update(self):
         self.rect.x += self.vx
         self.rect.y += self.vy
         if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right >  droite + 35:
                self.rect.x = random.randrange(width - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.vy = random.randrange(1, 8)


class Driver_pannel(pg.sprite.Sprite) :

      def __init__(self) :
           pg.sprite.Sprite.__init__(self)
           self.image = pg.Surface((width/3, height))
           self.image.fill(YELLOW)
           self.rect = self.image.get_rect()
           self.rect.x = droite + width/21

      def display_player_life():
          pass

      def display_score():
          pass

      def display_power_up():
          pass

      def display_bouclier():
           pass

      def display_scanner():
           pass

      def display_plan_vaisseau() :
          pass