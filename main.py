import time

def starting_screen():
    print("The game starts now")
    print("...3")
    time.sleep(1)
    print("...2")
    time.sleep(1)
    print("...1")
    time.sleep(1)

def create_board():

    board = [str(x+1) for x in range(9)]
    
    #board[2]= "X"
    #board[4]= "[O]"
    return board

def print_board(board):

    for x, board_tile in enumerate((board), 1):
        if x % 3 == 0:
            print(f"[{board_tile}]", "\n")
        else:
            print(f"[{board_tile}]", end=" ")

def winning_conditions(board):
    
    #increments are i+1; i+3; i % 2 == 0 !=1

    for i in range(0,7,3):
         if board[i] == board [i+1] == board[i+2]:
            if board[i] == "X":
                print("Player 1 won")
                return -1
            else:
                print("Player 2 won")
                return -1
    for i in range(0,3,1):
         if board[i] == board [i+3] == board[i+6]:
            if board[i] == "X":
                print("Player 1 won")
                return -1
            else:
                print("Player 2 won")
                return -1

    if board [0] == board [4] == board [8]:
        if board [0] == "X":
            print("Player 1 won")
            return -1
        else:
            print("PLayer 2 won")
            return -1
    if board [2] == board [4] == board [6]:
        if board [2] == "X":
            print("Player 1 won")
            return -1
        else:
            print("Player 2 won")
            return -1

 
def get_input(board):

    invalid = True
    while (invalid):
        action = input("Enter a number of an open tile or you lose: ")
        try:
            if int(action) in range(1, 10):
                #print(action, f"{board[int(action)-1]}" + "This is my position")
                if board[int(action)-1] == "X" or board[int(action)-1] == "O":
                        print("Spot already taken.. you lose")
                        return -1
                else:
                    invalid = False
                    return int(action)-1

        except ValueError:
            print("I said enter a number... you lose")
            return -1
        else:
            print("Haha, you lost")
            return -1
            

def player_action(board):

    r_counter = 0
    while r_counter < 9:
        r_counter += 1
        #print(f'{r_counter}')

        if r_counter % 2 > 0:
            pass
            print("Player 1 it's your turn")
            action = get_input(board)
            if action == -1:
               return -1 
            board[action] = "X"
            print_board(board)
            x = winning_conditions(board)
            if x == -1:
                return -1
        else:
            print("Player 2 it's your turn")
            action = get_input(board)
            if action == -1:
                return -1
            board[action] = "O"
            print_board(board)
            x = winning_conditions(board)
            if x == -1:
                return -1



playagain ="yes"
while playagain == "yes":
    starting_screen()
    board = create_board()
    print_board(board)
    player_action(board)
    print("Do you want to play again? type yes")
    playagain = input()