import random
import chess

x=0
board=chess.Board()
while(x<100):
    move=random.choice(list(board.legal_moves))
    x+=1
    print(str(move)+" "+str(x))