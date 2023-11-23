# Import necessary libraries
import pygame
import numpy as np
import time

# Define colors for different cell states
col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (20, 20, 42)
col_grid = (30, 30, 60)




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
    # Redimensionner pattern pour qu'il rentre dans cells
    pattern_resized = pattern[:min(pattern.shape[0], cells.shape[0] - pos[0]), :min(pattern.shape[1], cells.shape[1] - pos[1])]
    cells[pos[0]:pos[0]+pattern_resized.shape[0], pos[1]:pos[1]+pattern_resized.shape[1]] = pattern_resized

    #cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
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
    
    ## TO COMPLETE ## 
    
    
    
#import du array de base
openedarray = np.load('numpy_array.npy')
    
if __name__ == "__main__":
    # Start the game with specific dimensions and cell size
    main(100, 100, 10)
