#Sample Input
data = """3
rectangle 1 1 10 5
circle 5 0 8
rectangle -5 3 5 8
5
1 1
4 5
10 10
-10 -1
4 -3"""
#Input handling for original problem
"""
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
data = '\n'.join(contents)
"""

#Classes handling target coord info based on Shape
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = int(x1), int(y1)
        self.x2, self.y2 = int(x2), int(y2)
    
class Circle:
    def __init__(self, x_coord, y_coord, radius):
        self.x = int(x_coord)
        self.y = int(y_coord)
        self.r = int(radius)

#Functions to check if shot is inside target. Todo: refactor to use classes
def is_inside_rectangle(rectangle, x, y):
    if rectangle.x1 <= x <= rectangle.x2 and rectangle.y1 <= y <= rectangle.y2:
        return True
    return False

def is_inside_circle(circle, x, y, r):
    if (x - circle.x)**2 + (y - circle.y)**2 <= circle.r**2:
        return True
    return False

#Splitting data into number of targets
num_targets = 0
data = data.split('\n')
num_targets= int(data[0])
list_of_targets = []

#Creating a list of target objects from the given input
for i in range(1, num_targets + 1):
    target_info = data[i].split(' ')
    if target_info[0] == 'rectangle':
        list_of_targets.append(Rectangle(target_info[1], target_info[2], target_info[3], target_info[4]))
    elif target_info[0] == 'circle':
        list_of_targets.append(Circle(target_info[1], target_info[2], target_info[3]))
        

#Splitting data into number of shots and shot info
shots = data[num_targets + 1:]
num_shots = int(shots[0])
shots = shots[1:]
shots = [shot.split(' ') for shot in shots]
shots = [[int(shot[0]), int(shot[1])] for shot in shots]

#Checking if shots are inside targets and printing the number of targets hit for each shot
for i in range(num_shots):
    target_hit_count = 0
    for target in list_of_targets:
        #print(shots[i][0], shots[i][1])
        if target.__class__.__name__ == 'Rectangle':
            if is_inside_rectangle(target, shots[i][0], shots[i][1]):
                target_hit_count += 1
        elif target.__class__.__name__ == 'Circle':
            if is_inside_circle(target, shots[i][0], shots[i][1], target.r):
                target_hit_count += 1
    print(target_hit_count)