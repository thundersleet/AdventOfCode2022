def read_lines_as_ints(filename):
    lines = read_lines(filename)
    int_lines = [int(line) for line in lines]
    return int_lines


def read_lines(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    return lines
