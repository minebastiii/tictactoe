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
        else:
            print("Player 2 it's your turn")
            action = get_input(board)
            board[action] = "O"
            print_board(board)
            
board = create_board()
print_board(board)
player_action(board)