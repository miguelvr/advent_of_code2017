import os
import sys
from collections import Counter


def solve_captcha(captcha_file):

    count = Counter()

    assert os.path.isfile(captcha_file), "File %s does not exist!" % captcha_file

    captcha = open(captcha_file, 'r').readlines()

    if len(captcha) > 1:
        raise IOError("Only one line captchas are accepted")
    else:
        captcha = captcha[0].strip()

    for i, digit in enumerate(captcha[:-1]):

        next_digit = captcha[i+1]

        if not digit.isdigit() or not next_digit.isdigit():
            raise ValueError(
                "Only digits are accepted (detected sequence %s%s in string position %d)"
                % (digit, next_digit, i)
            )

        if digit == next_digit:
            count.update(digit)

    if captcha[-1] == captcha[0]:
        count.update(captcha[-1])

    return sum_counter(count)


def sum_counter(counter):
    total = 0
    for digit, count in counter.items():
        total += int(digit) * count

    return total


if __name__ == '__main__':
    file_path = sys.argv[-1]
    solution = solve_captcha(file_path)

    print "Captcha File:", file_path
    print "Solution:", solution
