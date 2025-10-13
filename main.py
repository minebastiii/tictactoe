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


def player_action(board):

    r_counter = 0
    while r_counter < 9:
        r_counter += 1
        print(f'{r_counter}')

        if r_counter % 2 > 0:
            pass
            print("Player 1 it's your turn")
            action = input("Enter a Number:")
            board[int(action)-1] = "X"
            print_board(board)
        else:
            print("Player 2 it's your turn")
            action = input("Enter a Number:")
            board[int(action)-1] = "O"
            print_board(board)
            
board = create_board()
print_board(board)
player_action(board)