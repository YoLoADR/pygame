import pygame

# Intialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game lopp
running = True

while running:
    # Background
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("Up arrow is pressed")
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                print("Down arrow is pressed")
                playerY_change = 0.3
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
