'''
===============================================================================
  ________                                _____  .__  .__  _____        
 /  _____/_____    _____   ____     _____/ ____\ |  | |__|/ ____\____   
/   \  ___\__  \  /     \_/ __ \   /  _ \   __\  |  | |  \   __\/ __ \  
\    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )  |    |  |_|  ||  | \  ___/  
 \______  (____  /__|_|  /\___  >  \____/|__|    |____/__||__|  \___  > 
        \/     \/      \/     \/                                    \/
==============================================================================='''
import pygame as pg
class GameOfLife:
    def __init__(self,size = (10,10)):
        self.size = size
        self.grid = [[0 for x in range(size[0])] for y in range(size[1])]
        self.running = True
    
    def setCellule (self,cellule,state=1):
        '''Set the state of a cellule'''
        x,y = cellule
        self.grid[x][y] = state
    
    def toggle_cell(self, x, y):
        '''Toggle the state of a cellule'''
        self.grid[x][y] = 1 - self.grid[x][y]
    
    def getNeighbours(self,cellule):
        '''A cellule can have 9 neighbours(the cellule itself and the 8 others around it)'''
        x,y = cellule
        neighbours = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                # Check if the cellule is in the grid
                if (x+i<self.size[0] and y+j<self.size[1] and x+i>=0 and y+j>=0):
                    neighbours.append((x+i,y+j))
        return neighbours
    
    def getNextState(self,cellule):
        '''Return the next state of a cellule'''
        x,y = cellule
        neighbours = self.getNeighbours(cellule)
        neighbours_state = [self.grid[x][y] for x,y in neighbours]
        alive = sum(neighbours_state)
        if self.grid[x][y]==1 and (alive == 3 or alive ==4):
            #The cellule will survive
            return 1
        elif self.grid[x][y]==0 and (alive == 3):
            #The cellule will be born
            return 1
        else:
            #The cellule die or stay dead
            return 0
    
    def updateGrid(self):
        '''Update the current grid to it next state'''
        next_grid = [[0 for x in range(self.size[0])] for y in range(self.size[1])]
        for i in range(self.size[0]):
            for j in range (self.size[1]):
                next_grid[i][j]=self.getNextState((i,j))
        self.grid = next_grid
    

        
        


