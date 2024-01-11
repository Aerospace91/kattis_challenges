import sys

r, c = list(map(int, input().split(' ')))
contents = sys.stdin.readlines()

parking_grid = []
for content in contents:
    a = content.strip('\n')
    parking_grid.append([*a])

zero_car = 0
one_car = 0
two_car = 0
three_car = 0
four_car = 0

for i in range(r - 1):
    for j in range(c - 1):
        check = [parking_grid[i][j], parking_grid[i][j + 1], parking_grid[i + 1][j], parking_grid[i + 1][j + 1]]
        dot = check.count('.')
        car  = check.count('X')
        building = check.count('#')
        if dot == 4:
            zero_car += 1
        elif dot == 3 and car == 1 and building == 0:
            one_car += 1
        elif dot == 2 and car == 2 and building == 0:
            two_car += 1
        elif dot == 1 and car == 3 and building == 0:
            three_car += 1
        elif dot == 0 and car == 4 and building == 0:
            four_car += 1

car_list = [zero_car, one_car, two_car, three_car, four_car]
for car in car_list:
    print(car)
            