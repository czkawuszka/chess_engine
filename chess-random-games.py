
import chess
import random
draw_counter=0
white_counter=0
black_counter=0
i=0
while(i<999):
    board=chess.Board()
    while (True):
        
        if(board.is_checkmate()==True):
            print(board)
            print("")
            if(board.outcome().winner==True):
                white_counter=white_counter+1
            else:
                black_counter=black_counter+1
            break
        if(board.is_insufficient_material() == True or board.is_stalemate()==True):
            draw_counter=draw_counter+1 
            break
        move=random.choice(list(board.legal_moves))
        
        try:
            board.push(move)

        except ValueError:
            print("Move is illegal")
        
    i=i+1
print("White won "+str(white_counter)+" times.")
print("Black won "+str(black_counter)+" times.")
print("It was a draw "+str(draw_counter)+" times.")

    
    
    
    