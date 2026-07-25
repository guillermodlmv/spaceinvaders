import pygame
# Permite ver las carpetas de las rutas
import os
# Dependencia mixer es para manejo de sonido
from pygame import mixer

#Background
BACKGROUND = pygame.image.load(os.path.join("img", "background.png"))
ICON_IMAGE = pygame.image.load(os.path.join("img", "title_icon.png"))
TITLE = 'Space Invaders HD'

#Player:
    #Images
PLAYER_IMAGE = pygame.image.load(os.path.join("img", "player_image.png"))
BULLET_IMAGE = pygame.image.load(os.path.join("img", "bullet_image.png"))


pygame.init()

# Game Window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON_IMAGE)


try:
    mixer.music.load(os.path.join("sounds", "background_song.mp3"))

except Exception as e:
    print("Error al cargar la música:", e)


