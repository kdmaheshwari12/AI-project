#game.py
import pygame
from board import Board
from utils import SQUARE_SIZE, BLUE

pygame.init()
pygame.mixer.init()

move_sound = pygame.mixer.Sound('sounds/move.wav')
capture_sound = pygame.mixer.Sound('sounds/capture.wav')
king_sound = pygame.mixer.Sound('sounds/king.wav')
win_sound = pygame.mixer.Sound('sounds/win.wav')


class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = 'black'
        self.valid_moves = {}

    def ai_move(self, board):
        self.board = board
        self.change_turn()

    def get_board(self):
        return self.board

    @property
    def square_size(self):
        return SQUARE_SIZE

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def select(self, row, col):
        piece = self.board.get_piece(row, col)

        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        elif piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)

    def _move(self, row, col):
        if self.selected and (row, col) in self.valid_moves:
            old_king_status = self.selected.king
            promoted = self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]

            # Play appropriate sounds
            if skipped:
                capture_sound.play()
                self.board.remove(skipped)
            elif promoted:
                king_sound.play()
            else:
                move_sound.play()

            self.change_turn()
            self.valid_moves = {}
            return True
        return False

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.selected = None
        self.valid_moves = {}
        self.turn = 'white' if self.turn == 'black' else 'black'

    def draw(self, win):
        for row in self.board.board:
            for piece in row:
                if piece is not None:
                    piece.draw(win)

    def winner(self):
        black_pieces = 0
        white_pieces = 0
        for row in self.board.board:
            for piece in row:
                if piece is not None and piece != 0:
                    if piece.color == 'black':
                        black_pieces += 1
                    elif piece.color == 'white':
                        white_pieces += 1

        if black_pieces == 0:
            return 'White'
        elif white_pieces == 0:
            return 'Black'
        return None

    def check_winner(self):
        black_pieces = white_pieces = 0
        for row in self.board.board:
            for piece in row:
                if piece != 0:
                    if piece.color == 'black':
                        black_pieces += 1
                    else:
                        white_pieces += 1
        if black_pieces == 0:
            return 'White'
        elif white_pieces == 0:
            return 'Black'
        return None
