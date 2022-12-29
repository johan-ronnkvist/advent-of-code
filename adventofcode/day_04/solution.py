import adventofcode.util as util
import re


def ranges_from_line(line: str):
    capture = re.match(r"^(\d+)-(\d+),(\d+)-(\d+)", line)
    first = range(int(capture.group(1)), int(capture.group(2))+1)
    second = range(int(capture.group(3)), int(capture.group(4))+1)
    return first, second


def fully_contained(line: str):
    ranges = ranges_from_line(line)
    first = ranges[0]
    second = ranges[1]

    return (first.start >= second.start and first.stop <= second.stop) or \
        (second.start >= first.start and second.stop <= first.stop)


def overlapping_line(line: str):
    ranges = ranges_from_line(line)

    return any([1 if n in ranges[1] else 0 for n in ranges[0]])

def fully_contained_sections(sections):
    return sum([1 if fully_contained(line) else 0 for line in sections])


def overlapping_sections(sections):
    return sum([1 if overlapping_line(line) else 0 for line in sections])


if __name__ == '__main__':
    raw_input = util.read_input('input.txt')

    print(f'fully contained: {fully_contained_sections(raw_input)}')
    print(f'overlapping: {overlapping_sections(raw_input)}')
