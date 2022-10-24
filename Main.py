from Common_methods import create_list_natural_numbers as create, power_equation
from Common_methods import power_equation as equation
from Common_methods import list_to_string as to_string
from Common_methods import enter
from Common_methods import string_to_list as to_list
from Common_methods import sum_coeffs

from Import_in_files import import_in_files as in_file

from random import randint
import os

os.system('cls')

amount_equation = enter('Введите количество уравнений (файлов): ')
max_coeff = 100
for i in range (amount_equation):
    max_power = enter(f'Введите максимально возможную степень в {i + 1} уравнении: ')
    power = randint(1, max_power)
    coeffs = create (power + 1, max_coeff)
    print(coeffs)
    my_equation = equation(coeffs)
    print(my_equation)
    file = f'Power_equation_{i + 1}.txt'
    in_file (file, my_equation)

total_list = []
    
for k in range (amount_equation):
    path = f'Power_equation_{k + 1}.txt'
    with open(path, 'r') as data:
        txt = data.read()
    list_coeffs = to_list(txt)
    print('Список текущих коэффициентов: ')
    print(list_coeffs)
    total_list = sum_coeffs(total_list, list_coeffs)
    print('Итоговый список коэффициентов')
    print(total_list)

total_equation = to_string(total_list)

file = 'Sum_equation.txt'
in_file (file, total_equation)