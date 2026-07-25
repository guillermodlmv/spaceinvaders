
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = None
        self.bullet_img = None
        self.bullet_cooldown_counter = 0
        self.cooldown = 60
        self.bullets = []

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))

    def get_width(self):
        return self.player_img.get_width()

    def get_height(self):
        return self.player_img.get_height()