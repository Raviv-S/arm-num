def arm_calc(inp_num):
    """
    Calculates the sum of each digit to the power of number of digit in the number.
    :param num: int
    :return: calculated int
    """
    digits = list(map(int, str(inp_num)))
    num_len = len(digits)
    return sum(digit ** num_len for digit in digits)


def armstrong_numbers(checked_num):
    """
    Returns all the armstrong numbers between 1 and the input.
    :param checked_num: Int - the maximum range to check.
    :return: List of all the armstrong numbers in the range.
    """
    return list(filter(lambda instance: instance == arm_calc(instance), range(1, checked_num + 1)))


def main():
    print(armstrong_numbers(99999))


if __name__ == '__main__':
    main()


