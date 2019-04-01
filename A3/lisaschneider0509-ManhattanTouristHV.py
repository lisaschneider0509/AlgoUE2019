#!/usr/bin/env python
import re
import sys


# functions
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


def manhattanTouristProblem(weights_down, weights_right, n, m):
    s_dict = {(0, 0): 0}

    for i in range(1, n):
        s_next = s_dict[(i-1, 0)] + weights_down[i-1][0]  # forgot to add the weights to the dict entries
        next_key = (i, 0)
        s_dict.update({next_key: s_next})

    for j in range(1, m):
        s_next = s_dict[(0, j-1)] + weights_right[0][j-1]  # forgot to add the weights to the dict entries
        next_key = (0, j)
        s_dict.update({next_key: s_next})


    for i in range(1, n):
        for j in range(1, m):
            next_key = (i, j)

            s_down = s_dict[(i-1, j)] + weights_down[i-1][j]
            s_right = s_dict[(i, j-1)] + weights_right[i][j-1]

            s_max = round(max([s_down, s_right]), 3)
            s_dict.update({next_key: s_max})

    print(s_dict[((n-1), (m-1))])


# read from stdin
if sys.stdin.isatty():  # to avoid getting stuck if no stdin is provided
    print("Running test data:")
    matrix_down = [[0.1, 0.0, 0.2, 0.4, 0.3],
                   [0.4, 0.6, 0.5, 0.2, 0.1],
                   [0.4, 0.4, 0.5, 0.2, 0.1],
                   [0.5, 0.6, 0.8, 0.5, 0.3]]

    matrix_right = [[0.3, 0.2, 0.4, 0],
                    [0.3, 0.2, 0.4, 0.2],
                    [0.0, 0.7, 0.3, 0.4],
                    [0.3, 0.3, 0.0, 0.2],
                    [0.1, 0.3, 0.2, 0.2]]

    matrix_dimension = [len(matrix_down[0]), len(matrix_right)]

else:
    inputString = sys.stdin.readlines()
    start_positions = [i for i, item in enumerate(inputString) if re.search('G.*', item)]
    end_positions = [i for i, item in enumerate(inputString) if re.search('---.*', item)]

    start_down = start_positions[0] + 1
    start_right = start_positions[1] + 1
    end_down = end_positions[0] - 1
    end_right = end_positions[1] - 1

    matrix_down = save_matrix(start_down, end_down, inputString)
    matrix_right = save_matrix(start_right, end_right, inputString)

    matrix_down = format_matrix(matrix_down)
    matrix_right = format_matrix(matrix_right)

    matrix_dimension = [len(matrix_down[0]), len(matrix_right)]


# run mtp
manhattanTouristProblem(matrix_down, matrix_right, matrix_dimension[0], matrix_dimension[1])
