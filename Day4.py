from math import floor


def input_read(filename):
    winning_numbers = []
    personal_numbers = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line_splitted = line.split(':')
            win_numbers, numbers = line_splitted[1].split('|')
            winning_numbers.append(win_numbers.split())
            personal_numbers.append(numbers.split())
    return winning_numbers, personal_numbers

w_nr, tries = input_read('input.txt')
suma = 0
for i in range(len(tries)):
    p=0.5
    for j in tries[i]:
        if j in w_nr[i]:
            p*=2
    suma+=floor(int(p))
print(suma)