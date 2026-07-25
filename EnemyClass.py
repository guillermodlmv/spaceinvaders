import pygame
import os
from ShipClass import Ship
import secrets

current_dir = os.path.dirname(os.path.abspath(__file__))

# Definir rutas completas de las imagenes
BULLET_IMG = pygame.image.load(os.path.join(current_dir, 'img', 'bullet_image.png'))
ENEMY_BLUE_IMAGE = pygame.image.load(os.path.join(current_dir, "img", "enemy_blue_image.png"))
ENEMY_GREEN_IMAGE = pygame.image.load(os.path.join(current_dir, "img", "enemy_green_image.png"))
ENEMY_PURPLE_IMAGE = pygame.image.load(os.path.join(current_dir, "img", "enemy_purple_image.png"))
SHOT_BLUE_IMAGE = pygame.image.load(os.path.join(current_dir, "img", "shot_blue.png"))
SHOT_GREEN_IMAGE = pygame.image.load(os.path.join(current_dir, "img", "shot_green.png"))
SHOT_PURPLE_IMAGE = pygame.image.load(os.path.join(current_dir, "img", "shot_purple.png"))
WIDTH, HEIGHT = 800, 600

class Enemy(Ship):
    COLOR = {
        'blue': [ENEMY_BLUE_IMAGE, SHOT_BLUE_IMAGE],
        'green': [ENEMY_GREEN_IMAGE, SHOT_GREEN_IMAGE],
        'purple': [ENEMY_PURPLE_IMAGE, SHOT_PURPLE_IMAGE]
    }

    def __init__(self, speed, x=50, y=50, color='blue', health=100):
        super().__init__(x, y, health)
        self.ship_img = self.COLOR[color][0]
        self.image, self.shot_image = self.COLOR[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.speed = speed

    def move(self):
        self.y += self.speed

    def create(self, amount):
        enemies = []
        for _ in range(amount):
            enemy = Enemy(x=  20 + secrets.randbelow(WIDTH - ENEMY_BLUE_IMAGE.get_width() - 40),
                            y= -1000 + secrets.randbelow(900),
                            color= secrets.choice(['blue', 'green', 'purple']),
                            speed=self.speed)
            enemies.append(enemy)
        return enemies

    def increase_speed(self):
        self.speed += 1.02

def main():
    run = True
    clock = pygame.time.Clock()
    enemies = Enemy(1).create(5)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for enemy in enemies:
            enemy.move()

        # Limpia la pantalla para generar enemigos
        WIN.fill((0, 0, 0))

        #Genera enemigos
        for enemy in enemies:
            enemy.draw(WIN)
        pygame.display.update()

    pygame.quit()

    