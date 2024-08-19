import pygame
from pygame.locals import *
import random

pygame.init()

# Window Initialization
window_X = 1280
window_Y = 720
window = pygame.display.set_mode((window_X, window_Y))
pygame.display.set_caption('Just another snake game')

clock = pygame.time.Clock()

# General Variables
red = (255,0,0)
black = (0,0,0)
green = (0, 255, 0)
blue = (0, 0, 128)
game_over = False
eaten = False
direction = 'UP'

# Fruit and snake initialization
init_cords = [(random.randint(50, 1280-50) // 15) * 15, (random.randint(50,720-50) // 15) * 15]
fruit_cords = [(random.randint(50, 1280-50) // 15) * 15, (random.randint(50,720-50) // 15) * 15]

snake = [Rect(init_cords[0], init_cords[1], 15, 15),
         Rect(init_cords[0], init_cords[1] + 15, 15, 15),
         Rect(init_cords[0], init_cords[1] + 30, 15, 15)]

fruit = Rect(fruit_cords[0], fruit_cords[1], 15, 15)

# Useful functions
def display_snake():
    for body in snake:
        pygame.draw.rect(window, red, body)

def change_direction(direct):
    if direct == 'RIGHT':
        snake.insert(0, Rect(snake[0].x + 15, snake[0].y, 15, 15))
    if direct == 'LEFT':
        snake.insert(0, Rect(snake[0].x - 15, snake[0].y, 15, 15))
    if direct == 'UP':
        snake.insert(0, Rect(snake[0].x, snake[0].y - 15, 15, 15))
    if direct == 'DOWN':
        snake.insert(0, Rect(snake[0].x, snake[0].y + 15, 15, 15))
    
    # Check if we reached fruit
    if snake[0].x != fruit.x or snake[0].y != fruit.y:
        snake.pop()
    else:
        global eaten
        eaten = True


def check_out_of_bounds():
    if snake[0].x > window_X or snake[0].x < 0 or snake[0].y > window_Y or snake[0].y < 0:
        global game_over
        game_over = True

def check_suicide():
    coords = {}
    for item in snake:
        if (item.x, item.y) in coords:
            global game_over
            game_over = True
            break
        else:
            coords[(item.x, item.y)] = 1
    del coords

# Main Logic        
while True:
    # Event Logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                direction = 'LEFT'
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                direction = 'RIGHT'
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                direction = 'UP'
        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                direction = 'DOWN'    
    
    window.fill("black")

    if game_over == False:
        change_direction(direction)

        display_snake()

        if eaten == True:
            fruit = Rect((random.randint(50, 1280-50) // 15) * 15, (random.randint(50,720-50) // 15) * 15, 15, 15)
            eaten = False

        pygame.draw.rect(window, green, fruit)

        check_out_of_bounds()

        check_suicide()
    else:
        font = pygame.font.Font('juiceitc.ttf', 62)
        text = font.render('Game Over', True, green, black)
        textRect = text.get_rect()
        textRect.center = (window_X // 2, window_Y // 2)
        window.blit(text, textRect)

    pygame.display.update()
    clock.tick(15)
