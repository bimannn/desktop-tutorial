import pygame
import sys
import random
from racer import Player, Enemy, PowerUp, LANES
from persistence import load_data, save_data, update_leaderboard
from ui import draw_text, create_button


pygame.init()
WIDTH, HEIGHT = 500, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Racer")
CLOCK = pygame.time.Clock()


ROAD_COLOR = (50, 50, 50)


settings = load_data("settings.json", {"sound": True, "color": (255, 255, 0), "difficulty": 1})

def main_game(username):
    speed = 5 + settings["difficulty"]
    score = 0
    distance = 0
    player = Player(settings["color"])
    
    enemies = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)
    
    active_powerup = None
    nitro_end_time = 0
    running = True

    while running:
        SCREEN.fill(ROAD_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        current_speed = speed + (distance // 1000)
        
        
        if len(enemies) < 2:
            new_enemy = Enemy(current_speed)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        
        if random.randint(1, 250) == 1:
            p = PowerUp(random.choice(['nitro', 'shield']))
            powerups.add(p)
            all_sprites.add(p)

        
        player.move()
        enemies.update()
        powerups.update(current_speed)
        distance += current_speed / 10
        score += 0.1

        
        if pygame.sprite.spritecollide(player, enemies, True):
            if player.has_shield:
                player.has_shield = False
                active_powerup = None
            else:
                update_leaderboard(username, score, distance)
                return "GAME_OVER"

        
        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if hit.type == 'nitro':
                speed += 5
                nitro_end_time = pygame.time.get_ticks() + 4000
                active_powerup = "Nitro"
            elif hit.type == 'shield':
                player.has_shield = True
                active_powerup = "Shield"

        
        if active_powerup == "Nitro" and pygame.time.get_ticks() > nitro_end_time:
            speed -= 5
            active_powerup = None

        
        all_sprites.draw(SCREEN)
        draw_text(SCREEN, f"Score: {int(score)}", 25, 70, 30)
        draw_text(SCREEN, f"{int(distance)}m", 20, 70, 60)
        
        if active_powerup:
            draw_text(SCREEN, f"Buff: {active_powerup}", 20, 400, 30, (0, 255, 255))

        pygame.display.update()
        CLOCK.tick(60)

def main_menu():
    username = "Player"
    entering_name = True
    
    while True:
        SCREEN.fill((30, 30, 30))
        draw_text(SCREEN, "STREET RACER", 50, WIDTH//2, 100)
        draw_text(SCREEN, f"Name: {username}", 30, WIDTH//2, 200, (200, 200, 200))
        
        if create_button(SCREEN, "START GAME", 150, 300, 200, 50, (0, 150, 0), (0, 200, 0)):
            res = main_game(username)
            

        if create_button(SCREEN, "QUIT", 150, 400, 200, 50, (150, 0, 0), (200, 0, 0)):
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if len(username) < 10:
                        username += event.unicode

        pygame.display.update()
        CLOCK.tick(60)

if __name__ == "__main__":
    main_menu()