import pygame

# initialize Pygame
pygame.init()

# set the window size
window_size = (400, 400)

# create a window surface
screen = pygame.display.set_mode(window_size)

# set the font and font size
font = pygame.font.Font(None, 36)

# create a 2D matrix of size 10x10 with 1's and 0's
matrix = [
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 1]
]

# set the color values
red = (255, 0, 0)
blue = (0, 0, 255)

# loop until the user closes the window
done = False
while not done:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # clear the screen
    screen.fill((255, 255, 255))

    # iterate through the matrix and draw the text
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                text_surface = font.render('1', True, red)
            else:
                text_surface = font.render('0', True, blue)

            # draw the text
            screen.blit(text_surface, (col * 40, row * 40))

    # update the screen
    pygame.display.update()

# quit Pygame
pygame.quit()