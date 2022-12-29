import adventofcode.day_03.solution as solution


def test_rucksack_01():
    r = solution.Rucksack('vJrwpWtwJgWrhcsFMMfFFhFp')
    assert r.first == 'vJrwpWtwJgWr'
    assert r.second == 'hcsFMMfFFhFp'
    assert r.overlap == {'p'}


def test_rucksack_02():
    r = solution.Rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')
    assert r.first == 'jqHRNqRjqzjGDLGL'
    assert r.second == 'rsFMfFZSrLrFZsSL'
    assert r.overlap == {'L'}


def test_priority_conversion():
    assert solution.priority('a') == 1
    assert solution.priority('z') == 26
    assert solution.priority('A') == 27
    assert solution.priority('Z') == 52


def test_priority_calculation():
    data = ['vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw']

    result = solution.priority_sum(data)
    assert result == 157


def test_badge_identification():
    data_1 = ['vJrwpWtwJgWrhcsFMMfFFhFp',
              'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
              'PmmdzqPrVvPwwTWBwg']

    assert solution.badge_identifier(data_1) == 'r'

    data_2 = ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
              'ttgJtRGJQctTZtZT',
              'CrZsJsPPZsGzwwsLwLmpwMDw']

    assert solution.badge_identifier(data_2) == 'Z'


def test_badge_prioritization():
    data = ['vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw']

    assert solution.badge_priority_sum(data) == 70
