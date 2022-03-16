#global variables

#game board
board =["_","_","_",
        "_","_","_",
        "_","_","_"]

#if game still going
game_is_still_going=True

#who won? or tie?
winner=None

#variable containing the player that is up next 
current_player="X"


def display_board():
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("\n")

    
#handle a single turn of an arbitury player
def handle_turn(player):
    print(player+ "'s turn.")
    
    position= input("Chose a position from 1 to 9: ")
    
    valid=False
    while not valid:
        #making sure the input is valid
        while position not in["1","2","3","4","5","6","7","8","9"]:
            position= input("Chose a position from 1 to 9: ")
        #get correct index in our board list
        position=int(position)-1
        #and making sure the spot is available on board
        if board[position]=="_":
            valid =True
        else:
            print("you can't go there,go again :)")

    #put game piece on board
    board[position]=player
    #show the game piece on board
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()
    

def check_if_win():
    #set up global variables
    global winner
    
    #check rows
    row_winner=check_rows()
    
    #check columns
    column_winner=check_columns()
     
    #check diagonals
    diagonal_winner=check_diagonals()
    
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
        #no winner yet

    
def check_if_tie():
    global game_is_still_going
    if "_" not in board:
        game_is_still_going=False
    


def flip_player():
    #global variable we need
    global current_player
    
    #if the current player was x.then change it to O and vice versa 
    if current_player=="X":
        current_player="O"
        return current_player
    
    elif current_player=="O":
        current_player="X"
        return current_player

def check_rows():
    #setup global variable
    global game_is_still_going
    #check if any of the rows have all the same value(and they are not empty)
    row_1=board[0]==board[1]==board[2] !="_"
    row_2=board[3]==board[4]==board[5] !="_"
    row_3=board[6]==board[7]==board[8] !="_"
    #if any row is true,then there is a win
    if row_1 or row_2 or row_3:
        game_is_still_going=False
    #return the winner (x or o)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    #setup global variable
    global game_is_still_going
    
    #check if any of the columns have all the same value(and they are not empty)
    column_1=board[0]==board[3]==board[6] !="_"
    column_2=board[1]==board[4]==board[7] !="_"
    column_3=board[2]==board[5]==board[8] !="_"
    #if any column is true,then there is a win
    if column_1 or column_2 or column_3:
        game_is_still_going=False
    #return the winner (x or o)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    #setup global variable
    global game_is_still_going
    #check if any of the diagonals have all the same value(and they are not empty)
    diagonal_1=board[0]==board[4]==board[8] !="_"
    diagonal_2=board[6]==board[4]==board[2] !="_"
    
    #if any column is true,then there is a win
    if diagonal_1 or diagonal_2:
        game_is_still_going=False
    #return the winner (x or o)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return
    

def play_game():
    #displaying the board asap
    display_board()


    #while the game is still going
    while game_is_still_going:

        #handle a single turn of an arbitrary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()


        #flip the turn to the other player
        flip_player()
        
        
    #the game has ended
    if winner=="X" or winner=="O":
        print(winner + " won!")
    elif winner==None:
        print("Tie!")


#place the other function call

play_game()
