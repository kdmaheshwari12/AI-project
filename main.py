#main.py
import pygame
from game import Game
from minimax import minimax
import copy

# Load sounds once
move_sound = pygame.mixer.Sound('sounds/move.wav')
capture_sound = pygame.mixer.Sound('sounds/capture.wav')
king_sound = pygame.mixer.Sound('sounds/king.wav')
win_sound = pygame.mixer.Sound('sounds/win.wav')

pygame.init()
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hybrid Checkers AI Game')
FPS = 60

def detect_capture(old_board, new_board):
    old_pieces = sum(piece is not None for row in old_board.board for piece in row)
    new_pieces = sum(piece is not None for row in new_board.board for piece in row)
    return new_pieces < old_pieces  # If less, then a capture happened

def detect_kinged_piece(old_board, new_board):
    for row in range(len(old_board.board)):
        for col in range(len(old_board.board[row])):
            old_piece = old_board.board[row][col]
            new_piece = new_board.board[row][col]
            if (new_piece and new_piece != 0 and 
                ((not old_piece or old_piece == 0) or 
                 (old_piece and not old_piece.king))) and new_piece.king:
                return True
    return False

def draw_winner(win, text):
    font = pygame.font.SysFont('arial', 50)
    win.fill((0, 0, 0))  # Clear screen
    label = font.render(f"🎉 {text} Wins! Congratulations! 🎉", True, (255, 255, 255))
    win.blit(label, (40, win.get_height() // 2 - 25))
    pygame.display.update()
    pygame.time.delay(4000)

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        # Check for winner BEFORE AI move
        if game.winner():
            win_sound.play()
            draw_winner(WIN, game.winner())
            run = False
            continue

        if game.turn == 'white':
            # AI TURN
            old_board = copy.deepcopy(game.get_board())
            value, new_board = minimax(game.get_board(), 3, True, game)

            # Detect sound type before applying move
            if detect_capture(old_board, new_board):
                capture_sound.play()
            elif detect_kinged_piece(old_board, new_board):
                king_sound.play()
            else:
                move_sound.play()

            game.ai_move(new_board)

            # Check for winner AFTER AI move
            if game.winner():
                win_sound.play()
                draw_winner(WIN, game.winner())
                run = False
                continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // game.square_size, pos[0] // game.square_size
                game.select(row, col)

                # Check for winner AFTER player move
                if game.winner():
                    win_sound.play()
                    draw_winner(WIN, game.winner())
                    run = False
                    continue

        game.update()

    pygame.quit()

if __name__ == '__main__':
    main()
