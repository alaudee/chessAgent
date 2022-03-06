import chess
import os

pawnTablew = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

pawnTableb = pawnTablew[::-1]

knightsTablew = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]

knightsTableb = knightsTablew[::-1]

bishopsTablew = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]

bishopsTableb = bishopsTablew[::-1]

rooksTablew = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]

rooksTableb = rooksTablew[::-1]

queensTablew = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]

queensTableb = queensTablew[::-1]

kingsTablew = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]

kingsTableb = kingsTablew[::-1]

italianGamew = ("e4","Nf3","Bc4")
italianGameb = ("e5","Nc6","Bb4")

def italianGame(board,count):
    if board.turn == True:
        board.push_san(italianGamew[count])
    else:
        board.push_san(italianGameb[count])

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def minimaxRoot(depth,board,isMaximizing):
    legalMoves = board.legal_moves
    bestMove = -9999
    finalMove = None
    for x in legalMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        value = max(bestMove, minimax(depth - 1, board,-10000,10000, not isMaximizing))
        board.pop()
        if value > bestMove:
            bestMove = value
            finalMove = move
    return finalMove

def minimax(depth, board, alpha, beta, maximizing):
    if(depth == 0):
        return -evaluateBoard(board)
    legalMoves = board.legal_moves
    if(maximizing):
        bestMove = -9999
        for x in legalMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            bestMove = max(bestMove,minimax(depth - 1, board,alpha,beta, not maximizing))
            board.pop()
            alpha = max(alpha,bestMove)
            if beta <= alpha:
                return bestMove
        return bestMove
    else:
        bestMove = 9999
        for x in legalMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            bestMove = min(bestMove, minimax(depth - 1, board,alpha,beta, not maximizing))
            board.pop()
            beta = min(beta,bestMove)
            if beta <= alpha:
                return bestMove
        return bestMove

def evaluateBoard(board):
    i = 0
    evaluation = 0
    x = board.turn
    while i < 63:
        i += 1
        evaluation = evaluation + (getPieceValue(str(board.piece_at(i)),i) if x else -getPieceValue(str(board.piece_at(i)),i))
    return evaluation


def getPieceValue(piece,i):
    if(piece == None):
        return 0
    value = 0
    if piece == "P" or piece == "p":
        value = 10 + ((pawnTablew[i]) if piece == "P" else (pawnTableb[i]))
    if piece == "N" or piece == "n":
        value = 30 + ((knightsTablew[i]) if piece == "N" else (knightsTableb[i]))
    if piece == "B" or piece == "b":
        value = 30 + ((bishopsTablew[i]) if piece == "B" else (bishopsTableb[i]))
    if piece == "R" or piece == "r":
        value = 50 + ((rooksTablew[i]) if piece == "R" else (rooksTableb[i]))
    if piece == "Q" or piece == "q":
        value = 90 + ((queensTablew[i]) if piece == "Q" else (queensTableb[i]))
    if piece == 'K' or piece == 'k':
        value = 900 + ((kingsTablew[i]) if piece == "K" else (kingsTableb[i]))
    return value

def verifyPlayerMove(move,board):
    try:
        board.push_san(move)
    except:
        print("Jogada inválida, tente novamente")

def gameOver(board):
    if board.is_checkmate() or board.is_stalemate() or board.is_insufficient_material():
        if(len(list(board.legal_moves)) == 0):
            return True
    else:
        return False
