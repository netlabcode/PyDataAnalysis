import csv
import collections

count_number = collections.Counter()
with open('SSIDConnected.csv') as input_file:
    r = csv.reader(input_file, delimiter=';')
    headers = next(r)
    for row in r:
        count_number[row[3]] += 1

CountCollect = count_number.most_common(100)


print CountCollect
