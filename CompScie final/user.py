from tile import *
from enime import *


num_pieces = []
player_board = [[tile() for _ in range(9)] for _ in range(9)]

battleships = {
    1: 1,  
    2: 2,  
    3: 4,  
    4: 1,  
}

def is_in_bounds(row, col, direction, size):
    if direction == 'u':
        return row - size + 1 >= 0
    elif direction == 'd':
        return row + size - 1 < 9
    elif direction == 'l':
        return col - size + 1 >= 0
    else:
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

def check_correct(deman):
    if len(demand) != 4:
        return False
    
    row = demand[0]
    col = demand[1]
    direction = demand[2]
    size = demand[3]
    
    if not row.isdigit() or not col.isdigit() or not size.isdigit():
        return False
    
    row = int(row)
    col = int(col)
    size = int(size)
    
    if 0 <= row < 9 and 0 <= col < 9:
        if direction in ['u', 'd', 'l', 'r']:
            if size >= 1 and (size <= 4 or (size == 1 and direction != 'u')):
                return True

    return False

def place_ship(board, stats):
    if int(stats[0]) > -1 and int(stats[0]) < 9 and int(stats[1]) > -1 and int(stats[1]) < 9:
        row, col, direction, size = int(stats[0]), int(stats[1]), stats[2], int(stats[3])

        if not is_in_bounds(row, col, direction, size):
            print('The ship does not fit on the board in the chosen direction.')
            
            return
        elif is_collision(player_board, row, col, direction, size):
            print('There is already a ship in the location of the new ship.')
            battleships[int(size)] += 1
            return
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
    else:
        print('ship not in range')


def print_board(board, enemy):
    i = 0
    print('  0 1 2 3 4 5 6 7 8')
    for row in board:
        print(i, end=' ')
        i = i + 1
        for col in row:
            col.print_self(enemy)
        print()

def print_battleships(battleships):
    print("Remaining battleships:")
    for size, count in battleships.items():
        print(f"{count} battleships of size {size} remaining")
    print()

def attack(cords):
    enimie_board[int(cords[0])][int(cords[1])].get_hit()
    if enimie_board[int(cords[0])][int(cords[1])].has_ship:
        print('Hit!')
    else:
        print('Miss!')
    print_board(enimie_board, True)

def check_win(board):
    for row in board:
        for tile in row:
            if tile.has_ship and not tile.been_hit:
                return False  
    return True  

name = input('what is your name?')
print('hello ' + name + '!')
print('lets play a game of battlship.')
print('1. The board is 9x9, and you\'ll use numbers from 0 to 8 (inclusive) to indicate the row and column where you want to place your battleship.\n2. After choosing the location, use \'u\' for up, \'d\' for down, \'l\' for left, or \'r\' for right to indicate the direction in which your battleship should be placed.\n3. Enter a number between 1 and 4 to indicate the size of the battleship. You have one 1-sized battleship, two 2-sized battleships, four 3-sized battleships, and one 4-sized battleship.(does not matter for 1 sized ship)\n4. Make sure that the ship will actually fit on the game board\n5. Make sure there are no spaces between the commands.\nExample: If you want to place a 3-sized battleship at position (2, 5) going down, you would enter: 25d3')

demand = ''
while(battleships[1] != 0 or battleships[2] != 0 or battleships[3] != 0 or battleships[4] != 0):
    demand = list(input('where will the ship go?'))

    if(check_correct(demand)):
        if(battleships[int(demand[3])] <= 0):
            print('you already used all of that type of ship!')
        else:
            place_ship(player_board, demand) 
        if(player_board[int(demand[0])][int(demand[1])].has_ship):
            battleships[int(demand[3])] -= 1
        print_board(player_board, False)
        print_battleships(battleships)

    else:
        print('please give a valid response')

    
         
print('now let\'s give a moment for your enemy to make their board')
enimie_choose_ships()


Pwin = False
Owin = False


while not Pwin or not Owin:
    coords = list(input('Now choose a location to attack, by typing in the coordinates\nEx: if you want to attack 7 tiles down, and 4 tiles accross, type 63'))
    if(int(coords[0]) >= 0 and int(coords[0]) < 9 and int(coords[1]) >= 0 and int(coords[1]) < 9 ):
        attack(coords)
        Pwin = check_win(enimie_board)
        enemy_attack(player_board)
        Owin = check_win(player_board)

if(Pwin):
    print('Congrats you won' + name + '!')
else:
    print('Better luck next time' + name + ':(')