
import chess
import random
board=chess.Board()
i=1
while True:
    
    print(board)
    print(board.legal_moves)
    if(board.is_checkmate()==True):
        print("Checkmate!")
        break
    if(board.is_insufficient_material()  == True):
        print("Draw!") 
        break
    """if(i%2== 0):
        colour="Black"
        i=i+1
        move=random.choice(list(board.legal_moves))
        print(move)
    else:
        colour="White"
        move_in = input(colour+", make a move: ")
        i=i+1
    """
    move=random.choice(list(board.legal_moves))
    print(move)
    
    try:
        #move=board.parse_san(move_in)
        board.push(move)

    except ValueError:
        print("Your move is illegal")
        i=i-1
        
    
    
    
    