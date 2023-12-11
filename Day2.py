def max_rgb(file):
    with open(file) as f:
        lines = f.readlines()
        red_max = []
        green_max = []
        blue_max = []
        for line in lines:
            reveals = line.split(':')[1].split(';')
            #print(reveals)
            red_max.append(0)
            green_max.append(0)
            blue_max.append(0)
            for i in reveals:
                cubes = i.split(',')
                for color in cubes:
                    color = color.strip()
                    nr, c = color.split()
                    nr = int(nr)
                    if c == "red":
                        if nr > red_max[-1]:
                            red_max[-1] = nr
                    elif c == "green":
                        if nr > green_max[-1]:
                            green_max[-1] = nr
                    else:
                        if nr > blue_max[-1]:
                            blue_max[-1] = nr
    return red_max, green_max, blue_max

def ex2():
    sum = 0
    red_max, green_max, blue_max = max_rgb("input.txt")
    for i in range(len(red_max)):
        sum += red_max[i] * green_max[i] * blue_max[i]  
    return sum
        
print(ex2())