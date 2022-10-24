from random import randint

def enter (message):
    num = int(input(message))
    return num

def create_list_natural_numbers (length, max):
    nat_nums = []
    for i in range (length):
        nat_nums.append(randint(0, max))
    return nat_nums

def power_equation (coeffs):
    equation = ''
    for i in range (len(coeffs) - 1, 0, -1):
        if coeffs[i] != 0:
            if i == 1:
                equation += f'{coeffs[i]} x + '
            else:
                equation += f'{coeffs[i]} x^{i} + '
    if coeffs[0] == 0:
        equation += ' = 0'
    else:
        equation += f'{coeffs[0]} = 0'
    return equation

def string_to_list (string_equation):
    list_coeffs = [int(item) for item in string_equation.split() if item.isdigit()]
    list_coeffs.pop()
    return list_coeffs

def sum_coeffs (total_list_coeffs, new_list_coeffs):
    if len(total_list_coeffs) == 0:
        total_list_coeffs = new_list_coeffs
    else:
        if len(total_list_coeffs) < len(new_list_coeffs):
            for i in range (0, len(total_list_coeffs)):
                new_list_coeffs[-1 - i] += total_list_coeffs[-1 - i]
                total_list_coeffs = new_list_coeffs
        else:
            for i in range (0, len(new_list_coeffs)):
                total_list_coeffs[-1 - i] += new_list_coeffs[-1 - i]
    return total_list_coeffs

def list_to_string (coeffs):
    equation = ''
    for i in range (len(coeffs) - 1):
        if coeffs[i] != 0:
            if i == len(coeffs) - 2:
                equation += f'{coeffs[i]} x + '
            else:
                equation += f'{coeffs[i]} x^{len(coeffs) - 1 - i} + '
    if coeffs[len(coeffs) - 1] == 0:
        equation += ' = 0'
    else:
        equation += f'{coeffs[len(coeffs) - 1]} = 0'
    return equation