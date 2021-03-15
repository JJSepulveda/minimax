"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


'''
SUPPORT FUNCTIONS
'''
def check_matchs(board, target):
    """
    Returns true if there are a match of 3. False otherwise
    """
    # check all rows
    for row in board:
        if row[0] == row[1] == row[2] == target:
            return True
    
    # check all colums
    for colum in range(3):
        if board[0][colum] == board[1][colum] == board[2][colum] == target:
            return True
    
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == target:
        return True

    if board[0][2] == board[1][1] == board[2][0] == target:
        return True

    return False

def board_is_full(board):
    """
    Returns true if there aren't empty elemets
    """
    for row in board:
        for element in row:
            if element is EMPTY:
                return False

    return True

def minValue(board):
    if terminal(board):
        return utility(board), None
    v = 2
    chose = None
    for action in actions(board):
        newBoard = result(board, action)
        value, _ = maxValue(newBoard)
        if value < v:
            chose = action
            v = value
    return v, chose

def maxValue(board):
    """
    Return a tuple of action and utility
    """
    if terminal(board):
        return utility(board), None
    v = -2
    chose = None
    for action in actions(board):
        newBoard = result(board, action)
        value, _ = minValue(newBoard)
        if value > v:
            chose = action
            v = value
    return v, chose

'''
MAIN FUNCTIONS
'''
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0
    # count all x's and o's and if the amount of x is
    # equal to amout of o means that is the x turns
    for row in board:
        for element in row:
            if element == X:
                x_counter += 1
            if element == O:
                o_counter += 1

    if x_counter == o_counter:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for r, row in enumerate(board):
        for c, element in enumerate(row):
            if element is EMPTY:
                actions.append((r, c))

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # invalid action
    if board[action[0]][action[1]] is not EMPTY:
        print(action)
        print(board)
        raise Exception

    # get the player turn
    turn = player(board)
    #copy the board to avoid to change the original board
    #board is a list of list so, board.copy() doesn't works
    #because only works for the first dimension.
    newBoard = [value[:] for value in board]
    newBoard[action[0]][action[1]] = turn

    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_matchs(board, X):
        return X
    elif check_matchs(board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if check_matchs(board, X): 
        return True

    if check_matchs(board, O):
        return True

    if board_is_full(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if check_matchs(board, X):
        return 1
    elif check_matchs(board, O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    # if the ia is X needs to maximize, otherwise
    # needs to minimize
    if turn == X:
        _, action = maxValue(board)
    else:
        _, action = minValue(board)

    return action
