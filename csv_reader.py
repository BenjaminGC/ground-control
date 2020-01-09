import csv

file = str(input('Filename: '))

with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
