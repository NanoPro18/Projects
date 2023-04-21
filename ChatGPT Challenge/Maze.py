import pygame
import matplotlib as plt
import numpy as np
from numpy import random as rnd


# Neigbourg
def get_neighbors(Grid, x, y, rad):
    neighbors = []
    for i in range(x - rad, x + rad + 1):
        for j in range(y - rad, x + rad + 1):
            if i >= 0 and j >= 0 and i < len(Grid) and j < len(Grid[0]):
                neighbors.append(Grid[i][j])
    return neighbors


# Initialize Pygame
pygame.init()

# Set the screen size and title
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze")

# Stand-in Values
x1 = 1
x2 = 1
y1 = 1
y2 = 1

# Color
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Grey = (128, 128, 128)

# Line Parameter
line_color = Grey
line_width = 5

# Line Vertical 1
line1_start = (0, 0)
line1_end = (0, 600)

# Line Vertical 2
line2_start = (100, 0)
line2_end = (100, 600)

# Line Vertical 3
line3_start = (200, 0)
line3_end = (200, 600)

# Line Vertical 4
line4_start = (300, 0)
line4_end = (300, 600)

#Line Vertical 5
line5_start = (400, 0)
line5_end = (400, 600)

# Line Vertical 6
line6_start = (500, 0)
line6_end = (500, 600)

# Line Vertical 7
line7_start = (600, 0)
line7_end = (600, 600)

# Line Vertical 8
line8_start = (700, 0)
line8_end = (700, 600)

# Line Vertical 9
line9_start = (800, 0)
line9_end = (800, 600)

# Line Horizontal 10
line10_start = (0, 0)
line10_end = (800, 0)

# Line Horizontal 11
line11_start = (0, 100)
line11_end = (800, 100)

# Line Horizontal 12
line12_start = (0, 200)
line12_end = (800, 200)

# Line Horizontal 13
line13_start = (0, 300)
line13_end = (800, 300)

# Line Horizontal 14
line14_start = (0, 400)
line14_end = (800, 400)

# Line Horizontal 15
line15_start = (0, 500)
line15_end = (800, 500)

# Line Horizontal 16
line16_start = (0, 600)
line16_end = (800, 600)

x_rect_position = 40
y_rect_position = 40

# Textbox
font = pygame.font.Font(None, 20)
text_box = pygame.Rect(x_rect_position, y_rect_position, 20, 20)

# Create a grid
grid_width = 800
grid_height = 600

# Subdivide the grid
x1 = 0
x2 = 100
y1 = 0
y2 = 100

# Fill screen
screen.fill(White)

# Grid
Grid = [[1, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 1],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1]]

# Visual Grid Numbering
grid_number = 1

# Draw a line on every point
while True:

    # Vertical
    pygame.draw.line(screen, line_color, line1_start, line1_end, line_width)
    pygame.draw.line(screen, line_color, line2_start, line2_end, line_width)
    pygame.draw.line(screen, line_color, line3_start, line3_end, line_width)
    pygame.draw.line(screen, line_color, line4_start, line4_end, line_width)
    pygame.draw.line(screen, line_color, line5_start, line5_end, line_width)
    pygame.draw.line(screen, line_color, line6_start, line6_end, line_width)
    pygame.draw.line(screen, line_color, line7_start, line7_end, line_width)
    pygame.draw.line(screen, line_color, line8_start, line8_end, line_width)
    pygame.draw.line(screen, line_color, line9_start, line9_end, line_width)

    # Horizontal
    pygame.draw.line(screen, line_color, line10_start, line10_end, line_width)
    pygame.draw.line(screen, line_color, line11_start, line11_end, line_width)
    pygame.draw.line(screen, line_color, line12_start, line12_end, line_width)
    pygame.draw.line(screen, line_color, line13_start, line13_end, line_width)
    pygame.draw.line(screen, line_color, line14_start, line14_end, line_width)
    pygame.draw.line(screen, line_color, line15_start, line15_end, line_width)
    pygame.draw.line(screen, line_color, line16_start, line16_end, line_width)
    
    # Next values (don't touch or suffer the while loop)
    x1 = x2
    x2 += 100
    y1 = y2
    y2 += 100

    # Grid number showing
    # Color
    for row in range(len(Grid)):
        for col in range(len(Grid[row])):
            if Grid[row][col] == 1:
                text_surface = font.render(str(grid_number), True, Blue)
                text_color = Red
                print(str(row) + "  :  " + str(col) + "  :::  " + "1")
            elif Grid[row][col] == 0:
                text_surface = font.render(str(grid_number), True, Red)
                text_color = Blue
                print(str(row) + "  :  " + str(col) + "  :::  "+ "0")
    
    # Draw the numbers     
    pygame.draw.rect(screen, White, text_box, 2)
    text_surface = font.render(str(grid_number), True, text_color)

    # Show
    screen.blit(text_surface, (x_rect_position + 5, y_rect_position + 5))
    
    # Grid number
    grid_number += 1
    x_rect_position += 100

    # Log
    #print("grid number : " + str(grid_number))
    #print("x : " + str(x))
    #print("y : " + str(y))

    # Next line
    if x_rect_position >= 840:
        x_rect_position = 40
        y_rect_position += 100

    # Break loop
    if grid_number == 49:
        break
    # Fallback
    elif x1 == 100000:
        error = 0
        while error <= 5:
            print("Error")
            error += 1

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state
    
    # Draw to the screen
    pygame.display.flip()  # Update the screen

# Quit Pygame
pygame.quit()