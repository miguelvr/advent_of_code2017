import os
import sys
import time
import numpy as np


def compute_checksum(spreadsheet_path):

    assert os.path.isfile(spreadsheet_path), "File %s not found!" % spreadsheet_path

    spreadsheet = read_spreadsheet(spreadsheet_path)

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

    t1 = time.time()
    checksum = compute_checksum(file_path)
    t2 = time.time() - t1

    print "Spreadsheet File:", file_path
    print "Checksum:", checksum
    print "Took: %.3f ms" % (t2 * 1000)
