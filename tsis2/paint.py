import pygame
import sys
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint TSIS 2")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))


color = (0, 0, 0)


tool = "pencil"


brush_sizes = [10]
brush_index = 0
brush_size = brush_sizes[brush_index]

drawing = False
last_pos = None
start_pos = None


font = pygame.font.SysFont(None, 30)
text_input = ""
text_pos = None
typing = False

clock = pygame.time.Clock()


def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        px, py = stack.pop()

        if px < 0 or py < 0 or px >= WIDTH or py >= HEIGHT:
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        stack.append((px + 1, py))
        stack.append((px - 1, py))
        stack.append((px, py + 1))
        stack.append((px, py - 1))


running = True
while running:
    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:

            
            if event.key == pygame.K_p:
                tool = "pencil"
            if event.key == pygame.K_l:
                tool = "line"
            if event.key == pygame.K_f:
                tool = "fill"
            if event.key == pygame.K_t:
                tool = "text"

            
            if event.key == pygame.K_1:
                brush_index = 0
            if event.key == pygame.K_2:
                brush_index = 1
            if event.key == pygame.K_3:
                brush_index = 2
            brush_size = brush_sizes[brush_index]

            
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("image_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            
            if typing:
                if event.key == pygame.K_RETURN:
                    text_surface = font.render(text_input, True, color)
                    canvas.blit(text_surface, text_pos)
                    typing = False
                    text_input = ""

                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if tool == "pencil":
                drawing = True
                last_pos = event.pos

            elif tool == "line":
                drawing = True
                start_pos = event.pos

            elif tool == "fill":
                flood_fill(canvas, x, y, color)

            elif tool == "text":
                typing = True
                text_pos = event.pos
                text_input = ""

        if event.type == pygame.MOUSEBUTTONUP:
            if tool == "pencil":
                drawing = False

            elif tool == "line":
                end_pos = event.pos
                pygame.draw.line(canvas, color, start_pos, end_pos, brush_size)
                drawing = False

        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    
    if drawing and tool == "line":
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, color, start_pos, mouse_pos, brush_size)

    
    if typing:
        text_surface = font.render(text_input, True, color)
        screen.blit(text_surface, text_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()