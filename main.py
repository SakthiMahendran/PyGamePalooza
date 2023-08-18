import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame")

# Set up colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Set up the initial position of the square
square_size = 50
square_x = (width - square_size) // 2
square_y = (height - square_size) // 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= 5
    if keys[pygame.K_RIGHT]:
        square_x += 5
    if keys[pygame.K_UP]:
        square_y -= 5
    if keys[pygame.K_DOWN]:
        square_y += 5

    # Update the display
    screen.fill(white)
    pygame.draw.rect(screen, blue, (square_x, square_y, square_size, square_size))
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(30)
