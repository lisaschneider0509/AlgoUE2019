#!/usr/bin/env python
import re
import sys


# functions
def find_separator(inputString, separator):
    sep_position = [i for i, item in enumerate(inputString) if re.search(separator, item)]
    return sep_position


def save_matrix(start, end, string_list):
    matrix = []
    while start <= end:
        matrix.append(string_list[start])
        start += 1
    return matrix


def format_matrix(string_list):
    matrix = []
    i = 0
    while i < len(string_list):
        buffer = string_list[i].strip("\n").split(" ")
        while '' in buffer:
            buffer.remove('')
        buffer = [float(x) for x in buffer]
        matrix.append(buffer)
        i += 1
    return matrix


def manhattanTouristProblem(weights_down, weights_right, weights_dia, n, m):
    s_dict = {(0, 0): 0}

    for i in range(1, n):
        s_next = weights_down[i-1][0]
        next_key = (i, 0)
        s_dict.update({next_key: s_next})

    for j in range(1, m):
        s_next = weights_right[0][j-1]
        next_key = (0, j)
        s_dict.update({next_key: s_next})

    for i in range(1, n):
        for j in range(1, m):
                next_key = (i, j)

                s_down = s_dict[(i - 1, j)] + weights_down[i - 1][j]
                s_right = s_dict[(i, j - 1)] + weights_right[i][j - 1]
                s_dia = s_dict[(i-1, j-1)] + weights_dia[i-1][j-1]

                s_max = max([s_down, s_right, s_dia])
                s_dict.update({next_key: s_max})

    print(s_dict[((n-1), (m-1))])


# read from stdin
if sys.stdin.isatty():  # to avoid getting stuck if no stdin is provided
    print("Running test data: Result = 20.68")

    matrix_down = [[0.60, 0.65, 0.91, 0.94, 0.14],
                   [0.85, 0.27, 0.70, 0.31, 0.63],
                   [0.63, 0.23, 0.35, 0.77, 0.20],
                   [0.37, 0.76, 0.41, 0.30, 0.67]]

    matrix_right = [[0.76, 0.41, 0.72, 0.13],
                    [0.57, 0.64, 0.62, 0.62],
                    [0.37, 0.98, 0.36, 0.24],
                    [0.99, 0.77, 0.39, 0.35],
                    [0.37, 0.34, 0.62, 0.82]]

    matrix_dia = [[6.74, 07.03, 02.47, 06.25],
                  [4.48, 03.75, 02.98, 03.62],
                  [7.90, 03.63, 03.67, 03.18],
                  [9.30, 08.40, 09.02, 02.58]]

    matrix_dimension = [len(matrix_down[0]), len(matrix_right)]

else:
    inputString = sys.stdin.readlines()
    start_positions = find_separator(inputString, 'G.*')
    end_positions = find_separator(inputString, '---.*')

    start_down = start_positions[0] + 1
    start_right = start_positions[1] + 1
    end_down = end_positions[0] - 1
    end_right = end_positions[1] - 1
    start_dia = start_positions[2] + 1
    end_dia = end_positions[2] - 1

    matrix_down = save_matrix(start_down, end_down, inputString)
    matrix_right = save_matrix(start_right, end_right, inputString)
    matrix_dia = save_matrix(start_dia, end_dia, inputString)

    matrix_down = format_matrix(matrix_down)
    matrix_right = format_matrix(matrix_right)
    matrix_dia = format_matrix(matrix_dia)

    matrix_dimension = [len(matrix_down[0]), len(matrix_right)]

# run mtp
manhattanTouristProblem(matrix_down, matrix_right, matrix_dia, matrix_dimension[0], matrix_dimension[1])
