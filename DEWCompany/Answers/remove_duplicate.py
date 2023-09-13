# import sys
# import csv
# import operator

# def remove_duplicate(read_filename, write_filename, column):
    # data = csv.reader(open(read_filename), delimiter=',')
    # newrows = []
    # Change "rows" to "data" to iterate over the CSV reader
    # for row in rows:
    #     if row not in newrows:
    #         newrows.append(row)
    # writer = csv.writer(open(write_filename, "w"))
    # writer.writerows(newrows)

# Correct Answer:

import csv

def remove_duplicate(read_filename, write_filename):
    data = csv.reader(open(read_filename), delimiter=',')
    newrows = []
    for row in data:
        if row not in newrows:
            newrows.append(row)
    writer = csv.writer(open(write_filename, "w"), delimiter=',')
    writer.writerows(newrows)

