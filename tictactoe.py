"""
Tic Tac Toe Player Game

A game in which two players alternately put Xs and Os in compartments 
of a figure formed by two vertical lines crossing two horizontal lines
and each tries to get a row of three X's or three O's before the opponent does.
Implemented using Artificial Intelligence based on Minimax algorithm.

"""


#Importing the libraries required

import math
from copy import deepcopy

X = "X"
O = "O"         
EMPTY = None


# Additional Helper Functions


def minmax_values(board, alpha, beta, player):
    
    # If the game is already over i.e., a row of three X's or
    # three O's is obtained then return utility

    if terminal(board):
        return utility(board)

    
    # It X's turn try to maximize the value

    if player == X:
        value = -math.inf

        for action in actions(board):
            value = max(value, minmax_values(result(board, action),alpha, beta, O))

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value


    # If O's turn try to minimize the value

    else:
        value = math.inf

        for action in actions(board):
            value = min(value, minmax_values(result(board, action), alpha, beta, X))

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value



# Tic Tac Toe Functions



def initial_state():
    """
    Returns starting state of the board.
    That is, every slot is empty at start.

    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    Based on the which player has played his/her turn previously.

    """
    
    # For counting total occupied positions

    count = 0
    
    # Assuming that X starts first
    
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count=count+1
    
    if count%2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) that are available 
    on the board for the player to place his/her marker on.

    """
    
    # Store all possible actions as a list of tuples

    possible_actions = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i,j))
                
    return possible_actions


def result(board, action):
    
    """
    Returns the board that results from making move (i, j) on the board.

    """
    
    # Unpacking the tuple

    a,b = action

    # Copy the state as not to update the actual state

    new_board =  deepcopy(board)
    turn = player(board)
    
    if new_board[a][b] != EMPTY:
        raise Exception("Invalid action")
    elif turn == X:
        new_board[a][b] = "X"
    else:
        new_board[a][b] = "O"
        
    return new_board


def winner(board):
    
    """
    Returns the winner of the game, if there is one
    If a row of three X's or three O's is obtained

    """
    
    if (board[0][0] == board[0][1] == board[0][2] == "X" or
        board[1][0] == board[1][1] == board[1][2] == "X" or
        board[2][0] == board[2][1] == board[2][2] == "X" or
        board[0][0] == board[1][0] == board[2][0] == "X" or
        board[0][1] == board[1][1] == board[2][1] == "X" or
        board[0][2] == board[1][2] == board[2][2] == "X" or
        board[0][0] == board[1][1] == board[2][2] == "X" or
        board[0][2] == board[1][1] == board[2][0] == "X"):
            
            return X
        
    elif (board[0][0] == board[0][1] == board[0][2] == "O" or
        board[1][0] == board[1][1] == board[1][2] == "O" or
        board[2][0] == board[2][1] == board[2][2] == "O" or
        board[0][0] == board[1][0] == board[2][0] == "O" or
        board[0][1] == board[1][1] == board[2][1] == "O" or
        board[0][2] == board[1][2] == board[2][2] == "O" or
        board[0][0] == board[1][1] == board[2][2] == "O" or
        board[0][2] == board[1][1] == board[2][0] == "O"):
            
            return O
        
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    """
    
    if winner(board) == 'X' or winner(board) == 'O':
        return True
    
    elif not actions(board):
        return True
    
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    """
    
    if winner(board) == 'X':
        return 1
    
    elif winner(board) == 'O':
        return -1
    
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    """
    
    # If the game is over return None

    if terminal(board):     
        return None

    move = None

    alpha = -math.inf
    beta = math.inf

    if player(board) == X:              # If its X turn
        value = -math.inf

        for action in actions(board):
            updated_value = minmax_values(result(board, action),alpha, beta, O)

            alpha = max(value, updated_value)

            if updated_value > value:
                
                value = updated_value
                move = action

    else:                               # If its O turn
        value = math.inf

        for action in actions(board):
            updated_value = minmax_values(result(board, action),alpha, beta, X)

            beta = min(value, updated_value)

            if updated_value < value:
                
                value = updated_value
                move = action

    return move
