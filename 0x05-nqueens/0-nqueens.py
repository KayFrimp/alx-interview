#!/usr/bin/python3
import sys


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


def solve_nq(board, col):
    """Checks if the queen can be placed in any row in the column col
    return: boolean"""
    # Base case: If all queens are placed
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_nq(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col]
            board[i][col] = 0

    # If the queen can not be placed in any row in this column col
    # then return false
    return False


def solve_n_queens(n):
    """Initialize the chess board, Solves the N Queen
    problem using backtracking and prints all possible
    solutions."""
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nq(board,  0):
        return "Solution does not exist"

    for row in board:
        print(row)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit()\
            or int(sys.argv[1]) < 4:
        print("Usage: nqueens N")
        sys.exit(1)

    N = int(sys.argv[1])
    result = solve_n_queens(N)
    if type(result) is str:
        print(result)
