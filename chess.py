
import chess
board=chess.Board()
i=1
while True:
    
    print(board)
    if(chess.Color== False):
        colour="Black"
    else:
        colour="White"
        if(i==1):
            print("All moves in san (ex. Nc3)!")
    
    
    
    move_in = input(colour+", make a move: ")
    try:
        move=board.parse_san(move_in)
        leg_check = move in board.legal_moves
        board.push(move)

    except ValueError:
        print("Your move is illegal")
        
    
    
    
    