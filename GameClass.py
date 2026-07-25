import pygame
import os
import sys
import turtle

BULLET_IMAGE = pygame.image.load(os.path.join("img", "bullet_image.png"))

class Game:
    def __init__(self, font, fps, count, window, lives, screen_width, screen_height, bullets = 0, click = pygame.time.Clock()):
        self.font = font
        self.FPS = fps
        self.count = count
        self.window = window
        self.lives = lives
        self.HEIGHT = screen_width
        self.WIDTH = screen_height
        self.bullets = bullets
        self.bullet_image = BULLET_IMAGE

    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False

    def over(self):
        if self.lives <= 0:
            self.count = 0
            while True:
                self.clock.tick(self.FPS)
                lost_label = self.font.render("GAME OVER", 1, (255, 0, 0))
                # Mostrar mensaje de "GAME OVER" a la mitad
                self.window.blit(lost_label, (self.WIDTH / 2 - lost_label.get_width() / 2, self.HEIGHT / 2 - lost_label.get_height() / 2))
                pygame.display.update()
                self.count += 1
                if self.count == self.FPS * 3:  # Esperar 3 segundos antes de cerrar el juego
                    break
            return True
        else:
            return False