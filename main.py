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
    
    if board [0] == "X" and board [4] == "X" and board [8] == "X":
        print("Player 1 won")
        exit()
    if board [2] == "X" and board [4] == "X" and board [6] == "X":
        print("Player 1 won")
        exit()
    if board [0] == "X" and board [1] == "X" and board [2] == "X":
        print("Player 1 won")
        exit()
    if board [3] == "X" and board [4] == "X" and board [5] == "X":
        print("Player 1 won")
        exit()
    if board [6] == "X" and board [7] == "X" and board [8] == "X":
        print("Player 1 won")
        exit()
    if board [0] == "X" and board [3] == "X" and board [6] == "X":
        print("Player 1 won")
        exit()
    if board [1] == "X" and board [4] == "X" and board [8] == "X":
        print("Player 1 won")
        exit()
    if board [2] == "X" and board [5] == "X" and board [9] == "X":
        print("Player 1 won")
        exit()
    if board [0] == "O" and board [4] == "O" and board [8] == "O":
        print("Player 2 won")
        exit()
    if board [2] == "O" and board [4] == "O" and board [6] == "O":
        print("Player 2 won")
        exit()
    if board [0] == "O" and board [1] == "O" and board [2] == "O":
        print("Player 2 won")
        exit()
    if board [3] == "O" and board [4] == "O" and board [5] == "O":
        print("Player 2 won")
        exit()
    if board [6] == "O" and board [7] == "O" and board [8] == "O":
        print("Player 2 won")
        exit()
    if board [0] == "O" and board [3] == "O" and board [6] == "O":
        print("Player 2 won")
        exit()
    if board [1] == "O" and board [4] == "O" and board [8] == "O":
        print("Player 2 won")
        exit()
    if board [2] == "O" and board [5] == "O" and board [9] == "O":
        print("Player 2 won")
        exit()
    pass

 
def get_input(board):

    invalid = True
    while (invalid):
        action = input("Enter a number of an open tile or you lose: ")
        try:
            if int(action) in range(1, 10):
                #print(action, f"{board[int(action)-1]}" + "This is my position")
                if board[int(action)-1] == "X" or board[int(action)-1] == "O":
                        print("Spot already taken.. you lose")
                        exit()
                else:
                    invalid = False
                    return int(action)-1

        except ValueError:
            print("I said enter a number... you lose")
            exit()
        else:
            print("Haha, you lost")
            exit()

def player_action(board):

    r_counter = 0
    while r_counter < 9:
        r_counter += 1
        print(f'{r_counter}')

        if r_counter % 2 > 0:
            pass
            print("Player 1 it's your turn")
            
            action = get_input(board)
            print("This is the action", action)
            board[action] = "X"
            print_board(board)
            winning_conditions(board)
        else:
            print("Player 2 it's your turn")
            action = get_input(board)
            board[action] = "O"
            print_board(board)
            winning_conditions(board)
            
board = create_board()
print_board(board)
player_action(board)