'''
===============================================================================
  ________                                _____  .__  .__  _____        
 /  _____/_____    _____   ____     _____/ ____\ |  | |__|/ ____\____   
/   \  ___\__  \  /     \_/ __ \   /  _ \   __\  |  | |  \   __\/ __ \  
\    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )  |    |  |_|  ||  | \  ___/  
 \______  (____  /__|_|  /\___  >  \____/|__|    |____/__||__|  \___  > 
        \/     \/      \/     \/                                    \/
===============================================================================
'''

import pygame as pg

class GameOfLife:
    def __init__(self, size=(10, 10), cell_size=20, pallet=None):
        self.size = size
        self.cell_size = cell_size
        self.color = pallet["alive"]
        self.background_color = pallet["background"]
        self.dead_color = pallet["dead"]
        self.grid = [[0 for _ in range(size[1])] for _ in range(size[0])]  
        self.running = True
        self.paused = True
        self.show_dead = False
        # Initialize Pygame
        pg.init()
        self.screen = pg.display.set_mode((size[1] * cell_size, size[0] * cell_size))
        self.screen.fill(self.background_color)
        pg.display.set_caption("Game of Life")
        self.clock = pg.time.Clock()

    def setCellule(self, cellule, state=1):
        '''Set the state of a cellule'''
        x, y = cellule
        self.grid[y][x] = state

    def toggle_cell(self, x, y):
        '''Toggle the state of a cellule'''
        self.grid[y][x] = 1 - self.grid[y][x]

    def getNeighbours(self, cellule):
        '''A cellule can have 9 neighbours (the cellule itself and the 8 others around it)'''
        x, y = cellule
        neighbours = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                # Check if the cellule is in the grid
                if (
                    0 <= x + i < self.size[1] and
                    0 <= y + j < self.size[0]
                ):
                    neighbours.append((x + i, y + j))
        return neighbours

    def getNextState(self, cellule):
        '''Return the next state of a cellule'''
        x, y = cellule
        neighbours = self.getNeighbours(cellule)
        neighbours_state = [self.grid[y][x] for x, y in neighbours]
        alive = sum(neighbours_state)
        if self.grid[y][x] == 1 and (alive == 3 or alive == 4):
            # The cellule will survive
            return 1
        elif self.grid[y][x] == 0 and alive == 3:
            # The cellule will be born
            return 1
        else:
            # The cellule dies or stays dead
            return 0

    def addPattern(self, pattern):
        '''Add a pattern to the grid'''
        x, y = self.size[1] // 3, self.size[0] // 3
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                self.grid[y + i][x + j] = pattern[i][j]

    def create_grid_animated(self):
        for x in range(self.size[1]):
            pg.draw.line(self.screen, (40, 40, 40), (x * self.cell_size, 0), (x * self.cell_size, self.size[0] * self.cell_size))
            pg.display.flip()
            self.clock.tick(30)
            
        for y in range(self.size[0]):
            pg.draw.line(self.screen, (40, 40, 40), (0, y * self.cell_size), (self.size[1] * self.cell_size, y * self.cell_size))
            pg.display.flip()
            self.clock.tick(30)

    def updateGrid(self):
        '''Update the current grid to its next state'''
        next_grid = [[0 for _ in range(self.size[1])] for _ in range(self.size[0])]
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                next_grid[y][x] = self.getNextState((x, y))
                if self.show_dead and self.grid[y][x] == 1 and next_grid[y][x] == 0:
                    pg.draw.rect(self.screen, self.dead_color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    pg.display.flip()
                    pg.time.wait(50)
        self.grid = next_grid

    def drawGrid(self):
        '''Draw the grid on the screen'''
        self.screen.fill(self.background_color)
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                color = self.color if self.grid[y][x] == 1 else self.background_color
                pg.draw.rect(self.screen, color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        
        # Draw grid lines
        for x in range(self.size[1]):
            pg.draw.line(self.screen, (40, 40, 40), (x * self.cell_size, 0), (x * self.cell_size, self.size[0] * self.cell_size))
        for y in range(self.size[0]):
            pg.draw.line(self.screen, (40, 40, 40), (0, y * self.cell_size), (self.size[1] * self.cell_size, y * self.cell_size))
        
        pg.display.flip()

    def handleEvents(self):
        '''Handle Pygame events'''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pg.K_r:
                    self.grid = [[0 for _ in range(self.size[1])] for _ in range(self.size[0])]
                elif event.key == pg.K_d:
                    self.show_dead = not self.show_dead
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                grid_x, grid_y = x // self.cell_size, y // self.cell_size
                self.toggle_cell(grid_x, grid_y)

    def run(self):
        '''Run the Game of Life'''
        self.create_grid_animated()
        while self.running:
            self.handleEvents()
            if not self.paused:
                self.updateGrid()
            self.drawGrid()
            self.clock.tick(10)
        pg.quit()

    
    
    