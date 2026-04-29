def player(prev_play, opponent_history=[]):

    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "R"

    # last 3 moves pattern
    last_three = "".join(opponent_history[-3:])

    patterns = {}
    for i in range(len(opponent_history) - 3):
        seq = "".join(opponent_history[i:i+3])
        next_move = opponent_history[i+3]
        if seq == last_three:
            if next_move in patterns:
                patterns[next_move] += 1
            else:
                patterns[next_move] = 1

    if patterns:
        predicted = max(patterns, key=patterns.get)
    else:
        predicted = opponent_history[-1]

    # counter move
    if predicted == "R":
        return "P"
    elif predicted == "P":
        return "S"
    else:
        return "R"
