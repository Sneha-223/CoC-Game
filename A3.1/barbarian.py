from re import S
import numpy as np
from person import *
from global_vars import *

class Barbarian(Person):

    def __init__(self, x, y):

        self.health = 100
        self.damage = 2
        self.spawned = 0
        Person.__init__(self, x, y)
    
    def barbarian_pos(self, grid):
        
        x = self.get_x()
        y = self.get_y()

        grid[x][y] = 'B' 

    def move(self, grid):

        dist = 500
        building_num = 0
        hut_num = 0
        building_x = 0
        building_y = 0

        if len(building_coords) == 0:
            return
        
        for i in range(cannon1_x - 7, cannon1_x + 7):
            for j in range(cannon1_y - 7, cannon1_y + 7):
                if i == self.get_x() and j == self.get_y():
                    self.health -= 5
        
        for i in range(cannon2_x - 7, cannon2_x + 7):
            for j in range(cannon2_y - 7, cannon2_y + 7):
                if i == self.get_x() and j == self.get_y():
                    self.health -= 5

        for key, value in building_coords.items():
            point1 = np.array([self.get_x(), self.get_y()])
            point2 = np.array([value[0], value[1]])
            temp = np.linalg.norm(point2 - point1)
            
            if temp < dist :
                dist = temp 
                building_num = key
            
        coords = building_coords.get(building_num)
        building_x = coords[0]
        building_y = coords[1]
        print(building_x, building_y)
        print(self.get_x(), self.get_y())
        print(dist)

        if building_x < self.get_x():          #building is above the barbarian
            #print("barbarian here1")
            if grid[self.get_x()-1][self.get_y()] == '-':
                grid[self.get_x()][self.get_y()] = '-'
                self.set_x(self.get_x()-1)
                grid[self.get_x()][self.get_y()] = 'B'
                
            elif grid[self.get_x()-1][self.get_y()] == 'H':         #B is to below the hut
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

            elif grid[self.get_x()-1][self.get_y()] == 'T':
                townhalls[0].health -= self.damage
                townhalls[0].set_health(townhalls[0].health)

                if townhalls[0].health <= 0:
                    building_coords.pop(5)
                
            
            elif grid[self.get_x()-1][self.get_y()] == '#':
                grid[self.get_x()-1][self.get_y()] = '-'

            
            
        
        elif building_x > self.get_x():        #building is below the barbarian   
            #print("barbarian here2")
            if grid[self.get_x()+1][self.get_y()] == '-':
                grid[self.get_x()][self.get_y()] = '-'
                self.set_x(self.get_x()+1)
                grid[self.get_x()][self.get_y()] = 'B'

            elif grid[self.get_x()+1][self.get_y()] == 'H':     #B is to above the hut
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
                        
            elif grid[self.get_x()+1][self.get_y()] == 'T':
                townhalls[0].health -= self.damage 
                townhalls[0].set_health(townhalls[0].health)

                if townhalls[0].health <= 0:
                    building_coords.pop(5)
            
            elif grid[self.get_x()+1][self.get_y()] == '#':
                grid[self.get_x()+1][self.get_y()] = '-'
            

        elif building_y < self.get_y():        #building is to the left of the barbarian
            #print("barbarian here3")
            if grid[self.get_x()][self.get_y()-1] == '-':
                grid[self.get_x()][self.get_y()] = '-'
                self.set_y(self.get_y()-1)
                grid[self.get_x()][self.get_y()] = 'B'
            
            elif grid[self.get_x()][self.get_y()-1] == 'H':     #B is to the right of the hut
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
            
            elif grid[self.get_x()][self.get_y()-1] == 'T':
                townhalls[0].health -= self.damage 
                townhalls[0].set_health(townhalls[0].health)

                if townhalls[0].health <= 0:
                    building_coords.pop(5)
            
            elif grid[self.get_x()][self.get_y()-1] == '#':
                grid[self.get_x()][self.get_y()-1] = '-'
                   
            
        
        elif building_y > self.get_y():       #building is to the right of the barbarian
            #print("barbarian here4")
            if grid[self.get_x()][self.get_y()+1] == '-':    
                grid[self.get_x()][self.get_y()] = '-'
                self.set_y(self.get_y()+1)
                grid[self.get_x()][self.get_y()] = 'B'

            elif grid[self.get_x()][self.get_y()+1] == 'H':     #B is to the left of the hut
                for key, value in hut_coords.items():
                
                    if (self.get_y()+1)==value[1]:
                        huts[key].health -= self.damage 
                        huts[key].set_health(huts[key].health)
                        hut_num = key

                        if huts[hut_num].health <= 0:
                            building_coords.pop(hut_num)
                            hut_coords.pop(hut_num)
                            huts[hut_num].exists == 0
                        break

            elif grid[self.get_x()][self.get_y()+1] == 'T':
                townhalls[0].health -= self.damage 
                townhalls[0].set_health(townhalls[0].health)

                if townhalls[0].health <= 0:
                    building_coords.pop(5)
            
            elif grid[self.get_x()][self.get_y()+1] == '#':
                grid[self.get_x()][self.get_y()+1] = '-'
        
        

        

