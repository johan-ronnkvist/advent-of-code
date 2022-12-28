import adventofcode.util as util


def priority(char: str):
    assert len(char) == 1
    ordinal = ord(char)
    if ordinal >= ord('a'):
        return ordinal-96
    else:
        return ordinal-38


class Rucksack:
    def __init__(self, data):
        self._data = data
        self._mid_point = int(len(data)/2)

    @property
    def contents(self):
        return self._data

    @property
    def first(self):
        return self._data[0:self._mid_point]

    @property
    def second(self):
        return self._data[self._mid_point:len(self._data)]

    @property
    def overlap(self):
        first = set(self.first)
        second = set(self.second)
        return first.intersection(second)


def priority_sum(data):
    rucksacks = [Rucksack(entry) for entry in data]
    prio_sum = 0
    for sack in rucksacks:
        for item in sack.overlap:
            prio_sum += priority(item)

    return prio_sum


def badge_identifier(data):
    assert len(data) == 3
    pack1 = Rucksack(data[0])
    pack2 = Rucksack(data[1])
    pack3 = Rucksack(data[2])
    intersection = list(set(pack1.contents).intersection(pack2.contents, pack3.contents))
    assert len(intersection) == 1
    return intersection[0]


def badge_priority_sum(data):
    assert (len(data) % 3) == 0
    badge_prio_sum = 0
    for i in range(0, len(data), 3):
        badge_prio_sum += priority(badge_identifier(data[i:i+3]))

    return badge_prio_sum


if __name__ == '__main__':
    raw_input = util.read_input("input.txt")
    print(priority_sum(raw_input), badge_priority_sum(raw_input))

