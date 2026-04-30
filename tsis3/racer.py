import pygame
import random

LANES = [80, 180, 280, 380] # Координаты центров полос

class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (230, 520)
        self.has_shield = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 50:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < 450:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(LANES), -50)
        self.speed = speed

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > 600:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, p_type):
        super().__init__()
        self.type = p_type # 'nitro', 'shield', 'repair'
        self.image = pygame.Surface((30, 30))
        colors = {'nitro': (255, 165, 0), 'shield': (0, 0, 255), 'repair': (0, 255, 0)}
        self.image.fill(colors[p_type])
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(LANES), -50)

    def update(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.kill()