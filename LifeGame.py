# Import necessary libraries
import pygame
import numpy as np

# Define colors for different cell states
col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (20, 20, 42)
col_grid = (30, 30, 60)

def update(surface, cur, sz):
    """
    Update the game state for the next generation.

    Parameters:
        surface (pygame.Surface): The Pygame surface to draw on.
        cur (numpy.ndarray): The current generation of cells.
        sz (int): The size of each cell.

    Returns:
        numpy.ndarray: The next generation of cells.
    """
    # Create a new array for the next generation
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    # Define the new size for each cell
    smaller_sz = int(sz / 2)

    # Loop through each cell in the current generation
    for r, c in np.ndindex(cur.shape):
        # Count the number of alive neighbors
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

        # Check the rules of the Game of Life and update the next generation
        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = col_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            col = col_alive

        # Set the color for the current cell based on its state
        col = col if cur[r, c] == 1 else col_background

        # Draw each cell with the smaller size
        pygame.draw.rect(surface, col, (c * sz, r * sz, smaller_sz, smaller_sz))

    return nxt

# Load a predefined pattern from a numpy array
openedarray = np.load('C:/Users/jeanc/Desktop/Languages/New folder/game life/numpy_array.npy')

def init(dimx, dimy):
    """
    Initialize the game with a predefined pattern.

    Parameters:
        dimx (int): The number of cells in the x-direction.
        dimy (int): The number of cells in the y-direction.

    Returns:
        numpy.ndarray: The initial state of the cells.
    """
    # Initialize the cells array and place the predefined pattern at a specific position
    cells = np.zeros((dimy, dimx))
    pattern = openedarray
    pos = (3, 3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells

def main(dimx, dimy, cellsize):
    """
    Main function to run the Game of Life simulation.

    Parameters:
        dimx (int): The number of cells in the x-direction.
        dimy (int): The number of cells in the y-direction.
        cellsize (int): The size of each cell in pixels.
    """
    # Initialize Pygame
    pygame.init()
    
    # Set up the display surface
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Let's go les 3ième")

    # Initialize the cells array with the predefined pattern
    cells = init(dimx, dimy)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the surface with the grid color
        surface.fill(col_grid)
        
        # Update and draw the next generation of cells
        cells = update(surface, cells, cellsize)
        
        # Update the display
        pygame.display.update()

if __name__ == "__main__":
    # Start the game with specific dimensions and cell size
    main(120, 150, 10)
