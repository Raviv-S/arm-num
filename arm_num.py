def arm_calc(inp_num):
    """
    Calculates the sum of each digit to the power of number of digit in the number.
    :param num: int
    :return: calculated int
    """
    num_digit_list = list(map(int, str(inp_num)))
    num_len = len(num_digit_list)
    return sum([digit ** num_len for digit in num_digit_list])


def armstrong_numbers(checked_num):
    """
    Returns all the armstrong numbers between 1 and the input.
    :param checked_num: Int - the maximum range to check
    :return: List of all the
    """
    armstrong_list = []
    for ins in range(checked_num + 1):
        if ins == arm_calc(ins):
            armstrong_list.append(ins)
    return armstrong_list


def main():
    print(armstrong_numbers(99999))


if __name__ == '__main__':
    main()


