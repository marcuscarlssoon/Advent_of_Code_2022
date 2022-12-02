# A=Rock, B=Paper, C=Scissors
# X=Rock, Y=Paper, Z=Scissors

# 1 for Rock, 2 for Paper, and 3 for Scissors

score1 = 0
score2 = 0

shape_points = {"X": 1, "Y": 2, "Z": 3}
win = 6
draw = 3

with open('input.txt') as input_text:
    lines = [x.split() for x in list(input_text.read().splitlines())]

    for line in lines:
        if line[0] == "A":
            if line[1] == "X":
                score1 += shape_points[line[1]] + draw
                score2 += shape_points["Z"]
            elif line[1] == "Y":
                score1 += shape_points[line[1]] + win
                score2 += shape_points["X"] + draw
            elif line[1] == "Z":
                score1 += shape_points[line[1]]
                score2 += shape_points["Y"] + win

        elif line[0] == "B":
            if line[1] == "Y":
                score1 += shape_points[line[1]] + draw
                score2 += shape_points["Y"] + draw
            elif line[1] == "Z":
                score1 += shape_points[line[1]] + win
                score2 += shape_points["Z"] + win
            elif line[1] == "X":
                score1 += shape_points[line[1]]
                score2 += shape_points["X"]

        elif line[0] == "C":
            if line[1] == "Z":
                score1 += shape_points[line[1]] + draw
                score2 += shape_points["X"] + win
            elif line[1] == "Y":
                score1 += shape_points[line[1]]
                score2 += shape_points["Z"] + draw
            elif line[1] == "X":
                score1 += shape_points[line[1]] + win
                score2 += shape_points["Y"]

    print(score1)
    print(score2)
