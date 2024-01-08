def citire(filename):
    with open(filename) as f:
        time = f.readline().split()[1:]
        #time = [int(x) for x in time]
        distance = f.readline().split()[1:]
        #distance = [int(x) for x in distance]
        total_time = ''
        total_distance = ''
        for x in time:
            total_time = total_time + str(x)
            total_distance = total_distance + str(distance[time.index(x)])
    return int(total_time),int(total_distance)

def part1():
    time, distance = citire("input.txt")
    p = 1
    for i in range(len(time)):
        x = 1
        current_distance = time[i]-1
        while current_distance <= distance[i]:
            x += 1
            current_distance = (time[i] - x) * x
        p *= time[i]-2*x+1
    return p

def part2():
    time, distance = citire("input.txt")
    x = 1
    current_distance = time-1
    while current_distance <= distance:
        x += 1
        current_distance = (time - x) * x
    return time-2*x+1

print(part2())