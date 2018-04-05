'''
Created on 4 Apr 2018

Game of life implementation

The world is finite

@author: igoroya
'''

import copy
import time

class World:
    
    def __init__(self, width, height):
        self.__grid = list()
        self.__generation = 0
        rows = ["_" for _ in range(0, width)]
        self.__grid = [rows.copy() for _ in range(0, height)]
        
    def print(self):
        for row in self.__grid:
            for value in row:
                print(value, end='')
            print()
            
    def print_in_place(self):
        import os
        os.system('clear')#FIXME only works in unix, does now work in eclipse find a generic solution 
        print("Generation: " + str(self.__generation))
        for row in self.__grid:
            for value in row:
                print(value, end='')
            print()
    
    def set_seed(self, row, column):
        self.__grid[row][column] = "*" 
        
    def evolve_one_generation(self):
        current_generation = copy.deepcopy(self.__grid)
        next_generation = copy.deepcopy(self.__grid)
        
        for i in range(0, len(current_generation)):         
            for j in range(0, len(current_generation[i])):
                live_neighbours = self._count_live_neighbours(i, j)
                if current_generation[i][j] is "*":
                    self.update_alive(i, j, live_neighbours, next_generation)
                else:
                    pass
                    self.update_dead(i, j, live_neighbours, next_generation)
        
        self.__grid = next_generation
        self.__generation = self.__generation + 1
    
    def update_alive(self, x, y, live_neighbours, grid):
        if live_neighbours < 2 or live_neighbours > 3:
            grid[x][y] = "_"
        else:
            grid[x][y] = "*"
            
    def update_dead(self, x, y, live_neighbours, grid):
        if live_neighbours is 3:
            grid[x][y] = "*"
        else:
            grid[x][y] = "_"
        
    """
    Puts a certain seed pattern at a given grid position. 
    row and column are taken as the upper-left edge of the insertion
    point of the provided pattern
    """        
    def put_pattern_at(self, pattern, row, column):

        width_p = len(pattern)
        heighth_p= len(pattern[0])
               
        for i in range(0, width_p):
            for j in range(0, heighth_p):
                self.__grid[column+i][row+j] = pattern[i][j]
    
    def _count_live_neighbours(self, row, column):
        
        live_neighbours = 0;
        
        width = len(self.__grid[0])
        height = len(self.__grid)
                
        grid_column_size = 3
        grid_column_start = column - 1 
        grid_row_size = 3
        grid_row_start = row - 1
        
        if column is 0:
            grid_column_size = 2
            grid_column_start = column

        if row is 0:
            grid_row_size = 2
            grid_row_start = row

        #FIXME: Border conditions are probably not OK
        if row is height - 1:
            grid_row_size = 2
            grid_row_start = row - 2
      
        if column is width - 1:
            grid_column_size = 2
            grid_column_start = column - 2 
        
        for i in range(grid_row_start, grid_row_start + grid_row_size):
            for j in range(grid_column_start, grid_column_start + grid_column_size):
                if (i is row) and (j is column):
                    pass
                else:
                    if self.__grid[i][j] is "*":
                        #print("is alive!")
                        live_neighbours = live_neighbours + 1
        return live_neighbours
        
def get_glider_seed_pattern():
    pattern = [["_", "*", "_"],
              ["_", "_", "*"],
              ["*", "*", "*"]]
    return pattern
        
def get_pre_loaf_seed_pattern():
    pattern = [["_", "*", "*"],
              ["*", "_", "*"],
              ["*", "*", "*"]]
    return pattern

def get_pi_seed_pattern():
    pattern = [["*", "*", "*"],
              ["_", "_", "*"],
              ["*", "*", "*"]]
    return pattern


def get_richsp18_seed_pattern():
    pattern = [
        ["_", "*", "*", "_", "*", "*", "_", "*", "*", "_", "*", "*", "_"],
        ["*", "_", "_", "_", "_", "*", "_", "*", "_", "_", "_", "_", "*"],
        ["_", "_", "_", "_", "_", "*", "_", "*", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "*", "_", "_", "_", "*", "_", "_", "_", "_"],
        ["_", "_", "_", "*", "*", "*", "_", "*", "*", "*", "_", "_", "_"],
 
              ]
    return pattern
        
if __name__ == '__main__':
    world = World(200, 55)

    world.put_pattern_at(get_glider_seed_pattern(), 4, 1)    
    world.put_pattern_at(get_glider_seed_pattern(), 10, 3)    
    world.put_pattern_at(get_pre_loaf_seed_pattern(), 15, 6)    
    world.put_pattern_at(get_pi_seed_pattern(), 19, 11)    
    world.put_pattern_at(get_richsp18_seed_pattern(), 85, 24)    
    world.put_pattern_at(get_richsp18_seed_pattern(), 35, 24)  
    world.put_pattern_at(get_glider_seed_pattern(), 33, 13)    
    world.put_pattern_at(get_glider_seed_pattern(), 56, 36)    
    world.put_pattern_at(get_glider_seed_pattern(), 78, 20) 
    world.put_pattern_at(get_glider_seed_pattern(), 75, 19)    

    world.print_in_place() 
   
    for _ in range(0, 300):
        print("###################")
        world.evolve_one_generation()
        time.sleep(0.05)
        world.print_in_place() 
     
