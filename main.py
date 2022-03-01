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
n = 0
print(board)
while n < 100:
    if n%2 == 0:
        print(list(board.legal_moves))
        move = input("Coloque sua jogada: ")
        move = chess.Move.from_uci(str(move))
        board.push(move)
    else:
        print("Jogada da IA:")
        move = minimaxRoot(2,board,True)
        move = chess.Move.from_uci(str(move))
        board.push(move)
    print(board)
    n += 1