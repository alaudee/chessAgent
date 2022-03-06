from funcoes import *
import random

Heuristic = bool(random.getrandbits(1))
count = 0
board = chess.Board()
print("Bem vindo ao Xadrez!")
playerColor = bool(int(input("Escolha a cor: Branco(1) ou preto(0)? ")))
print(board)
while not gameOver(board):
    if board.turn == playerColor:
        print(board.legal_moves)
        move = input("Coloque sua jogada: ")
        verifyPlayerMove(move,board)
        print(board)
    else:
        if Heuristic:
            italianGame(board,count)
            count += 1
            Heuristic = False if count > 2 else True
        else:
            print("Jogada da IA:")
            move = minimaxRoot(4,board,True)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        clearConsole()
        print(board)
print("Xeque mate")