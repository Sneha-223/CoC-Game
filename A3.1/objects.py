from global_vars import *
from map import *
from hut import *
from townhall import *
from cannon import *
from input import *
from king import *
from barbarian import *

#colorama.init()

board_x = 30
board_y = 110

board = Map(board_x, board_y)
board.create_map()

townhall = Townhall(board_x//2 -2, board_y//2 -2, 3, 4)
#print(board_x//2 -2, board_y//2 -2)
townhall.add_townhall(board.grid)
townhalls.append(townhall)

#townhall.set_color(board.color_grid, board.grid)

# building the walls
for i in range(board_x//2 -3, board_x//2 -3 + 6):
    for j in range(board_y//2 -3, board_y//2 -3 + 5):
        if(i == board_x//2 -3 or i == board_x//2 -3 + 5): #or j == board_y//2 -3 or j == board_y//2 -3 + 5):
            board.grid[i][j] = '#'
        if(j == board_y//2 -3 or j == board_y//2 -3 + 4):
            board.grid[i][j] = '#'
        

hut1 = Hut(2, 10, 3, 2)
hut1.add_hut(board.grid)
huts.append(hut1)

hut2 = Hut(18, 32, 3, 2)
hut2.add_hut(board.grid)
huts.append(hut2)

hut3 = Hut(7, 70, 3, 2)
hut3.add_hut(board.grid)
huts.append(hut3)

hut4 = Hut(12, 88, 3, 2)
hut4.add_hut(board.grid)
huts.append(hut4)

hut5 = Hut(26, 77, 3, 2)
hut5.add_hut(board.grid)
huts.append(hut5)

cannon1 = Cannon(cannon1_x, cannon1_y, 1, 1)
cannon1.add_cannon(board.grid)
cannons.append(cannon1)

cannon2 = Cannon(cannon2_x, cannon2_y, 1, 1)
cannon2.add_cannon(board.grid)
cannons.append(cannon2)

king = King(0, 0)
king.king_pos(board.grid)

#spawning points 
board.grid[2][100] = "@"
board.grid[6][40] = "@"
board.grid[28][95] = "@"

#creating barbarian objects
barbarian1 = Barbarian(6, 39)
barbarian2 = Barbarian(6, 39)
barbarian3 = Barbarian(6, 39)
barbarian4 = Barbarian(2, 99)
barbarian5 = Barbarian(2, 99)
barbarian6 = Barbarian(2, 99)
barbarian7 = Barbarian(28, 94)
barbarian8 = Barbarian(28, 94)
barbarian9 = Barbarian(28, 94)

barbarians.append(barbarian1)
barbarians.append(barbarian2)
barbarians.append(barbarian3)
barbarians.append(barbarian4)
barbarians.append(barbarian5)
barbarians.append(barbarian6)
barbarians.append(barbarian7)
barbarians.append(barbarian8)
barbarians.append(barbarian9)
