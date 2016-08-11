#-------------------------------------------------------------------------------
# Name:        Settings
# Purpose:     conserve les parametres d'un jeu lambda
#
# Author:      Tom LaPomme | Les Studios LaPomme
#
# Created:     05/08/2016
# Copyright:   (c) TLP 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame as pg
import random
import os
pg.mixer.init()

# --- Fonctions os pour la compatibilite---
def path_asset(fichier) :
    return os.path.join('Assets',fichier)

# --- Assets ---
logo   = pg.image.load (path_asset('Graphics/Logo_Studio.png'))
icone  = pg.image.load( path_asset('Graphics/icone.png'))
player_img  = pg.image.load( path_asset('Graphics/Player.png'))
select = pg.mixer.Sound(path_asset('Audio/BGS/select.wav'))
beat   = pg.mixer.Sound(path_asset('Audio/BGS/heartbeat.wav'))
shoot   = pg.mixer.Sound(path_asset('Audio/BGS/select.wav'))

# --- Game option settings ---
width  = 1200
height = 500
fps    = 60
font   = 'handmeds'

droite = width/1.5
player_bullet_size = (3, 6)
ennemie_bullet_size = (5, 10)
meteor_size = (30, 30)
ennemie_size = (25,30)
nb_ennemies = 2
cadence_ennemie = 25
player_initial_pos = (width / 2, height / 1.2)


# --- Colors ---
background_color = (5,5,30)
WHITE            = (255,255,255)
BLACK            = (0,0,0)
YELLOW           = (255,255,0)
RED              = (255,0,0)

# --- Vocabulary ---
title   = 'Shoot em up Test'