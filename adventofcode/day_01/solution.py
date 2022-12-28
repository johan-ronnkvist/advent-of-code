import adventofcode.util as util

def get_elves_by_calorie_count(data):
    elves = []
    calories = 0
    for line in data:
        if len(line) == 0:
            elves.append(calories)
            calories = 0
        else:
            calories = calories + int(line)
    return elves


if __name__ == '__main__':
    data = util.read_input('input.txt')
    elves = get_elves_by_calorie_count(data)

    max_value = max(elves)
    index = elves.index(max_value)

    total_kcal = 0;
    for i in range(3):
        current_max = max(elves)
        total_kcal += current_max
        elves.remove(current_max)

    print(total_kcal)



