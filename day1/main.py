import os
import sys
import time
from collections import Counter


def solve_captcha(captcha_file, part2=False):

    count = Counter()

    assert os.path.isfile(captcha_file), "File %s does not exist!" % captcha_file

    captcha = open(captcha_file, 'r').readlines()

    if len(captcha) > 1:
        raise IOError("Only one line captchas are accepted")
    else:
        captcha = captcha[0].strip()

    length = len(captcha)
    for i, digit in enumerate(captcha):

        if part2:
            next_digit = captcha[(i + length/2) % length]
        else:
            next_digit = captcha[(i+1) % length]

        if not digit.isdigit() or not next_digit.isdigit():
            raise ValueError(
                "Only digits are accepted (detected sequence %s%s in string position %d)"
                % (digit, next_digit, i)
            )

        if digit == next_digit:
            count.update(digit)

    return sum_counter(count)


def sum_counter(counter):
    total = 0
    for digit, count in counter.items():
        total += int(digit) * count

    return total


if __name__ == '__main__':

    file_path = sys.argv[-1]

    print "\nCaptcha File: %s\n" % file_path

    t1 = time.time()
    solution = solve_captcha(file_path)
    t2 = time.time() - t1

    print "Part 1 Solution: %d" % solution
    print "Took: %.3f ms\n" % (t2 * 1000)

    t1 = time.time()
    solution = solve_captcha(file_path, part2=True)
    t2 = time.time() - t1

    print "Part 2 Solution: %d" % solution
    print "Took: %.3f ms" % (t2 * 1000)