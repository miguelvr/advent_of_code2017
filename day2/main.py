import os
import sys
import time
import numpy as np
import itertools


def compute_checksum(spreadsheet_path, part2=False):

    assert os.path.isfile(spreadsheet_path), "File %s not found!" % spreadsheet_path

    spreadsheet = read_spreadsheet(spreadsheet_path)

    if part2:
        checksum = []
        for i, row in enumerate(spreadsheet):
            combinations = np.array(list(itertools.combinations(row, 2)))
            combinations = np.vstack((combinations, combinations[:, [1, 0]]))
            is_divisible = np.where((combinations[:, 0] % combinations[:, 1]) == 0)[0]
            assert len(is_divisible) == 1, \
                "Found more than one divisible number in row %d" % i
            checksum.append(combinations[is_divisible][0, 0] / combinations[is_divisible][0, 1])
        checksum = np.array(checksum).sum()
    else:
        max_values = np.max(spreadsheet, axis=-1)
        min_values = np.min(spreadsheet, axis=-1)

        checksum = (max_values - min_values).sum()

    return int(checksum)


def read_spreadsheet(file_path):
    spreadsheet = []
    with open(file_path, 'r') as f:
        for line in f:
            spreadsheet.append(np.fromstring(line, sep='\t'))

    return np.stack(spreadsheet, axis=0)


if __name__ == '__main__':
    file_path = sys.argv[-1]

    print "Spreadsheet File:", file_path

    t1 = time.time()
    checksum = compute_checksum(file_path)
    t2 = time.time() - t1

    print "Part 1 Checksum:", checksum
    print "Took: %.3f ms" % (t2 * 1000)

    t1 = time.time()
    checksum = compute_checksum(file_path, part2=True)
    t2 = time.time() - t1

    print "Part 2 Checksum:", checksum
    print "Took: %.3f ms" % (t2 * 1000)
