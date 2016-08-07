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

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(player_size)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = player_initial_pos
        self.vx  = 0
        self.vy  = 0

    def update(self):
        self.vx = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx= -5
        if keys[pg.K_RIGHT]:
            self.vx = 5

        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.x > droite:
            self.rect.x = droite
        if self.rect.x < 0:
            self.rect.x = 0



    def tir(self,game):
       bullet = Bullet(game,self)
       bullet.update()


    def bouclier(self):
        pass

    def load_img():
        pass

    def animate() :
        pass

class Bullet(pg.sprite.Sprite) :

      def __init__(self,game,player) :
           pg.sprite.Sprite.__init__(self)
           game.all_sprites.add(self)
           self.image = pg.Surface(bullet_size)
           self.image.fill(YELLOW)
           self.rect = self.image.get_rect()
           self.rect.center = player.rect.center


      def update(self) :
          self.rect.y -= 5


class Ennemie(pg.sprite.Sprite) :

      def __init__(self):
          pg.sprite.Sprite.__init__(self)
          self.image = pg.Surface(player_size)
          self.image.fill(WHITE)
          self.rect = self.image.get_rect()


      def update(self):
        pass

      def tir():
          bullet = Bullet(game,self)
          bullet.update()
          pass

class Meteor(pg.sprite.Sprite) :

      def __init__(self) :
          pg.sprite.Sprite.__init__(self)
          self.image = pg.Surface((meteor_size))
          self.image.fill(WHITE)
          self.rect = self.image.get_rect()
          self.rect.x = random.randrange(300 - self.rect.width)
          self.rect.y = random.randrange(-100, -40)
          self.speedy = random.randrange(1, 8)
          self.speedx = random.randrange(-3, 3)

      def update(self):
         self.rect.x += self.speedx
         self.rect.y += self.speedy
         if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right >  droite:
                self.rect.x = random.randrange(width - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 8)


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