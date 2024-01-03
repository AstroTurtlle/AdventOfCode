def check_whole_number(i,j, matrix, freq):
    j_initial = j
    number = 0
    p=1
    while j>=0 and matrix[i][j].isnumeric():
        number = p*int(matrix[i][j])+number
        freq[i][j] = 1
        p*=10
        j-=1
    j_initial+=1
    while j_initial<len(matrix[0]) and matrix[i][j_initial].isnumeric():
        freq[i][j_initial] = 1
        number = number*10+int(matrix[i][j_initial])
        j_initial+=1
    return number

def has_number(matrix, row, col):
    freq = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    nr_numbers = 0
    rows = len(matrix)
    cols = len(matrix[0])
    sum=1
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if matrix[new_row][new_col].isnumeric() and freq[new_row][new_col]==0:
                number = check_whole_number(new_row, new_col, matrix, freq)
                if number>0:
                    nr_numbers+=1
                    sum *= number
    if nr_numbers == 2:
        return sum
    return 0

def part_numbers2(file):
    with open(file) as f:
        suma=0
        lines = f.readlines()
        listc = [list(string)[:-1] for string in lines]
        for line_number in range(len(listc)):
            for char_number in range(len(listc[0])):
                if listc[line_number][char_number]=='*':
                    suma += has_number(listc, line_number, char_number)

    return suma

print(part_numbers2('./input.txt'))