# kattis_challenges
Collection of Kattis Challenges longer then a handful of lines

# Handling Input
---
## Single Line
```
data = input()
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