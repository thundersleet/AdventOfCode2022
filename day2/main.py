import common.file_manipulation as file_manipulation


def day2_part1(filename):
    """
    a function to calculate the answer to Day 2 Part 1
    :param filename: the filename of the problem input
    :return: the answer to Day 2 Part 1
    """
    answer = None
    turn_list = file_manipulation.read_lines(filename)
    score_list = []
    for turn in turn_list:
        match turn[0]:
            case 'A':
                match turn[2]:
                    case 'X':
                        score_list.append(1 + 3)
                    case 'Y':
                        score_list.append(2 + 6)
                    case 'Z':
                        score_list.append(3 + 0)
            case 'B':
                match turn[2]:
                    case 'X':
                        score_list.append(1 + 0)
                    case 'Y':
                        score_list.append(2 + 3)
                    case 'Z':
                        score_list.append(3 + 6)
            case 'C':
                match turn[2]:
                    case 'X':
                        score_list.append(1 + 6)
                    case 'Y':
                        score_list.append(2 + 0)
                    case 'Z':
                        score_list.append(3 + 3)
            case _:
                raise Exception("Elf turn choice did not match pattern")

    answer = sum(score_list)
    return answer


def day2_part2(filename):
    """
    a function to calculate the answer to Day 2 Part 2
    :param filename: the filename of the problem input
    :return: the answer to Day 2 Part 2
    """
    answer = None
    turn_list = file_manipulation.read_lines(filename)
    score_list = []
    for turn in turn_list:
        match turn[0]:
            case 'A':
                match turn[2]:
                    case 'X':
                        score_list.append(3 + 0)
                    case 'Y':
                        score_list.append(1 + 3)
                    case 'Z':
                        score_list.append(2 + 6)
            case 'B':
                match turn[2]:
                    case 'X':
                        score_list.append(1 + 0)
                    case 'Y':
                        score_list.append(2 + 3)
                    case 'Z':
                        score_list.append(3 + 6)
            case 'C':
                match turn[2]:
                    case 'X':
                        score_list.append(2 + 0)
                    case 'Y':
                        score_list.append(3 + 3)
                    case 'Z':
                        score_list.append(1 + 6)
            case _:
                raise Exception("Elf turn choice did not match pattern")

    answer = sum(score_list)
    return answer


if __name__ == '__main__':
    print(f'Day 2 Part 1 answer: {day2_part1("input1.txt")}')
    print(f'Day 2 Part 2 answer: {day2_part2("input1.txt")}')
