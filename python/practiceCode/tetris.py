import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Shapes of Tetris blocks
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]]
]

# Initialize game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Define a grid for the game
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


def draw_grid(surface, grid):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val != 0:
                pygame.draw.rect(surface, colors[val], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(surface, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


def new_shape():
    shape = random.choice(tetris_shapes)
    return shape


def draw_shape(surface, shape, position):
    for y, row in enumerate(shape):
        for x, val in enumerate(row):
            if val != 0:
                pygame.draw.rect(surface, colors[val], (
                (position[0] + x) * BLOCK_SIZE, (position[1] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(surface, BLACK, (
                (position[0] + x) * BLOCK_SIZE, (position[1] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


def check_collision(grid, shape, position):
    for y, row in enumerate(shape):
        for x, val in enumerate(row):
            if val != 0:
                if position[1] + y >= GRID_HEIGHT or position[0] + x < 0 or position[0] + x >= GRID_WIDTH or \
                        grid[position[1] + y][position[0] + x]:
                    return True
    return False


def merge_grid(grid, shape, position):
    for y, row in enumerate(shape):
        for x, val in enumerate(row):
            if val != 0:
                grid[position[1] + y][position[0] + x] = val


def clear_rows(grid):
    rows_cleared = 0
    for i in range(len(grid) - 1, -1, -1):
        if 0 not in grid[i]:
            rows_cleared += 1
            del grid[i]
            grid.insert(0, [0 for _ in range(GRID_WIDTH)])
    return rows_cleared


colors = {
    0: BLACK,
    1: (255, 0, 0),
    2: (0, 255, 0),
    3: (0, 0, 255),
    4: (255, 255, 0),
    5: (255, 0, 255),
    6: (0, 255, 255),
}


def main():
    shape = new_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    current_position = [GRID_WIDTH // 2 - len(shape[0]) // 2, 0]

    while True:
        win.fill(WHITE)
        draw_grid(win, grid)
        draw_shape(win, shape, current_position)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            current_position[0] -= 1
            if check_collision(grid, shape, current_position):
                current_position[0] += 1
        if keys[pygame.K_RIGHT]:
            current_position[0] += 1
            if check_collision(grid, shape, current_position):
                current_position[0] -= 1
        if keys[pygame.K_DOWN]:
            current_position[1] += 1
            if check_collision(grid, shape, current_position):
                current_position[1] -= 1

        if keys[pygame.K_SPACE]:
            while not check_collision(grid, shape, [current_position[0], current_position[1] + 1]):
                current_position[1] += 1

        if pygame.time.get_ticks() - fall_time > 500:
            current_position[1] += 1
            if check_collision(grid, shape, current_position):
                current_position[1] -= 1
                merge_grid(grid, shape, current_position)
                rows_cleared = clear_rows(grid)
                shape = new_shape()
                current_position = [GRID_WIDTH // 2 - len(shape[0]) // 2, 0]

            fall_time = pygame.time.get_ticks()


main()
