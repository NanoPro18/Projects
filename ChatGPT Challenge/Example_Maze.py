import pygame

# Initialize Pygame
pygame.init()

# Set the screen size and title
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Window")

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state

    # Draw to the screen
    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.display.flip()  # Update the screen

# Quit Pygame
pygame.quit()
