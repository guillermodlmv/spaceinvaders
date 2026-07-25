import pygame

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self, speed):
        self.y += speed

    def collision(self, obj):
        offset = (int(obj.x - self.x - 30), int(obj.y - self.y - 20))
        return self.mask.overlap(obj.mask, offset)
