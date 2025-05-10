import copy
import pygame

def minimax(position, depth, max_player, game, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, 'white', game):
            evaluation, _ = minimax(move, depth - 1, False, game, alpha, beta)
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, 'black', game):
            evaluation, _ = minimax(move, depth - 1, True, game, alpha, beta)
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def get_all_moves(board, color, game):
    capture_moves = []
    normal_moves = []

    for row in board.board:
        for piece in row:
            if piece and piece.color == color:
                valid_moves = board.get_valid_moves(piece)
                for move, skip in valid_moves.items():
                    temp_board = copy.deepcopy(board)
                    temp_piece = temp_board.get_piece(piece.row, piece.col)
                    new_board = simulate_move(temp_piece, move, temp_board, game, skip)
                    
                    if skip:  # It's a capturing move
                        capture_moves.append(new_board)
                    else:
                        normal_moves.append(new_board)

    # Prioritize capturing moves
    return capture_moves if capture_moves else normal_moves
