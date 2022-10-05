import chess
import random
import engine

board=chess.Board()



print(board)
i=0
while(i<999):
    
    board=chess.Board()
    move_counter=1
    while (True):
        
        if(board.is_checkmate()==True):
            if(board.outcome().winner==True):
                white_counter=white_counter+1
            else:
                black_counter=black_counter+1
            break
        if(board.is_insufficient_material() == True or board.is_stalemate()==True):
            draw_counter=draw_counter+1 
            break
        if(move_counter%2==0):
            print("black move")
            move=random.choice(list(board.legal_moves))
            
        else:
            print("white move")
            move=engine.Material_engine(board)
           

        try:
            board.push(move)

        except ValueError:
            print("Move is illegal")
    print("")
    i=i+1
print("White won "+str(white_counter)+" times.")
print("Black won "+str(black_counter)+" times.")
print("It was a draw "+str(draw_counter)+" times.")