"""
A - ROCK
B - PAPER
C - SCISSORS

X - ROCK
Y - PAPER
Z - SCISSORS
"""

data = open("day_two.in")
data = [i.strip() for i in data]
score = 0
for i in data:
    if i[0] == "A":
        if i[-1] == "X":
            score += 0
            score += 3
        elif i[-1] == "Y":
            score += 3
            score += 1
        else:
            score += 6
            score += 2
    elif i[0] == "B":
        if i[-1] == "X":
            score += 0
            score += 1
        elif i[-1] == "Y":
            score += 3
            score += 2
        else:
            score += 6
            score += 3
    elif i[0] == "C":
        if i[-1] == "X":
            score += 0
            score += 2
        elif i[-1] == "Y":
            score += 3
            score += 3
        else:
            score += 6
            score += 1

    # if i[-1] == "X":
    #     score += 1
    # elif i[-1] == "Y":
    #     score += 2
    # elif i[-1] == "Z":
    #     score += 3

print(score)
