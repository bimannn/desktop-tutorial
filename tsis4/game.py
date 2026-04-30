import pygame
import random

class Snake:
    def __init__(self, color):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.dir = (10, 0)
        self.color = color
        self.score = 0
        self.level = 1
        self.speed = 10
        self.obstacles = []
        self.shield = False
        self.powerup_active = None
        self.timer = 0

    def move(self):
        head = (self.body[0][0] + self.dir[0], self.body[0][1] + self.dir[1])
        self.body.insert(0, head)
        self.body.pop()

    def spawn_obstacles(self):
        self.obstacles = []
        if self.level >= 3:
            for _ in range(self.level * 2):
                while True:
                    obs = (random.randrange(1, 48) * 10, random.randrange(1, 48) * 10)
                    if obs not in self.body and abs(obs[0] - self.body[0][0]) > 40:
                        self.obstacles.append(obs)
                        break

    def apply_powerup(self, p_type):
        self.powerup_active = p_type
        self.timer = pygame.time.get_ticks() + 5000
        if p_type == "speed": self.speed = 18
        elif p_type == "slow": self.speed = 6
        elif p_type == "shield": self.shield = True

    def check_poison(self):
        if len(self.body) > 2:
            self.body.pop()
            self.body.pop()
            return False
        return True