from common import file_manipulation


def day3_part1(filename):
    """
    a function to calculate the answer to Day 3 Part 1
    :param filename: the filename of the problem input
    :return: the answer to Day 3 Part 1
    """
    answer = 0
    rucksack_list = file_manipulation.read_lines(filename)
    for rucksack in rucksack_list:
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]
        for item in first_compartment:
            if item in second_compartment:
                if item.isupper():
                    answer += (ord(item) - ord('A')) + 27
                else:
                    answer += (ord(item) - ord('a')) + 1
                break
    return answer


def day3_part2(filename):
    """
    a function to calculate the answer to Day 3 Part 2
    :param filename: the filename of the problem input
    :return: the answer to Day 3 Part 2
    """
    answer = 0
    rucksack_list = file_manipulation.read_lines(filename)
    for first, second, third in zip(rucksack_list[::3], rucksack_list[1::3], rucksack_list[2::3]):
        for item in first:
            if item in second and item in third:
                if item.isupper():
                    answer += (ord(item) - ord('A')) + 27
                else:
                    answer += (ord(item) - ord('a')) + 1
                break
    return answer


if __name__ == '__main__':
    print(f'Day 3 Part 1 answer: {day3_part1("input1.txt")}')
    print(f'Day 3 Part 2 answer: {day3_part2("input1.txt")}')
