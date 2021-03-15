import tictactoe as ttt
EMPTY = None
X = "X"
O = "O"
def test_terminal():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    game_over = ttt.terminal(board)
    assert(game_over == False)

    board = [[O, X, X],
            [O, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    game_over = ttt.terminal(board)
    assert(game_over == False)

    board = [[X, X, X],
            [O, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    game_over = ttt.terminal(board)
    assert(game_over == True)

    board = [[O, X, X],
            [O, EMPTY, EMPTY],
            [O, EMPTY, EMPTY]]
    game_over = ttt.terminal(board)
    assert(game_over == True)

    board = [[O, X, O],
             [X, O, X],
             [X, O, X]]
    game_over = ttt.terminal(board)
    assert(game_over == True)

def test_player():
    board = [[O, X, O],
             [X, O, X],
             [X, O, EMPTY]]
    player = ttt.player(board)
    assert(player == X)

    board = [[O, X, O],
             [X, O, X],
             [X, EMPTY, EMPTY]]
    player = ttt.player(board)
    assert(player == O)

    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    player = ttt.player(board)
    assert(player == X)

    board = [[X, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    player = ttt.player(board)
    assert(player == O)

def test_Winner():
    board = [[X, X, X],
            [O, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    winner = ttt.winner(board)
    assert(winner == X)

    board = [[O, X, X],
            [O, EMPTY, EMPTY],
            [O, EMPTY, EMPTY]]
    winner = ttt.winner(board)
    assert(winner == O)

    board = [[O, X, O],
             [X, O, X],
             [X, O, X]]
    winner = ttt.winner(board)
    assert(winner == None)

    board = [[X, X, EMPTY],
             [O, X, O],
             [O, O, X]]
    winner = ttt.winner(board)
    assert(winner == X)

    board = [[X, X, O],
             [EMPTY, O, EMPTY],
             [O, EMPTY, X]]
    winner = ttt.winner(board)
    assert(winner == O)

def test_actions():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    actions = ttt.actions(board)
    print(actions)

    board = [[X, X, O],
             [X, O, EMPTY],
             [O, EMPTY, EMPTY]]
    actions = ttt.actions(board)
    print(actions)

    board = [[EMPTY, X, O],
             [X, X, O],
             [O, O, X]]
    actions = ttt.actions(board)
    print(actions)

    board = [[X, O, X],
             [O, X, O],
             [X, EMPTY, EMPTY]]
    actions = ttt.actions(board)
    print(actions)

def test_result():
    board = [[EMPTY, X, O],
             [X, X, O],
             [O, O, X]]
    action = (0, 0)
    newBoard = ttt.result(board, action)
    print(newBoard)

    board = [[X, X, O],
             [X, O, EMPTY],
             [O, EMPTY, EMPTY]]
    action = (2, 2)
    newBoard = ttt.result(board, action)
    print(newBoard)

    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    action = (1, 1)
    newBoard = ttt.result(board, action)
    print(newBoard)

    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, X, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    action = (2, 1)
    newBoard = ttt.result(board, action)
    print(newBoard)

def main():
    print('test Terminal function: ')
    test_terminal()
    print('Terminal works :D')

    print('test player function: ')
    test_player()
    print('Player works :D')

    print('test Winner function: ')
    test_Winner()
    print('Winner works :D')

    print('test actions function: ')
    test_actions()
    print('actions works :D')

    print('test result function: ')
    test_result()
    print('result works :D')

main()