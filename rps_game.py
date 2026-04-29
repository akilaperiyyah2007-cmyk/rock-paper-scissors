import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    p1_score = 0
    p2_score = 0

    for i in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            pass
        elif (p1_play == "R" and p2_play == "S") or \
             (p1_play == "P" and p2_play == "R") or \
             (p1_play == "S" and p2_play == "P"):
            p1_score += 1
        else:
            p2_score += 1

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    print("Player1:", p1_score, "Player2:", p2_score)
    win_rate = (p1_score / num_games) * 100
    print("Win rate:", win_rate)
    return win_rate


# Bots
def quincy(prev_play, counter=[0]):
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]

def abbey(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    if len(opponent_history) < 2:
        return "R"
    if opponent_history[-1] == opponent_history[-2]:
        return opponent_history[-1]
    return random.choice(["R", "P", "S"])

def kris(prev_play):
    return random.choice(["R", "P", "S"])

def mrugesh(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    if len(opponent_history) < 2:
        return "R"
    most_common = max(set(opponent_history), key=opponent_history.count)
    return most_common
