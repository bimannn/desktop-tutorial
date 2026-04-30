import pygame
import sys
import json
import os
import random
from game import Snake
from db import save_score, get_top_10, get_personal_best

pygame.init()
SCREEN = pygame.display.set_mode((500, 600))
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 20)

def load_settings():
    if os.path.exists("settings.json"):
        try:
            with open("settings.json", "r") as f: return json.load(f)
        except: pass
    return {"color": [0, 255, 0], "grid": True}

def draw_text(txt, x, y, color=(255,255,255)):
    SCREEN.blit(FONT.render(txt, True, color), (x, y))

def game_loop(username):
    conf = load_settings()
    s = Snake(conf["color"])
    best = get_personal_best(username)
    food = (random.randrange(1, 48)*10, random.randrange(1, 48)*10)
    poison = (random.randrange(1, 48)*10, random.randrange(1, 48)*10)
    p_up_pos = None
    p_up_type = None
    p_spawn_time = 0

    running = True
    while running:
        SCREEN.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and s.dir != (0, 10): s.dir = (0, -10)
                if event.key == pygame.K_DOWN and s.dir != (0, -10): s.dir = (0, 10)
                if event.key == pygame.K_LEFT and s.dir != (10, 0): s.dir = (-10, 0)
                if event.key == pygame.K_RIGHT and s.dir != (-10, 0): s.dir = (10, 0)

        s.move()
        head = s.body[0]

        if head == food:
            s.score += 1
            s.body.append(s.body[-1])
            food = (random.randrange(1, 48)*10, random.randrange(1, 48)*10)
            if s.score % 5 == 0:
                s.level += 1
                s.spawn_obstacles()

        if head == poison:
            if s.check_poison(): running = False
            poison = (random.randrange(1, 48)*10, random.randrange(1, 48)*10)

        if not p_up_pos and random.randint(1, 200) == 1:
            p_up_type = random.choice(["speed", "slow", "shield"])
            p_up_pos = (random.randrange(1, 48)*10, random.randrange(1, 48)*10)
            p_spawn_time = pygame.time.get_ticks()

        if p_up_pos:
            if head == p_up_pos:
                s.apply_powerup(p_up_type)
                p_up_pos = None
            elif pygame.time.get_ticks() - p_spawn_time > 8000:
                p_up_pos = None

        if head[0] < 0 or head[0] > 490 or head[1] < 0 or head[1] > 590 or head in s.body[1:] or head in s.obstacles:
            if s.shield:
                s.shield = False
                s.powerup_active = None
            else: running = False

        if s.powerup_active and pygame.time.get_ticks() > s.timer:
            s.speed = 10
            s.powerup_active = None

        if conf.get("grid", True):
            for i in range(0, 500, 10): pygame.draw.line(SCREEN, (40,40,40), (i,0), (i,600))
            for i in range(0, 600, 10): pygame.draw.line(SCREEN, (40,40,40), (0,i), (500,i))

        for b in s.body: pygame.draw.rect(SCREEN, s.color, (*b, 9, 9))
        for o in s.obstacles: pygame.draw.rect(SCREEN, (100, 100, 100), (*o, 10, 10))
        pygame.draw.rect(SCREEN, (0, 255, 0), (*food, 10, 10))
        pygame.draw.rect(SCREEN, (200, 0, 0), (*poison, 10, 10))
        if p_up_pos: pygame.draw.rect(SCREEN, (0, 255, 255), (*p_up_pos, 10, 10))

        draw_text(f"{username} | Score: {s.score} | Lvl: {s.level} | Best: {best}", 10, 10)
        pygame.display.update()
        CLOCK.tick(s.speed)

    save_score(username, s.score, s.level)

def menu():
    user = "Player"
    while True:
        SCREEN.fill((30, 30, 30))
        draw_text("SNAKE DATABASE EDITION", 130, 150, (0, 255, 0))
        draw_text(f"User: {user}", 150, 220)
        draw_text("Press ENTER to Start", 150, 280)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: game_loop(user)
                elif event.key == pygame.K_BACKSPACE: user = user[:-1]
                else:
                    if len(user) < 10: user += event.unicode
        pygame.display.update()

if __name__ == "__main__":
    menu()