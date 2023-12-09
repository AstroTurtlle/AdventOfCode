def first_last(file):
    elements = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            aux_first = -1
            aux_last = -1
            first_number = -1
            last_number = -1
            for i in range(int(len(line)/2)+1):
                if(line[i].isnumeric() and first_number == -1):
                    first_number = int(line[i])
                elif(line[i].isnumeric()):
                    aux_last = int(line[i])
                if(line[len(line)-i-1].isnumeric() and last_number == -1):
                    last_number = int(line[len(line)-i-1])
                elif(line[len(line)-i-1].isnumeric()):
                    aux_first = int(line[len(line)-i-1])
                if(first_number != -1 and last_number != -1):
                    break
            if(first_number == -1):
                if(aux_first != -1):
                    first_number = aux_first
                else:
                    first_number = last_number
            if(last_number == -1):
                if(aux_last != -1):
                    last_number = aux_last
                else:
                    last_number = first_number
            elements.append(first_number*10+last_number)
    return elements

def first_last2(file):
    elements = []
    digits = {"z": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    digit_names = list(digits.keys())
    digit_names_reverse = []
    digit_names_reverse = [digit[::-1] for digit in digit_names]
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            minim_nr = 10
            maxim_nr = -1
            minim = len(line)
            maxim = -1
            for j in range(1,10):
                if line.find(digit_names[j]) < minim and line.find(digit_names[j]) != -1:
                    minim = line.find(digit_names[j])
                    minim_nr = j
                if len(line) - line[::-1].find(digit_names_reverse[j]) - 1 > maxim and line[::-1].find(digit_names_reverse[j]) != -1:
                    maxim = len(line) - line[::-1].find(digit_names_reverse[j]) - 1
                    maxim_nr = j
                if line.find(str(j)) < minim and line.find(str(j)) != -1:
                    minim = line.find(str(j))
                    minim_nr = j
                if len(line) - line[::-1].find(str(j)) - 1 > maxim and line[::-1].find(str(j)) != -1:
                    maxim = len(line) - line[::-1].find(str(j)) - 1
                    maxim_nr = j
            elements.append(minim_nr*10+maxim_nr)
    return elements

elements = first_last2("input.txt")
print(elements)
print(sum(elements))
#print(elements[858])