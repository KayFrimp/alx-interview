#!/usr/bin/python3
import sys


def print_board(board):
    """ print_board
    Args:
        board - list of list with length sys.argv[1]
    """
    new_list = []
    for i, row in enumerate(board):
        value = []
        for j, col in enumerate(row):
            if col == 1:
                value.append(i)
                value.append(j)
        new_list.append(value)

    print(new_list)


def is_safe(board, row, col):
    """Checks for any safe movements on board"""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board),  1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nq(board, col, col_number):
    """Checks if the queen can be placed in any row in the column col
    return: boolean"""
    if (col == col_number):
        print_board(board)
        return True
    possible = False
    for i in range(col_number):

        if (is_safe(board, i, col, col_number)):

            # Place this queen in board[i][col]
            board[i][col] = 1

            # Make result true if any placement
            # is possible
            possible = solve_nq(board, col + 1, col_number) or possible

            board[i][col] = 0  # BACKTRACK

    return possible


def solve_n_queens(n):
    """Initialize the chess board, Solves the N Queen
    problem using backtracking and prints all possible
    solutions."""
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nq(board,  0, n):
        return False

    return True


def validate(args):
    """ Validate the input data to verify if the size to
        answer is posible
    Args:
        args - sys.argv
    """
    if (len(args) == 2):
        # Validate data
        try:
            number = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    N = validate(sys.argv)
    solve_n_queens(N)
