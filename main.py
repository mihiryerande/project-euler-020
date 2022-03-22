# Problem 20:
#     Factorial Digit Sum
#
# Description:
#     n! means n × (n − 1) × ... × 3 × 2 × 1
#
#     For example,
#       10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#       and the sum of the digits in the number 10! is
#       3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#     Find the sum of the digits in the number 100!

from math import ceil, floor, log, log10


def main(n):
    """
    Returns the sum of the digits of the number n! (n factorial)

    Args:
        n (int): Natural number

    Returns:
        Sum of digits of n!

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    # To prevent overflow for large factorials,
    #   maintain a decimal representation of n!
    #   as an array of digits (in reverse),
    #   removing unnecessary zeros from the end, while computing.
    digit_len_full = floor(sum([log10(i) for i in range(1, n+1)])) + 1  # Number of digits overall in n!
    fives_count = sum([(n // 5**i) for i in range(1, floor(log(n, 5)) + 1)])  # Number of extra zeros at the end
    digit_buffer = ceil(log10(n))  # Buffer space to not run out while multiplying
    digits_len = digit_len_full + digit_buffer - fives_count

    digits = [0 for _ in range(digits_len)]  # 1's digit, 10's digit, etc

    # Linearly iterate to get the factorial by multiplying
    i = 0
    digits[0] = 1  # Begin with 0!
    digit_count = 1  # To shorten the iterations

    while i < n:
        # Multiply the digits by i
        # This shouldn't be computationally expensive as `i` is assumed to not be huge
        i += 1
        carried = 0
        for j in range(digit_count):
            carried, digits[j] = divmod(i * digits[j] + carried, 10)

        # If the factorial now extends past current `digit_count`,
        #   meaning `carried` ended up greater than zero,
        #   extend the digit range of the factorial.
        j = digit_count
        while carried > 0:
            carried, digits[j] = divmod(carried, 10)
            j += 1
            digit_count += 1

        # Trim any superfluous zeros from end of number
        while digits[0] == 0:
            digits.pop(0)
            digits.append(0)
            digit_count -= 1

    return sum(digits)


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    power_sum = main(num)
    print('Sum of digits of 2^{}:'.format(num))
    print('  {}'.format(power_sum))
