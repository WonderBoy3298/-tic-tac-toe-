from ast import While
from operator import truediv
from pickle import TRUE



def display_board(board):
    blankBoard="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""
    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    
    print(blankBoard)
    


def player_marker():
    x=0
    while x==0:
        p1=str(input("player 1,choose your marker: X or O  "))
        p1=p1.upper()
        if(p1=='X' or p1=='O'):
            if(p1=='X'):
                p2='O'
                print("player 1 is"+" "+p1+" "+"and player 2 is"+" "+p2)
                x=1
                return p1,p2
            else:
                p2='X'
                p1='O'
                print("player 1 is"+" "+p1 +"and player 2 is"+" "+ p2)
                x=1
                return p1,p2
        else:
            x=0
            print("invalid input")
    

def free_place(board,position):
    if(board[position]=='X' or board[position]=='O'):
        return False
    else:
        return True
    

def place_marker(board,marker,position):
    i=0
    while i==0:
        if(free_place(board,position)):
            board[position]=marker
            i=1
            return board
            
        else:
            print("invalid position")
            i=0

def winner(board,mark):
    if(board[1]==board[2]==board[3]==mark):
        return True
    elif(board[4]==board[5]==board[6]==mark):
        return True
    elif(board[7]==board[8]==board[9]==mark):
        return True
    elif(board[1]==board[5]==board[9]==mark):
        return True
    elif(board[3]==board[5]==board[7]==mark):
        return True 
    else:
        return False


def full_board_check(board):
    t=False
    for i in range(1,10):
        if(board[i]=="#"):
            t=True
            
    return t
         
        

b=["x","o","x","x","x","x","x","x","x"]
#Xdisplay_board(b)


#----replay function------

def replay():
    playAgain=input("do You want to replay Y or N")
    if(playAgain.upper()=="y"):
        return True
    else:
        return False

#-------------------------main--------------------------

print("Welcome to Tic Tac Toe")

board=["#"]*10
tab=player_marker()
i=1
j=1

while True:
    j=1
    p1=int(input("player , choose  your position: "))
    
    if(i%2==0):
        marker=tab[1]
    else:
        marker=tab[0]
    
    place_marker(board,marker,p1) 
    display_board(board)
    i+=1
    if(winner(board,marker)):
        print("You Won")
        break
    if(full_board_check(board)==False):
        print("equal game")
        break
    j=2
    
