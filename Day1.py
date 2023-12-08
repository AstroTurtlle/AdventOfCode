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

elements = first_last("input.txt")
print(sum(elements))