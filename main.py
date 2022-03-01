from funcoes import *

# board = chess.Board()
# legalMoves = board.legal_moves

# #MAIN 
# print("Bem Vindo ao Xadrez!")
# print(board)

# while not board.is_checkmate():
#     if board.turn:
#         print(list(legalMoves))
#         move = chess.Move.from_uci(input("Faça sua jogada: "))
#         if move in board.legal_moves:
#             board.push(move)
#         else:
#             print("Jogada não valida, tente outra")
#     else:
#         # randomChoice(board,legalMoves)
        
        
#     #clearConsole()
#     print(board)

board = chess.Board()
print(board)
while not board.is_checkmate():
    if board.turn:
        print(list(board.legal_moves))
        move = input("Coloque sua jogada: ")
        move = chess.Move.from_uci(str(move))
        board.push(move)
    else:
        print("Jogada da IA:")
        move = minimaxRoot(4,board,True)
        move = chess.Move.from_uci(str(move))
        board.push(move)
    #clearConsole()
    print(board)