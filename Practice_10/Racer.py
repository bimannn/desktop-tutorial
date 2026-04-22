import pygame
import random

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Цвета
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Игрок
player = pygame.Rect(180, 500, 40, 60)
speed = 5

# Монеты
coins = []
coin_size = 20
coin_spawn_timer = 0

# Счет
score = 0
font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    # Ограничение движения
    if player.x < 0:
        player.x = 0
    if player.x > WIDTH - player.width:
        player.x = WIDTH - player.width

    # Спавн монет
    coin_spawn_timer += 1
    if coin_spawn_timer > 30:
        coin_spawn_timer = 0
        x = random.randint(0, WIDTH - coin_size)
        coins.append(pygame.Rect(x, 0, coin_size, coin_size))

    # Движение монет
    for coin in coins[:]:
        coin.y += 5
        if coin.colliderect(player):
            coins.remove(coin)
            score += 1
        elif coin.y > HEIGHT:
            coins.remove(coin)

    # Рисование
    pygame.draw.rect(screen, (0, 255, 0), player)

    for coin in coins:
        pygame.draw.rect(screen, YELLOW, coin)

    # Счет (правый верхний угол)
    text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()