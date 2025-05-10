import pygame
from utils import SQUARE_SIZE

class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        border_color = (0, 0, 0)
        fill_color = (255, 255, 255) if self.color == 'white' else (0, 0, 0)
        pygame.draw.circle(win, border_color, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, fill_color, (self.x, self.y), radius)
        if self.king:
            pygame.draw.circle(win, (255, 215, 0), (self.x, self.y), radius // 2)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
