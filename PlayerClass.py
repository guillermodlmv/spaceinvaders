import pygame
import sys
import os
from ShipClass import Ship
from BulletClass import Bullet

PLAYER_IMG = pygame.image.load(os.path.join("img", "player_image.png"))
BULLET_IMG = pygame.image.load(os.path.join("img", "bullet_image.png"))
WIDTH, HEIGHT = 800, 600

class Player(Ship):
    def __init__(self,x, y, x_speed, y_speed, health=100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_IMG
        self.bullet_img = BULLET_IMG
        self.max_health = health
        self.bullet_speed = -10
        self.creation_cooldown_counter = 0
        self.max_amount_bullets = 3
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y > 0:  # Up
            self.y -= self.y_speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y < HEIGHT - self.ship_img.get_height() - 60:  # Down
            self.y += self.y_speed
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > 0:  # Left
            self.x -= self.x_speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x + self.x_speed < WIDTH - self.ship_img.get_width():  # Right
            self.x += self.x_speed

    def increase_speed(self):
        if self.x_speed < 10:
            self.x_speed += 1.25
            self.y_speed += 1.25
        elif self.x_speed >= 10:
            self.x_speed = 10
            self.y_speed = 8
        if self.cooldown > 25:
            self.cooldown *= 0.9
    
    def create_bullets(self):
        if (len(self.bullets) < self.max_amount_bullets and self.creation_cooldown_counter == 0):
            bullet = Bullet(self.x, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.creation_cooldown_counter = 1