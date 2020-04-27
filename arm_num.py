def arm_calc(num):
    """
    Does the Armstrong calculation - Sum of each digit to the power of number of digit in the number.
    :param num: int
    :return: calculated int
    """
    num_digit_list = list(str(num))
    num_digit_list = [int(digit) for digit in num_digit_list]
    num_len = len(num_digit_list)
    sum_result = 0

    # Calculating the sum of digits
    for digit in num_digit_list:
        sum_result += digit**num_len

    return sum_result


checked_num = 1000
armstrong_list = []
while checked_num > 0:
    if checked_num == arm_calc(checked_num):
        armstrong_list.append(checked_num)
    checked_num -= 1

print(armstrong_list)