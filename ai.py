#ai.py
import copy

def minimax(position, depth, max_player, game, alpha=float('-inf'), beta=float('inf')):
    winner = game.winner()
    if depth == 0 or winner is not None:
        return evaluate(position), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, 'white', game):
            eval, _ = minimax(move, depth - 1, False, game, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, 'black', game):
            eval, _ = minimax(move, depth - 1, True, game, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def evaluate(board):
    white_score = 0
    black_score = 0
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == 'white':
                    white_score += 2 if piece.king else 1
                else:
                    black_score += 2 if piece.king else 1
    return white_score - black_score

def get_all_moves(board, color, game):
    moves = []
    for row in board.board:
        for piece in row:
            if piece != 0 and piece.color == color:
                valid_moves = game.get_valid_moves(piece)
                for move, skipped in valid_moves.items():
                    new_board = copy.deepcopy(board)
                    new_piece = new_board.get_piece(piece.row, piece.col)
                    new_board.move(new_piece, move[0], move[1])
                    moves.append(new_board)
    return moves
