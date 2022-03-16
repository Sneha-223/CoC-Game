import os 
import numpy as np

huts = []
townhalls = []
cannons = []
barbarians = []

buildings = huts + townhalls

#x coordinates of the hut
hut_coords = {0: [2, 10], 1: [18, 32], 2: [7, 70], 3: [12, 88], 4: [26, 77]} 

#x coordinates of all the buildings 
building_coords = {0: [2, 10], 1: [18, 32], 2: [7, 70], 3: [12, 88], 4: [26, 77], 5: [13, 53]} 

num_of_barbarians = 0

cannon1_x = 10
cannon1_y = 33

cannon2_x = 19
cannon2_y = 85

def game_win():
    os.system('aplay -q ./sounds/game_win.wav&')
    print("YOU WON")

def game_over():
    print("YOU LOST!")