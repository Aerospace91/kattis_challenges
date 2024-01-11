# kattis_challenges
Collection of Kattis Challenges longer then a handful of lines

# Handling Input
---
## Single Line
```
data = input()
```
or
```
a = sys.stdin.readline()
```

## Multi-Line
```
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
data = '\n'.join(contents)
```
or
```
contents = sys.stdin.readlines()
```
---

# target_hit.py

https://open.kattis.com/problems/hittingtargets

---
## Input
Input starts with an integer **m** indicating the number of targets.
Each of the next **m** lines begins with the word rectangle or circle and then a description of the target boundary.
After the target descriptions is an integer **n** indicating the number of shots that follow.
The next n lines each contain two integers **x** , **y** indicating the coordinates of a shot. All **x** and **y** coordinates for targets and shots are in the range

## Output
For each of the **n** shots, print the total number of targets the shot hits.

# temp_check.py

https://open.kattis.com/problems/cold?editresubmit=12631883

Very simple challenge but I'm particularly proud of the solution and feeling like I'm starting to grasp python 1 liners

---
## Input 
1. The first line contains a single positive integer **n** that specifies the number of temperatures collected
2. The second line contains **n** temperatures, each seperated by a single space.

## Output
You must print a single integer: the number of temperatures strictly less than zero.

# cudoviste.py

https://open.kattis.com/problems/cudoviste?editresubmit=12633287

---
## Summary
His friend, Slavko, works part time in the city parking company. He periodically sends Mirko a map of the city with occupied parking spaces marked. The map can be represented as a table with **R** rows, **C** columns each. Each cell can contain a building (symbol ‘#’), a parked car (symbol ‘X’) or a free parking space (symbol ‘.’). A monster truck is quite huge, **2x2** cells to be exact.

Help Mirko calculate the number of possible parking spaces grouped by the number of cars he needs to squash to park in them. We are only interested in the number of cars Mirko will squash on the parking space, not the number of cars he will squash on the way over. However, Mirko can’t park on a building. Not even a monster truck is large enough to squash buildings

## Input
The first line of input contains two integers, **R** and **C**, the number of rows and columns of the map.
The next **R** lines contain **C** characters each. Only characters ‘#’, ‘X’ and ‘.’ appear in the input. Note that ‘X’ will always be capital.

## Output
The output consists of five lines, the total number of parking spaces Mirko can park on if he squashes 
0 cars (first line), 
1 car (second line), 
2 cars (third line), 
3 cars (fourth line), 
4 cars (fifth line).

## Sample Input
```
4 4
#..#
..X.
..X.
#XX#
```
## Sample Output
```
1
1
2
1
0
```