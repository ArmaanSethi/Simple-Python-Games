import random
def display_instruct():
    """Display Game Instructions"""

def ask_yes_no(question):
    print "Answer 'yes' or 'no'"
    answer = raw_input(question)
    return answer.strip()

def ask_number():
    print "Select the difficulty setting"
    print "1) Completely Random"
    print "2) Goes for the best move available"
    print "3) Goes for the Win"
    print "4) Goes for the Tie"
    return int(raw_input().strip())

def pieces():#human = pieces
    answer = raw_input("Who goes first. Answer 'Me' or 'You'.")
    if (answer.lower().strip() == "me"):
        return "X"
    else:
        return "O"
    
def new_board():
    return [" "," "," "," "," "," "," "," ", " "]

def display_board(board):
    for i in range(9):
        if((i%3)==0):
            print " "
        print board[i],"|",
    print ""

def legal_moves(board):
    """Create list of legal moves"""
    moves = []
    for i in range(9):
        if(board[i] == " "):
            moves.append(i)
    return moves

def winner(board,computer,human):
    """Determine game winner."""
    computer_pos=[]
    human_pos=[]
    winner = ((0,1,2),
              (3,4,5),
              (6,7,8),
              (0,3,6),
              (1,4,7),
              (2,5,8),
              (0,4,8),
              (2,4,6))
    for i in range(len(board)):
        if(board[i]==computer):
            computer_pos.append(i)
        if(board[i]==human):
            human_pos.append(i)
    print "ComputerPos: ", computer_pos
    print "HumanPos: ", human_pos
    for i in range(len(winner)):
        if(winner[i][0] in computer_pos)and(winner[i][1] in computer_pos)and(winner[i][2] in computer_pos):
            return computer
        if(winner[i][0] in human_pos)and(winner[i][1] in human_pos)and(winner[i][2] in human_pos):
            return human
        
    return "no"

def two_of(board,turn, winner):
    ##
    turn_pos = []
    for i in range(len(board)):
    if(board[i]==turn):
        turn_pos.append(i)

    count = 0
    win_method = 0
    for i in range(len(winner)):
        if(winner[i][0] in turn_pos):
            count+=1
        if(winner[i][1] in turn_pos):
            count+=1
        if(winner[i][2] in turn_pos):
            count+=1
        if(count ==2):
            win_method = i
            for j in range(len(winner[i])):
                if(winner[i][j] not in turn_pos):
                    return winner[i][j]
            
                   
            
    """Determind of two of same peice in row"""
    
def winning_move(board,turn):
    ##
    """Determine game winner."""
    posMoves=legal_moves(board)
    


    
def human_move(board,human):
    print"legalMoves:",legal_moves(board)    
    move = raw_input("Where would you like to place your piece?")
    while((int(move)-1) not in legal_moves(board)):
        print "invalid"
        move = raw_input("Where would you like to place your piece?")
    board[int(move)-1] = human

def level_one(board,computer):
        placement = random.randrange(len(board))
        while(placement not in legal_moves(board)):
            placement = random.randrange(len(board))            
        board[placement] = computer

def level_two(board,computer):
        print"legalMoves:",legal_moves(board)
        if(4 in legal_moves(board)):
            board[4] = computer
            print"middle"
        elif((0 in legal_moves(board))or(2 in legal_moves(board))or(6 in legal_moves(board))or(8 in legal_moves(board))):
            placement = random.randrange(5)*2
            while(placement not in legal_moves(board)):
                placement = random.randrange(5)*2
            board[placement] = computer
            print"corner"
        else:
            placement = random.randrange(4)*2+1
            while(placement not in legal_moves(board)):
                placement = random.randrange(4)*2+1
            board[placement] = computer
            print"edge"

    
def computer_move(board,computer,human, difficulty):
    #"""Make Computer move""" 
    #4 cases of randomness
    print "Difficulty =",difficulty
    if(difficulty == 1):
        level_one(board,computer)
    if(difficulty == 2):
        level_two(board,computer)
    if(difficulty == 3):
        #win if possible
        winning_move(board, computer)
        if(winning_move != "no"):
            board[winning_move] = computer
        else:
            level_two(board,computer)
    if(difficulty == 4):
        #block then win
        print"Level 4"
        if(winning_move(board,human) != "no"):
            print "Block"
            board[winning_move] = computer
        else:     
            if(winning_move(board,human) != "no"):
                board[winning_move] = computer
            else:
                level_two(board,computer)

            
def next_turn(turn):
    if (turn == "X"):
        return "O"
    else:
        return "X"

def congrat_winner(the_winner, computer, human):
    """Congradulate the winner."""
    if(the_winner == human):
        print "HUMAN WINS!!!", human,"WINS!!!"
    elif(the_winner == computer):
        print "COMPUTER WINS!!!",computer,"WINS!!"
    else:
        print "TIE!!!"

def main():
    win = "no"
    turn = "X"
    display_instruct()
    difficulty = ask_number()
    board = new_board()
    human = pieces()
    computer = next_turn(human)
        
    while((win == "no")and(len(legal_moves(board))!=0)):
        display_board(board)
        if(turn == human):
            human_move(board,human)
        elif(turn == computer):
            computer_move(board,computer,human,difficulty)
        win = winner(board, computer, human)
        
        turn = next_turn(turn)

    display_board(board)
    print "Game Over"
    congrat_winner(win, computer, human)
    return 0        
        

main()
raw_input("\n\nPress the enter key to quit")
    
