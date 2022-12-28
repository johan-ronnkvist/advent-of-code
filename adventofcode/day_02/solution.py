import adventofcode.util as util
from abc import ABC

class Options:
    rock = 'A'
    paper = 'B'
    scissors = 'C'


def get_shape_score(shape: str):
    points_value = {Options.rock: 1,
                    Options.paper: 2,
                    Options.scissors: 3}

    return points_value[shape]


def get_result_score(first: str, second: str):
    score_win = 6
    score_draw = 3
    score_lost = 0

    if first == second:
        return score_draw
    elif first == Options.rock and second == Options.paper:
        return score_win
    elif first == Options.paper and second == Options.scissors:
        return score_win
    elif first == Options.scissors and second == Options.rock:
        return score_win
    else:
        return score_lost


def get_translated_choice(data: str):
    translations = {'X': Options.rock,
                    'Y': Options.paper,
                    'Z': Options.scissors}
    return translations[data]


def get_loosing_choice(choice: str):
    if choice == Options.rock:
        return Options.scissors
    elif choice == Options.paper:
        return Options.rock
    elif choice == Options.scissors:
        return  Options.paper


def get_winning_choice(choice: str):
    if choice == Options.rock:
        return Options.paper
    elif choice == Options.paper:
        return Options.scissors
    elif choice == Options.scissors:
        return Options.rock


def get_translated_choice_2(first: str, second: str):
    if second == 'X':  # loose
        return get_loosing_choice(first)
    elif second == 'Z':  # win
        return  get_winning_choice(first)
    elif second == 'Y':  # draw
        return first


def get_score(first: str, second: str):
    choice = get_translated_choice(second)
    return get_result_score(first, choice) + get_shape_score(choice)


def get_score_2(first: str, second: str):
    choice = get_translated_choice_2(first, second)
    return get_result_score(first, choice) + get_shape_score(choice)


if __name__ == '__main__':
    raw_input = util.read_input("input.txt")

    score_1 = 0
    score_2 = 0
    for line in raw_input:
        moves = line.split()
        score_1 += get_score(moves[0], moves[1])
        score_2 += get_score_2(moves[0], moves[1])

    print(score_1, score_2)