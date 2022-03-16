from objects import *
from global_vars import *
# from map import *
# from hut import *
# from townhall import *
# from cannon import *
# from input import *
# from king import *

# import os

# #colorama.init()

# board_x = 30
# board_y = 110

# board = Map(board_x, board_y)
# board.create_map()

# #board.print_board()
# #board.add_town_hall()

# townhall = Townhall(board_x//2 -2, board_y//2 -2, 3, 4)
# townhall.add_townhall(board.grid)

# townhall.set_health(board.color_grid)

# # # building the walls
# # for i in range(board_x//2 -3, board_x//2 -3 + 6):
# #     for j in range(board_y//2 -3, board_y//2 -3 + 5):
# #         if(i == board_x//2 -3 or i == board_x//2 -3 + 5): #or j == board_y//2 -3 or j == board_y//2 -3 + 5):
# #             board.grid[i][j] = '#'
# #         if(j == board_y//2 -3 or j == board_y//2 -3 + 4):
# #             board.grid[i][j] = '#'
        


# hut1 = Hut(2, 10, 3, 3)
# hut1.add_hut(board.grid)

# hut2 = Hut(18, 32, 3, 2)
# hut2.add_hut(board.grid)

# hut3 = Hut(7, 70, 2, 3)
# hut3.add_hut(board.grid)

# hut4 = Hut(12, 88, 2, 2)
# hut4.add_hut(board.grid)

# hut5 = Hut(26, 77, 3, 3)
# hut5.add_hut(board.grid)

# cannon1 = Cannon(28, 10, 1, 1)
# cannon1.add_cannon(board.grid)

# cannon2 = Cannon(27, 100, 1, 1)
# cannon2.add_cannon(board.grid)

# king = King(0, 0)
# king.king_pos(board.grid)

# townhall.set_health(board.grid, 100)

board.print_map()

while True:
    os.system('clear')
        
    board.print_map()
    king.display_health()
    # print(len(building_coords))
    # print(len(hut_coords))
    
    if len(building_coords) <= 0 :
        game_win()


    # input = Get()
    # char = input.__call__()

    char = input_to(Get())

    if char == 'q':                             #quit the game
        quit()

    elif char == ' ':                             #king attacks    
        #print("inside game attack")
        king.king_attack(board.grid, char)
    
    
    elif char == 'l':                             #spawning point 1
        
        if num_of_barbarians < 9:

            barbarians[num_of_barbarians].barbarian_pos(board.grid)
            barbarians[num_of_barbarians].set_x(6)
            barbarians[num_of_barbarians].set_y(39)
            barbarians[num_of_barbarians].spawned = 1
            num_of_barbarians = num_of_barbarians + 1
    
    elif char == 'm':                             #spawning point 2

        if num_of_barbarians < 9:
            barbarians[num_of_barbarians].barbarian_pos(board.grid)
            barbarians[num_of_barbarians].set_x(2)
            barbarians[num_of_barbarians].set_y(99)
            barbarians[num_of_barbarians].spawned = 1
            num_of_barbarians = num_of_barbarians + 1
        
    elif char == 'n':                             #spawning point 3

        if num_of_barbarians < 9:
            barbarians[num_of_barbarians].barbarian_pos(board.grid)
            barbarians[num_of_barbarians].set_x(28)  
            barbarians[num_of_barbarians].set_y(94)
            barbarians[num_of_barbarians].spawned = 1
            num_of_barbarians = num_of_barbarians + 1
    
    elif char == 'r':                             

        king.damage *= 2
        
        for i in range(len(barbarians)):
            barbarians[i].damage *= 2 
            #print("b damage" , i, barbarians[i].damage)
    
    elif char == 'h':                             

        if king.health * 1.5 < 100 :
            king.health = king.health * 1.5
        else :
            king.health = 100
        
        for i in range(len(barbarians)):

            if barbarians[i].health * 1.5 < 100 :
                barbarians[i].health = barbarians[i].health * 1.5
            else :
                barbarians[i].health = 100
            
            
    #print("b health" , 0, barbarians[0].health)
    #print("king damage" , king.damage)

    for i in range(9):
        if barbarians[i].spawned == 1 and barbarians[i].health > 0:
            barbarians[i].move(board.grid)
    
    
    townhall.set_color(board.color_grid, board.grid)        

    for i in range(len(huts)):

        if huts[i].exists == 1:
            huts[i].set_color(board.color_grid, board.grid)

    if king.health > 0:
        king.move(board.grid, char)


    #print(len(building_coords))
    #barbarian1.move_barbarian(board.grid)
    
    b_dead = 0
    k_dead = 0

    if king.health <= 0 :
        k_dead = 1
    
    for i in range(9):
        if barbarians[i].spawned == 1 and barbarians[i].health <= 0:
            k_dead = 1
        elif barbarians[i].spawned == 1 and barbarians[i].health > 0:
            k_dead = 0
            break
    
    if b_dead == 1 and k_dead == 1:
        game_over()
    
    

    
    
    
    


    

    

    



    


