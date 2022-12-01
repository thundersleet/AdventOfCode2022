import common.file_manipulation as file_manipulation


def get_elf_calorie_list(filename):
    """
    function to get a list of the total calories each elf is carrying
    :param filename: the filename of the problem input
    :return: a list of elf calorie sums, in order
    """
    lines = file_manipulation.read_lines(filename)
    calorie_sum = 0
    elf_calories = []
    for line in lines:
        if line != '\n':
            calorie_sum += int(line)
        else:
            elf_calories.append(calorie_sum)
            calorie_sum = 0
    return elf_calories


def day1_part1(filename):
    """
    a function to calculate the answer to Day 1 Part 1
    :param filename: the filename of the problem input
    :return: the answer to Day 1 Part 1
    """
    elf_calorie_list = get_elf_calorie_list(filename)

    return max(elf_calorie_list)


def day1_part2(filename):
    """
    a function to calculate the answer to Day 1 Part 2
    :param filename: the filename of the problem input
    :return: the answer to Day 1 Part 2
    """
    elf_calorie_list = get_elf_calorie_list(filename)
    elf_calorie_list_sorted = sorted(elf_calorie_list)
    top3_elf_calories = elf_calorie_list_sorted[-3:]
    top3_elf_calorie_sum = sum(top3_elf_calories)
    return top3_elf_calorie_sum


if __name__ == '__main__':
    print(day1_part1('input1.txt'))
    print(day1_part2('input1.txt'))
