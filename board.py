#board.py
import pygame
from piece import Piece
from utils import DARK_SQUARE, LIGHT_SQUARE, ROWS, COLS, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 != 0:
                    if row < 4:
                        self.board[row][col] = Piece(row, col, 'white')
                    elif row > 5:
                        self.board[row][col] = Piece(row, col, 'black')
                    else:
                        self.board[row][col] = 0
                else:
                    self.board[row][col] = 0

    def draw(self, win):
        win.fill(LIGHT_SQUARE)
        for row in range(ROWS):
            for col in range(COLS):
                color = DARK_SQUARE if (row + col) % 2 else LIGHT_SQUARE
                pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        for row in self.board:
            for piece in row:
                if piece != 0 and piece is not None:
                    piece.draw(win)

    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = 0, piece
        piece.move(row, col)
    
    
        if (piece.color == 'black' and row == 0) or (piece.color == 'white' and row == ROWS - 1):
            if not piece.king:
                piece.make_king()
                return True
        return False

    def remove(self, pieces):
        if pieces:
            for piece in pieces:
                self.board[piece.row][piece.col] = 0

    def get_valid_moves(self, piece):
        moves = {}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        if not piece.king:
            if piece.color == 'black':
                directions = [(-1, 0), (-1, -1), (-1, 1)]
            else:
                directions = [(1, 0), (1, -1), (1, 1)]

        for drow, dcol in directions:
            row = piece.row + drow
            col = piece.col + dcol

            if 0 <= row < ROWS and 0 <= col < COLS:
                target = self.get_piece(row, col)
                if target == 0:
                    moves[(row, col)] = []
                elif target is not None and target.color != piece.color:
                    jump_row = row + drow
                    jump_col = col + dcol
                    if 0 <= jump_row < ROWS and 0 <= jump_col < COLS and self.get_piece(jump_row, jump_col) == 0:
                        moves[(jump_row, jump_col)] = [target]

        return moves

    def evaluate(self):
        score = 0
        for row in self.board:
            for piece in row:
                if piece != 0 and piece is not None:
                    piece_score = 1
                    if piece.king:
                        piece_score += 2

                    if piece.color == 'black':
                        score += piece_score
                        score += 0.1 * piece.row
                    else:
                        score -= piece_score
                        score -= 0.1 * piece.row
        return score

    def ai_move(self):
        best_move = None
        best_score = float('-inf')

        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if piece != 0 and piece is not None and piece.color == 'black':
                    valid_moves = self.get_valid_moves(piece)
                    for move, skipped in valid_moves.items():
                        temp_board = self.copy_board()
                        temp_piece = temp_board.get_piece(piece.row, piece.col)
                        temp_board.move(temp_piece, move[0], move[1])
                        score = temp_board.evaluate()

                        if score > best_score:
                            best_score = score
                            best_move = (piece, move)

        if best_move:
            self.move(best_move[0], best_move[1][0], best_move[1][1])

    def copy_board(self):
        new_board = Board()
        new_board.board = [row[:] for row in self.board]
        return new_board

    def winner(self):
        white_left = sum(piece is not None and piece != 0 and piece.color == 'white' for row in self.board for piece in row)
        black_left = sum(piece is not None and piece != 0 and piece.color == 'black' for row in self.board for piece in row)

        if white_left == 0:
            return 'Black'
        elif black_left == 0:
            return 'White'
        return None
