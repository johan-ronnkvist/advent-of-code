import adventofcode.day_04.solution as solution


def test_fully_contained_sections():
    data = ['2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8']

    assert solution.fully_contained_sections(data) == 2


def test_overlapping_sections():
    data = ['2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8']

    assert solution.overlapping_sections(data) == 4
