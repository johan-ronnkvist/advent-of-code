def read_input(filename):
    with open(filename) as file:
        return [line.rstrip() for line in file]