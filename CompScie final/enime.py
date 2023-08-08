from tile import *
import random

enimie_board = [[tile() for _ in range(9)] for _ in range(9)]

def is_in_bounds(row, col, direction, size):
    if direction == 'u':
        return row - size + 1 >= 0
    elif direction == 'd':
        return row + size - 1 < 9
    elif direction == 'l':
        return col - size + 1 >= 0
    else:  # direction == 'r'
        return col + size - 1 < 9

def is_collision(board, row, col, direction, size):
    if direction == 'u':
        for i in range(size):
            if board[row - i][col].has_ship:
                return True
    elif direction == 'd':
        for i in range(size):
            if board[row + i][col].has_ship:
                return True
    elif direction == 'l':
        for i in range(size):
            if board[row][col - i].has_ship:
                return True
    else:  # direction == 'r'
        for i in range(size):
            if board[row][col + i].has_ship:
                return True
    return False

def print_board(board, enemy):
    i = 0
    print('  0 1 2 3 4 5 6 7 8')
    for row in board:
        print(i, end=' ')
        i = i + 1
        for col in row:
            col.print_self(enemy)
        print()


battleshipsE = {
    1: 1,  
    2: 2,  
    3: 4,  
    4: 1,  
}



def place_ship(board, stats):
    if int(stats[0]) > -1 and int(stats[0]) < 9 and int(stats[1]) > -1 and int(stats[1]) < 9:
        row, col, direction, size = int(stats[0]), int(stats[1]), stats[2], int(stats[3])

        if not is_in_bounds(row, col, direction, size):
            return(False)
        elif is_collision(enimie_board, row, col, direction, size):

            return(False)
        else:

            match stats[2]:
                case 'u':
                    for i in range(size):
                        board[row-i][col].set_ship()
                case 'd':
                    for i in range(size):
                        board[row+i][col].set_ship()
                case 'l':
                    for i in range(size):
                        board[row][col-i].set_ship()
                case 'r':
                    for i in range(size):
                        board[row][col+i].set_ship()
            return(True)
    else:
        return(False)
    
def enimie_choose_ships():
    for i in battleshipsE:
        while battleshipsE[i] > 0:  
            pos_x = random.randrange(0, 9)  
            pos_y = random.randrange(0, 9)  
            re = random.randrange(0, 4)    
            direction = ''  

            if re == 0:
                direction = 'u'
            elif re == 1:
                direction = 'd'
            elif re == 2:
                direction = 'l'
            elif re == 3:
                direction = 'r'

            demandE = [pos_x, pos_y, direction, i]
            print(demandE)
            if place_ship(enimie_board, demandE):
                battleshipsE[i] -= 1


    print_board(enimie_board, True)  

def enemy_attack(board):
    last_attack_coords = (-1, -1)
    while True:
        
        pos_x = random.randrange(0, 9)
        pos_y = random.randrange(0, 9)
        target_tile = board[pos_x][pos_y]
            
        
        target_tile.get_hit()
        print(f"Enemy attacked: {pos_x}{pos_y}")
        if board[pos_x][pos_y].has_ship:
            print('Hit!')
        else:
            print('Miss!')
        
        last_attack_coords = (pos_x, pos_y)
        print_board(board, False) 
        break
