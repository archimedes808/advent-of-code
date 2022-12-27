# A,X = Rock = 1
# B,Y = Paper = 2
# C,Z = Scissors = 3
# Lose = 0
# Draw = 3
# Win = 6


def win(challenge):
    match challenge:
        case 'A':
            return 2
        case 'B':
            return 3
        case 'C':
            return 1


def lose(challenge):
    match challenge:
        case 'A':
            return 3
        case 'B':
            return 1
        case 'C':
            return 2


def draw(challenge):
    match challenge:
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
            return 3


def rps(strats):
    if strats[1] == 'X':
        round_score = lose(strats[0])
    elif strats[1] == 'Y':
        round_score = draw(strats[0]) + 3
    elif strats[1] == 'Z':
        round_score = win(strats[0]) + 6
    return round_score


# Using list comprehension
# for each item in list, strip it, and add to new list lines[]
lines = [line.strip().split() for line in open('input.txt')]

my_score = 0

rounds = 1
for line in lines:
    my_score += rps(line)
    rounds += 1

print(f"Total rounds played: {rounds}")
print(f"Total score: {my_score}")
