from funcoes import *

board = chess.Board()
playerColor = bool(int(input("Escolha a cor: Branco(1) ou preto(0)? ")))
print(playerColor)

print(board)
while not board.is_checkmate() or not board.is_stalemate() or not board.is_insufficient_material():
    if board.turn == playerColor:
        print(list(board.legal_moves))
        move = chess.Move.from_uci(input("Coloque sua jogada: "))
        board.push(move)
    else:
        print("Jogada da IA:")
        move = minimaxRoot(4,board,True)
        move = chess.Move.from_uci(str(move))
        board.push(move)
    clearConsole()
    print(board)
print("CABO O JOGO")