# DO NOT MODIFY THE CODE IN THIS FILE

# Source of this code: https://gist.github.com/mauricioaniche/671fb553a81df9e6b29434b7e6e53491
# Python builtins package https://docs.python.org/3/library/builtins.html

import builtins

input_values = []
print_values = []


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs