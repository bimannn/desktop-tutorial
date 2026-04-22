import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

snake = [(100, 100)]
direction = (10, 0)

food = (200, 200)

score = 0
level = 1
speed = 10

font = pygame.font.SysFont(None, 25)

def random_food():
    while True:
        x = random.randrange(0, WIDTH, 10)
        y = random.randrange(0, HEIGHT, 10)
        if (x, y) not in snake:
            return (x, y)

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -10)
    if keys[pygame.K_DOWN]:
        direction = (0, 10)
    if keys[pygame.K_LEFT]:
        direction = (-10, 0)
    if keys[pygame.K_RIGHT]:
        direction = (10, 0)

    # Движение змейки
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Проверка выхода за границы
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    # Проверка столкновения с собой
    if head in snake:
        running = False

    snake.insert(0, head)

    # Еда
    if head == food:
        score += 1
        food = random_food()

        # Уровни
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Рисование
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))

    pygame.draw.rect(screen, (255, 0, 0), (*food, 10, 10))

    # Текст
    text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()