import pygame
import random
pygame.init()

canvas = pygame.display.set_mode((640,580))
pygame.display.set_caption("ANN Snake Game")

isOver = False
isExit = False

black = [0,0,0]
red = [255,0,0]
blue = [0,0,255]
green = [0,255,0]
white = [255,255,255]
canvas.fill(black)

score = 0
snake_x = 20
snake_y = 20
snake_size = 20
apple_x = 500
apple_y = 500

snake_length = 1
snake_pos = [[snake_x,snake_y]]

isEaten = True
velocity = [0,0]
moveSpeed = snake_size
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,48)

while not isExit and not isOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and velocity[0] == 0:
                velocity[0] = 1
                velocity[1] = 0
            if event.key == pygame.K_LEFT and velocity[0] == 0:
                velocity[0] = -1
                velocity[1] = 0
            if event.key == pygame.K_UP and velocity[1] == 0:
                velocity[0] = 0
                velocity[1] = 1
            if event.key == pygame.K_DOWN and velocity[1] == 0:
                velocity[0] = 0
                velocity[1] = -1

    snake_x = snake_x  +  (moveSpeed * velocity[0])
    snake_y = snake_y  - (moveSpeed  *  velocity[1])

    for i in range(0,snake_length - 1):
        snake_pos[i][0] = snake_pos[i+1][0]
        snake_pos[i][1] = snake_pos[i+1][1]

    if abs(snake_x - apple_x) < snake_size and abs(snake_y - apple_y) < snake_size:
        isEaten = True
        score = score + 1
        snake_pos.append([apple_x,apple_y])
        snake_length = snake_length + 1
    else:
        snake_pos[snake_length - 1][0] = snake_x
        snake_pos[snake_length - 1][1] = snake_y
        
    
    if snake_x > 640 - snake_size or snake_x < 0:
        isOver = True
        print("Game Over")
    if snake_y > 580 - snake_size or snake_y < 0:
        isOver = True
        print("Game Over")

    for i in range(0, snake_length-1):
        if abs(snake_x - snake_pos[i][0]) < snake_size and abs(snake_y - snake_pos[i][1]) < snake_size:
            isOver = True
            print("Game Over")

    canvas.fill(black)
    if isEaten:
        apple_x = random.randint(0,(int)((640 - snake_size)/snake_size))
        apple_y = random.randint(0,(int)((580 - snake_size)/snake_size))
        isEaten = False
        apple_x = apple_x * snake_size
        apple_y = apple_y * snake_size

    for pos in snake_pos:
        pygame.draw.rect(canvas,blue,[pos[0], pos[1] , snake_size, snake_size])

    pygame.draw.rect(canvas,red,[apple_x,apple_y,snake_size,snake_size])
    text = font.render("Score: " + str(score),True, white)
    canvas.blit(text, [5,5])
    clock.tick(12)
    pygame.display.update()

pygame.quit()
quit()
