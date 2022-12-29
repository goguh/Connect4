# All imports are imports from python
import numpy as np
import pygame
import sys
import math 

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7
# this a global variable to show the static variable that dont change 
# a non-changeable variable


# we are defineing a function as create_board
def create_board():
    # when ceating the variable board to np.zeros
    # which fills up the board with zeros to a certain length given in ()
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    #(6,7), which is 6 up on the y-axis & 7 across on the x-axis
    return board
    #which we return board and create a variable to print out our function
    # you cant have create_board() because it will run but not print anything

def drop_piece(board, row, col, piece):
    board[row][col] = piece
    # Were going to make it fill in the board with whatever piece
    # that the player just dropped
    # This is an assign not equal 

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0
    # The last row in the index -1 for ROW_COUNT
    # [col] is the column user selected
    
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
    # This r is going to count to zero to row minus one 
    
        if board[r][col] == 0:
            return r
    # if the row is equal to 0, means the slot is empty
    # so we are returning the first instance that it's empty
    
def print_board(board):
    print(np.flip(board, 0))
# This is going to change the orientation of the board

def winning_move():
    # Checking the horizontal locations for the win
    for c in range(COLUMN_COUNT-3): 
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return true
    # we are subtracting three from the sides
    # because having it wouldnt work for a win 
    
    # checking the vertical locations for the win
    for c in range(COLUMN_COUNT): 
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return true
    # we are subtracting three from the top 
    # because having it wouldnt work for a win
    
    # Checking for the positive sloped diaganols
    for c in range(COLUMN_COUNT-3): 
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return true
    # since we are checking the slops now we need to subtracte three for rows and columns
    # not only that but in our loop we need to add the (+1,+2,+3). since we are doing both
    
    # Checking for the negative sloped diaganols
    for c in range(COLUMN_COUNT-3): 
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return true
    # so the reason we only have 3 in range of r (ROW_COUNT). is due to the 3rd row
    # and the reason we have (r-1,r-2,r-3). is due to going down a row

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	# So now we are caling C and R that are in range of COLUMN_COUNT and ROW_COUNT.
	# Which lets us create the reactangle and circles 
	
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                
    pygame.display.update()

    
board = create_board()
# This the variable that going to equal to our function, that allows us to 
# print this variable to the user

print_board(board)

game_over = False
# If game over is false it tells the program that you'll play the game until it 
# turn True. which someone has to connect four to the end game

turn = 0
# when turn is 0. we can start the game and decide who'll go first
# usually player 1

pygame.init()
# Initializing the pygame (always done when importing the pygame)

SQUARESIZE = 100 
# This is the squares that represent each coulumn

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
# This is the window box for the images
# In addition for the height, we are adding another row for height
# this is only for the aspect having a black row to see the inital drop 

size = (width, height)
# The combination of with and height for the window box

RADIUS = int(SQUARESIZE/2- 5)

screen = pygame.display.set_mode(size)
# The display screen

draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont('monospace', 75)

# A while loop is going to be running as long as this game variable is false 
while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Event is mostly the action your making like (mouse motion, mouse button down, 
    # key down, etc)
    # pygame.ouit is basically closing the program
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    
                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True
            
            # Player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    
                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True
                        
            print_board(board)
            draw_board(board)
            
            turn += 1
            # We would want to increase the turn by 1. 
            # so that we have the game asking for more input
            turn = turn % 2
            # making the odd even as well as taking the remainder.(% = mod)
            # by dividing it by 2. so its an alternative between zero and one
            
            if game_over:
                pygame.time.wait(3000)
