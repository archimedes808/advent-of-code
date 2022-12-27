# A,X = Rock = 1
# B,Y = Paper = 2
# C,Z = Scissors = 3
# Lose = 0
# Draw = 3
# Win = 6

def replace_values(values):
    # Replace letters with their score value
    values = values.strip()
    replace_dict = {
        'A': '1', 'B': '2', 'C': '3', 'X': '1', 'Y': '2', 'Z': '3'
    }
    for _key in replace_dict.keys():
        values = values.replace(_key, replace_dict[_key])
    return values

def rps(answers):
    answers = [int(x) for x in answers.strip().split(' ')]
    # If same answers, draw
    if sum(answers) == 2 or 1 not in answers and sum(answers) == 4 or sum(answers) == 6:
        round_score = 3
    # If your paper vs their rock or your scissors vs their paper, win
    elif answers[1] != 1 and answers[0] == answers[1] - 1:
        round_score = 6
    # If their paper vs your rock or their scissors vs your paper, lose
    elif answers[0] != 1 and answers[1] == answers[0] - 1:
        round_score = 0
    # If your rock vs their scissors, win
    elif answers[1] == 1 and answers[0] == 3:
        round_score = 6
    # If their rock vs your scissors, lose
    elif answers[0] == 1 and answers[1] == 3:
        round_score = 0
    round_score += answers[1]
    return round_score

# Using list comprehension
# for each item in list, strip it, and add to new list lines[]
lines = [replace_values(line) for line in open('input.txt')]

my_score = 0

rounds = 1
for line in lines:
    my_score += rps(line)
    rounds +=1

print(f"Total rounds played: {rounds}")
print(f"Total score: {my_score}")