with open ('26.txt') as file:
    n = int(file.readline())
    stations = [list(map(int, i.split())) for i in file]

stations = sorted(stations, key= lambda x: (x[0], x[1]))

for station