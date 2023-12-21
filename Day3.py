def has_non_dot_or_number_neighbor(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < rows and 0 <= new_col < cols:
            if matrix[new_row][new_col] not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return True

    return False

def part_numbers(file):
    with open(file) as f:
        numbers = []
        lines = f.readlines()
        listc = [list(string)[:-1] for string in lines]
        for line_number in range(len(lines)):
            ok = 0
            nr = 0
            for letter in range(len(lines[line_number])):
                if lines[line_number][letter].isnumeric():
                    nr = nr * 10 + int(lines[line_number][letter])
                    if has_non_dot_or_number_neighbor(listc, line_number, letter):
                        ok = 1
                else:
                    if nr != 0 and ok == 1:
                        numbers.append(nr)
                    ok = 0
                    nr = 0
    return numbers
                    

num = part_numbers('./input.txt')
print(sum(num))