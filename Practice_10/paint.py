import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 700))
    clock = pygame.time.Clock()
    
    # State variables
    radius = 15
    drawing_color = (255, 255, 255) # Default white
    tool = 'pencil' 
    
    # Points/shapes storage
    points = [] 
    
    # Main Loop
    while True:
        pressed_keys = pygame.key.get_pressed()
        alt_held = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
        ctrl_held = pressed_keys[pygame.K_LCTRL] or pressed_keys[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                
                # Tool Selection
                if event.key == pygame.K_r: drawing_color = (255, 0, 0)   # Red
                if event.key == pygame.K_g: drawing_color = (0, 255, 0)   # Green
                if event.key == pygame.K_b: drawing_color = (0, 0, 255)   # Blue
                if event.key == pygame.K_e: tool = 'eraser'
                if event.key == pygame.K_p: tool = 'pencil'
                if event.key == pygame.K_s: tool = 'rectangle'
                if event.key == pygame.K_c: tool = 'circle'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    start_pos = event.pos
                    if tool == 'rectangle':
                        points.append(('rect', drawing_color, pygame.Rect(start_pos, (0, 0))))
                    elif tool == 'circle':
                        points.append(('circle', drawing_color, start_pos, 0))
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if event.buttons[0]: # Left button held
                    if tool == 'pencil':
                        points.append(('line', drawing_color, position, radius))
                    elif tool == 'eraser':
                        points.append(('line', (0, 0, 0), position, radius))
                    elif tool == 'rectangle' and len(points) > 0:
                        # Update last rectangle size
                        last_rect = points[-1][2]
                        new_width = position[0] - last_rect.x
                        new_height = position[1] - last_rect.y
                        points[-1] = ('rect', drawing_color, pygame.Rect(last_rect.topleft, (new_width, new_height)))
                    elif tool == 'circle' and len(points) > 0:
                        # Update last circle radius
                        center = points[-1][2]
                        new_radius = int(((position[0]-center[0])**2 + (position[1]-center[1])**2)**0.5)
                        points[-1] = ('circle', drawing_color, center, new_radius)

        screen.fill((0, 0, 0))
        
        # Draw all stored shapes
        for shape in points:
            if shape[0] == 'line':
                pygame.draw.circle(screen, shape[1], shape[2], shape[3])
            elif shape[0] == 'rect':
                pygame.draw.rect(screen, shape[1], shape[2], 2) # 2 is border thickness
            elif shape[0] == 'circle':
                if shape[3] > 0:
                    pygame.draw.circle(screen, shape[1], shape[2], shape[3], 2)
        
        pygame.display.flip()
        clock.tick(60)

main()