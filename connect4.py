import numpy as np
import random
import pygame
import sys
import math

def show_menu():
    pygame.init()
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("Connect 4 - Menu")
    font = pygame.font.SysFont("monospace", 50)
    menu_text = font.render("Select Mode", True, (255, 255, 255))
    two_player_text = font.render("1. Two Player", True, (255, 255, 255))
    three_player_text = font.render("2. Three Player", True, (255, 255, 255))
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit(menu_text, (180, 100))
        screen.blit(two_player_text, (150, 200))
        screen.blit(three_player_text, (150, 300))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return (1,1)  # Two player mode (1 human, 1 AI)
                if event.key == pygame.K_2:
                    return show_three_player_menu()

def show_three_player_menu():
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("Three Player Configuration")
    font = pygame.font.SysFont("monospace", 40)
    prompt_text = font.render("Select Players", True, (255, 255, 255))
    option1_text = font.render("1. 1 Human, 2 AI", True, (255, 255, 255))
    option2_text = font.render("2. 2 Humans, 1 AI", True, (255, 255, 255))
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit(prompt_text, (200, 100))
        screen.blit(option1_text, (150, 200))
        screen.blit(option2_text, (150, 300))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return (1, 2)  # 1 Human, 2 AI
                if event.key == pygame.K_2:
                    return (2, 1)  # 2 Humans, 1 AI

num_players = show_menu()
if num_players ==(1,1):
    # Two player mode (1 human, 1 AI)
    # Initialize game with 1 human player and 1 AI player
    human=num_players[0]
    ai=num_players[1]
    num_players=2
else:
    # Three player mode (1 human, 2 AI)
    human=num_players[0]
    ai=num_players[1]
    num_players=3
    
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER1 = 0
PLAYER2 = 1
AI = 2

EMPTY = 0
PLAYER1_PIECE = 1
PLAYER2_PIECE = 2
AI_PIECE = 3

WINDOW_LENGTH = 4

def is_board_full(board):
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            return False
    return True

def create_board():
    return np.zeros((ROW_COUNT,COLUMN_COUNT))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER1_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 20
    
    return score

def score_position(board, piece):
    score = 0
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    score += center_array.count(piece) * 6

    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)
    
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROW_COUNT-3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    return score

def minimax(board, depth, alpha, beta, maximizingPlayer, piece):
    valid_locations = get_valid_locations(board)
    is_terminal = any(winning_move(board, p) for p in [PLAYER1_PIECE, PLAYER2_PIECE, AI_PIECE]) or len(valid_locations) == 0
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER1_PIECE) or winning_move(board, PLAYER2_PIECE):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, piece))
    
    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, piece)
            new_score = minimax(b_copy, depth-1, alpha, beta, False, piece)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE if piece != AI_PIECE else PLAYER1_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, True, piece)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value

def get_valid_locations(board):
    return [col for col in range(COLUMN_COUNT) if is_valid_location(board, col)]

def player_turn_pause():
    time.sleep(2)  # Pause for 1 second between turns
# Rest of the game logic remains unchanged
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            color = BLACK
            if board[r][c] == PLAYER1_PIECE:
                color = RED
            elif board[r][c] == PLAYER2_PIECE:
                color = YELLOW
            elif board[r][c] == AI_PIECE:
                color = GREEN
            pygame.draw.circle(screen, color, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

board = create_board()
print_board(board)
game_over = False
pygame.init()

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 75)
turn = random.randint(PLAYER1, AI if num_players == 3 else PLAYER2)

def is_board_full(board):
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            return False
    return True

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and turn == PLAYER1:
            col = event.pos[0] // SQUARESIZE
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER1_PIECE)
                if winning_move(board, PLAYER1_PIECE):
                    label = myfont.render("Player 1 wins!", 1, RED)
                    screen.blit(label, (40,10))
                    game_over = True
                turn = (turn + 1) % num_players
                draw_board(board)
    
    if turn in [PLAYER2, AI] and not game_over:
        if num_players == 2:
            col, minimax_score = minimax(board, 5, -math.inf, math.inf, True, AI_PIECE)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)
                if winning_move(board, AI_PIECE):
                    label = myfont.render("Player 2 wins!!", 1, GREEN)
                    screen.blit(label, (40,10))
                    game_over = True
                print_board(board)
                draw_board(board)
            turn = (turn + 1) % num_players
        else:
            if human == 2 and turn == PLAYER2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        col = event.pos[0] // SQUARESIZE
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, PLAYER2_PIECE)
                            if winning_move(board, PLAYER2_PIECE):
                                label = myfont.render("Player 2 wins!", 1, YELLOW)
                                screen.blit(label, (40,10))
                                game_over = True
                            turn = (turn + 1) % num_players
                            draw_board(board)
            else:
                col, minimax_score = minimax(board, 5, -math.inf, math.inf, True, PLAYER2_PIECE if turn == PLAYER2 else AI_PIECE)
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER2_PIECE if turn == PLAYER2 else AI_PIECE)
                    if winning_move(board, PLAYER2_PIECE if turn == PLAYER2 else AI_PIECE):
                        label = myfont.render(f"Player {turn+1} wins!", 1, YELLOW if turn == PLAYER2 else GREEN)
                        screen.blit(label, (40,10))
                        game_over = True
                turn = (turn + 1) % num_players
                draw_board(board)

    if is_board_full(board) and not game_over:
        label = myfont.render("Game Over! No more moves!", 1, RED)
        screen.blit(label, (40,10))
        game_over = True
    
    if game_over:
        pygame.time.wait(5000)
