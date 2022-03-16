import numpy as np
from person import *
from global_vars import *

class King(Person):

    def __init__(self, x, y):

        self.health = 100
        self.damage = 5
        Person.__init__(self, x, y)
    
    def king_pos(self, grid):
        
        x = self.get_x()
        y = self.get_y()

        grid[x][y] = 'K' 

    def move(self, grid, char):
        
        for i in range(cannon1_x - 7, cannon1_x + 7):
            for j in range(cannon1_y - 7, cannon1_y + 7):
                if i == self.get_x() and j == self.get_y():
                    self.health -= 5
        
        for i in range(cannon2_x - 7, cannon2_x + 7):
            for j in range(cannon2_y - 7, cannon2_y + 7):
                if i == self.get_x() and j == self.get_y():
                    self.health -= 5
        
        if char == 'w' and grid[self.get_x()-1][self.get_y()] == '-':
            grid[self.get_x()][self.get_y()] = '-'
            grid[self.get_x()-1][self.get_y()] = 'K'
            self.set_x(self.get_x()-1)
        
        elif char == 's' and grid[self.get_x()+1][self.get_y()] == '-':
            grid[self.get_x()][self.get_y()] = '-'
            grid[self.get_x()+1][self.get_y()] = 'K'
            self.set_x(self.get_x()+1)
        
        elif char == 'a' and grid[self.get_x()][self.get_y()-1] == '-':
            grid[self.get_x()][self.get_y()] = '-'
            grid[self.get_x()][self.get_y()-1] = 'K'
            self.set_y(self.get_y()-1)
        
        elif char == 'd' and grid[self.get_x()][self.get_y()+1] == '-':
            grid[self.get_x()][self.get_y()] = '-'
            grid[self.get_x()][self.get_y()+1] = 'K'
            self.set_y(self.get_y()+1)
        
    def king_attack(self, grid, char):
        #print("inside attack")
        
        #attacking the walls
        if char == ' ' :
            if grid[self.get_x()][self.get_y()+1] == '#':
                grid[self.get_x()][self.get_y()+1] = '-'
                #print("wall here")
            elif grid[self.get_x()][self.get_y()-1] == '#':
                grid[self.get_x()][self.get_y()-1] = '-'
            elif grid[self.get_x()+1][self.get_y()] == '#':
                grid[self.get_x()+1][self.get_y()] = '-'
            elif grid[self.get_x()-1][self.get_y()] == '#':
                grid[self.get_x()-1][self.get_y()] = '-'

            #attacking townhall
            elif grid[self.get_x()][self.get_y()+1] == 'T':
                #print("townhall here")
                townhalls[0].health -= self.damage 
                #print(townhalls[0].health)
                townhalls[0].set_health(townhalls[0].health)
                if townhalls[0].health <= 0:
                    building_coords.pop(5)
            elif grid[self.get_x()][self.get_y()-1] == 'T':
                townhalls[0].health -= self.damage 
                #print(townhalls[0].health)
                townhalls[0].set_health(townhalls[0].health)
                if townhalls[0].health <= 0:
                    building_coords.pop(5)

            elif grid[self.get_x()+1][self.get_y()] == 'T':
                townhalls[0].health -= self.damage 
                #print(townhalls[0].health)
                townhalls[0].set_health(townhalls[0].health)
                if townhalls[0].health <= 0:
                    building_coords.pop(5)
            elif grid[self.get_x()-1][self.get_y()] == 'T':
                townhalls[0].health -= self.damage 
                #print(townhalls[0].health)
                townhalls[0].set_health(townhalls[0].health)
                if townhalls[0].health <= 0:
                    building_coords.pop(5)


            #attacking huts
            elif grid[self.get_x()][self.get_y()+1] == 'H':     #K is to the left of the hut
                for key, value in hut_coords.items():
                    
                    #for val in value:
                        if (self.get_y()+1)==value[1]:
                            huts[key].health -= self.damage 
                            huts[key].set_health(huts[key].health)
                            hut_num = key

                            if huts[hut_num].health <= 0:
                                building_coords.pop(hut_num)
                                hut_coords.pop(hut_num)
                                huts[hut_num].exists == 0
                            break
                #print(townhalls[0].health)
                
            elif grid[self.get_x()][self.get_y()-1] == 'H':     #K is to the right of the hut
                for key, value in hut_coords.items():
                    if (self.get_y()-1)==value[1]+2:
                        huts[key].health -= self.damage 
                        huts[key].set_health(huts[key].health)
                        hut_num = key

                        if huts[hut_num].health <= 0:
                            building_coords.pop(hut_num)
                            hut_coords.pop(hut_num)
                            huts[hut_num].exists == 0
                        break
            elif grid[self.get_x()+1][self.get_y()] == 'H':     #K is to above of the hut
                for key, value in hut_coords.items():
                    if (self.get_x()+1)==value[0]:
                        huts[key].health -= self.damage 
                        huts[key].set_health(huts[key].health)
                        hut_num = key

                        if huts[hut_num].health <= 0:
                            building_coords.pop(hut_num)
                            hut_coords.pop(hut_num)
                            huts[hut_num].exists == 0
                        break
            elif grid[self.get_x()-1][self.get_y()] == 'H':       #K is to below of the hut
                for key, value in hut_coords.items():
                    if (self.get_x()-1)==value[0]+1:
                        huts[key].health -= self.damage 
                        huts[key].set_health(huts[key].health)
                        hut_num = key

                        if huts[hut_num].health <= 0:
                            building_coords.pop(hut_num)
                            hut_coords.pop(hut_num)
                            huts[hut_num].exists == 0
                        break
            #print(grid[self.get_x()][self.get_y()+1])

    def display_health(self):
        bar = '|'
        for i in range(int(self.health / 5)):
            #bar += '■'
            bar += '*'

        for _ in range(int((100 - self.health) / 5)):
            bar += ' '
        bar += '|'
        print (bar)

        

