def arm_calc(inp_num):
    """
    Does the Armstrong calculation - Sum of each digit to the power of number of digit in the number.
    :param num: int
    :return: calculated int
    """
    num_digit_list = list(str(inp_num))
    num_digit_list = [int(digit) for digit in num_digit_list]
    num_len = len(num_digit_list)
    sum_result = 0

    # Calculating the sum of digits
    for digit in num_digit_list:
        sum_result += digit ** num_len

    return sum_result


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
    print(armstrong_numbers(153))


if __name__ == '__main__':
    main()


