# import sys
# import csv
# import operator

# def sort_file(read_filename, write_filename, column):
    # data = csv.reader(open(read_filename), delimiter=',')
    # Convert column to an integer
    # sortedlist = sorted(data, key=operator.itemgetter(0))
    # fileWriter = csv.writer(open(write_filename, "w"), delimiter=',')
    # for row in sortedlist:
    #     fileWriter.writerow(row)

# Correct Answer:

import csv
import operator

def sort_file(read_filename, write_filename, column):
    data = csv.reader(open(read_filename), delimiter=',')
    sortedlist = sorted(data, key=operator.itemgetter(int(column)))
    fileWriter = csv.writer(open(write_filename, "w"), delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)