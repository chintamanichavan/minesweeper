import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
window_width = 800
window_height = 600

# Create the game window
window = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption("Minesweeper")

# Set the dimensions of the grid
grid_width = 20
grid_height = 15

# Set the size of each cell
cell_size = 40

# Set the number of mines
num_mines = 40

# Create the grid
grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]

# Create the revealed grid
revealed = [[False for _ in range(grid_width)] for _ in range(grid_height)]

# Create the flags grid
flags = [[False for _ in range(grid_width)] for _ in range(grid_height)]

# Place the mines
for _ in range(num_mines):
    while True:
        x = random.randint(0, grid_width - 1)
        y = random.randint(0, grid_height - 1)
        if grid[y][x] == 0:  # Make sure we don't place a mine on top of another
            grid[y][x] = -1
            break

# Calculate adjacent mines
for y in range(grid_height):
    for x in range(grid_width):
        if grid[y][x] == -1:  # Skip mines
            continue
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < grid_width and 0 <= ny < grid_height and
                        grid[ny][nx] == -1):
                    count += 1
        grid[y][x] = count

# Create a font object
font = pygame.font.Font(None, cell_size // 2)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_x, grid_y = x // cell_size, y // cell_size
            if event.button == 1:  # Left click
                revealed[grid_y][grid_x] = True
            elif event.button == 3:  # Right click
                flags[grid_y][grid_x] = not flags[grid_y][grid_x]  # Toggle flag

    # Redraw the screen
    window.fill((0, 0, 0))  # Fill the screen with black
    for y in range(grid_height):
        for x in range(grid_width):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if revealed[y][x]:
                if grid[y][x] == -1:  # Mine
                    pygame.draw.rect(window, (255, 0, 0), rect)  # Red color
                else:
                    text = font.render(str(grid[y][x]), True, (255, 255, 255))  # White color
                    window.blit(text, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2))
            elif flags[y][x]:
                pygame.draw.rect(window, (0, 0, 255), rect)  # Blue color
            else:
                pygame.draw.rect(window, (255, 255, 255), rect, 1)  # White color

    # Update the display
    pygame.display.flip()
