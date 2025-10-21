import time
import random


def starting_screen():
    print("Hello, this is my TicTacToe game.\nJust for your information, any wrong input will result in a loss.\n" \
    "Before you start the game you have to decide whether you want to play versus a second player or against AI.\nHave fun! ")
    
    invalid = True
    while (invalid):
        decide_player = input("Player or AI?: ")
        if decide_player == "Player":
            return -1
        if decide_player == "AI":
            return
        if decide_player != "Player" or "AI":
            print("Enter either 'Player' or 'AI'")
        
    
def game_starts():
    
    print("Game is starting in")
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
    
    #rows
    for i in range(0,7,3):
         if board[i] == board [i+1] == board[i+2]:
            if board[i] == "X":
                print("Player 1 won")
                return -1
            else:
                print("Player 2 won")
                return -1
    #columns
    for i in range(0,3,1):
         if board[i] == board [i+3] == board[i+6]:
            if board[i] == "X":
                print("Player 1 won")
                return -1
            else:
                print("Player 2 won")
                return -1
    #diagonal
    if board [0] == board [4] == board [8]:
        if board [0] == "X":
            print("Player 1 won")
            return -1
        else:
            print("PLayer 2 won")
            return -1
    #diagonal
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

def check_board(board):
    #if second choose middle--> if corner is free chose a random corner

    #rows
  """  for i in range(0,7,3):
        #checks for board[2,5,8] numpad 3,6,9
        if board[i] == board [i+1] == board[""]:
            if board[""] == "X" or "O":
                return 
    for i in range(0,7,3):
        #checks board [1,4,7] 
        if board[i] == board [""] == board[i+2]:
            if board[""] == "X" or "O":
                return 
        #check [0,3,6]
    for i in range(0,7,3):
        if board[""] == board [i+1] == board[i+2]:
            if board[""] == "X" or "O":
                return 
            
    #columns       
    for i in range(0,3,1):
         if board[i] == board [i+3] == board[""]:
            if board[""] == "X" or "O":
                return 
                   
    for i in range(0,3,1):
         if board[i] == board [""] == board[i+6]:
            if board[""] == "X" or "O":
                return 
      
    for i in range(0,3,1):
         if board[""] == board [i+3] == board[i+6]:
            if board[""] == "X" or "O":
                return 
    #diagonals
    if board [""] == board [4] == board [8]:
        if board [""] == "X" or "O":
            return 1
    
    if board [0] == board [""] == board [8]:
        if board [""] == "X" or "O":
            return 4
    
    if board [0] == board [4] == board [""]:
        if board [""] == "X" or "O":
            return 8
    
    if board [2] == board [4] == board [""]:
        if board [""] == "X" or "O":
            return 6
    
    if board [2] == board [""] == board [6]:
        if board [""] == "X" or "O":
            return 4
    
    if board [""] == board [4] == board [6]:
        if board [""] == "X" or "O":
            return 2"""



def ai_moves(board):
    """Rules to set... 
    1. look for a win, if possible, win
    2. Block a potential enemy win
    3. look if enemy could place somewhere with 2 win cons.. if so, create win con to block their path
    4. Place X or O for 2 win conditions
    5. Place 1 win con
    6. if there is no other way but a draw, make a random move
    7. if ai is the first player, make a move in one corner
    8. the second move..."""
    move = 6 #check_board(board)
    return move       

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
            
def player_action_ai_action(board):

    p1 = ["Player", "AI"]
    res = random.choice(p1)
    if res == "Player":

         
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
                action = ai_moves(board)
                if action == -1:
                    return -1
                board[int(action)] = "O"
                print_board(board)
                x = winning_conditions(board)
                if x == -1:
                    return -1
            
    if res == "AI":
         
        r_counter = -1
        while r_counter < 9:
            r_counter += 1
            print(f'{r_counter}')
        
            if r_counter == 0:
                print("My turn!")
                first_move =[1, 3, 7, 9]
                res = random.choice(first_move)
                action = res
                board[int(action-1)] = "X"
                print_board(board)
                x = winning_conditions(board)
                if x == -1:
                    r_counter +=1
                    return -1
            
        #print(f'{r_counter}')    
            if r_counter % 2 > 0:
                    print("It's my turn!")
                    action = ai_moves(board)
                    if action == -1:
                        return -1
                    board[int(action)-1] = "X"
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
pass

playagain ="yes"
while playagain == "yes":
    if starting_screen() == -1:
        game_starts()
        board = create_board()
        print_board(board)
        player_action(board)
        print("Do you want to play again? type yes")
        playagain = input()
    else:
        game_starts()
        board = create_board()
        print_board(board)
        player_action_ai_action(board)
        print("Do you want to play again? type yes")
        playagain = input()