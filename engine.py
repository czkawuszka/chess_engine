from operator import ne
import chess
import random



def Count_material(board):
    i=0
    material_balance=0
    while(i<8):
        j=0
        while(j<8):
            try:
                piece = board.piece_at(chess.square(j,i))
                piece_type = piece.piece_type
                piece_color = piece.color
                piece_symbol = piece.symbol()
                
                if(piece_type==1): #whats the type of the piece?
                    piece_value=1
                elif(piece_type==2 or piece_type==3):
                    piece_value=3
                elif(piece_type==4):
                    piece_value=5
                elif(piece_type==5):
                    piece_value=9


                if(piece_color==1): #white or black
                    material_balance+=piece_value
                else:
                    material_balance-=piece_value
                    

            except:
                j=j
            j=j+1
        i=i+1
    return material_balance

def Material_engine(board):
    saved_move=None
    old_material=Count_material(board)
    for move in board.legal_moves: #player move
        board.push(move)
        new_material=Count_material(board)
        if(new_material>old_material):
                old_material=new_material
                
                saved_move=move
    if(old_material==0):
        saved_move=random.choice(list(board.legal_moves))
    return saved_move

'''def Material_engine(board):
    saved_move=None
    old_material=Count_material(board)
    for move in board.legal_moves: #player move
        board.push(move)
        mid_material=Count_material(board)
        for move in board.legal_moves: #opponent move
            board.push(move)
            new_material=Count_material(board)
            if(new_material>old_material):
                old_material=new_material
                saved_move=move
            board.pop()
        board.pop()
    if(mid_material==0 and old_material==0):
        saved_move=random.choice(list(board.legal_moves))
    return saved_move'''