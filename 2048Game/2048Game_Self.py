"""
2048 Game
2048 is a game and you are expected to implement the move function for this game.
Arguments passed to the four functions is the matrix which we are using for 2048
The move function will be returning new matrix after moving the corresponding move.
Implement All The Four Moves Using These Functions -
1. move_up
2. move_down
3. move_left
4. move_right
"""

import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    return mat


def add_random_2(mat):
    row = random.randint(0, 3)
    col = random.randint(0, 3)

    while (mat[row][col]) != 0:
        row = random.randint(0, 3)
        col = random.randint(0, 3)

    mat[row][col] = 2
    return mat  # this return statement was missed initially


def get_current_state(mat):
    #anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WON"
    # anywhere 0 is present
    for i in range(4): # not working solution had range set to 3;
        for j in range(4):
            if mat[i][j] == 0:
                return "GAME NOT OVER"
    # EVERY ROW AND COLUMN EXCEPT LAST ROW AND LAST COLUMN
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return "GAME NOT OVER"
    # Last ROW
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return "GAME NOT OVER"
    # Last COL
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return "GAME NOT OVER"

    return "LOST"


def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1

    return new_mat, changed


def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True

    return mat, changed


def reverse(mat):
    new_mat = []

    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4 - j - 1])

    return new_mat


def transpose(mat):
    new_mat = []

    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])

    return new_mat


def move_up(grid):
    # Implement This Function
    # ------- Issue with value storage of value grid
    # firstTransposed = transpose(grid)
    # compress(firstTransposed)
    # merge(firstTransposed)
    # compress(firstTransposed)
    # secondTransposed = transpose(firstTransposed)

    firstTransposed = transpose(grid)
    new_grid, changed1 = compress(firstTransposed)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    secondTransposed = transpose(grid)

    return secondTransposed, changed


def move_down(grid):
    # Implement This Function
    firstTransposed = transpose(grid)
    firstReversed = reverse(firstTransposed)
    new_grid, changed1 = compress(firstReversed)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    secondReversed = reverse(new_grid)
    secondTransposed = transpose(secondReversed)
    return secondTransposed, changed


def move_right(grid):
    firstReversed = reverse(grid)
    new_grid, changed1 = compress(firstReversed)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    secondReversed = reverse(new_grid)
    return secondReversed, changed


def move_left(grid):
    # Implement This Function
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)

    return new_grid, changed


mat = start_game()
mat[1][3] = 2
mat[2][2] = 2
mat[3][0] = 4
mat[3][1] = 8
mat[2][1] = 4
inputs = [int(ele) for ele in input().split()]
for ele in inputs:
    if ele == 1:
        mat = move_up(mat)
    elif ele == 2:
        mat = move_down(mat)
    elif ele == 3:
        mat = move_left(mat)
    else:
        mat = move_right(mat)
    print(mat)