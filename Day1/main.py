import common.file_manipulation as file_manipulation


def get_elf_calorie_list(filename):
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
    elf_calorie_list = get_elf_calorie_list(filename)

    return max(elf_calorie_list)


def day1_part2(filename):
    elf_calorie_list = get_elf_calorie_list(filename)
    elf_calorie_list_sorted = sorted(elf_calorie_list)
    top3_elf_calories = elf_calorie_list_sorted[-3:]
    top3_elf_calorie_sum = sum(top3_elf_calories)
    return top3_elf_calorie_sum


if __name__ == '__main__':
    print(day1_part1('input1.txt'))
    print(day1_part2('input1.txt'))
