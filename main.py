import csv
rows = []
with open("/Users/frankjr./assignments-2/csv-reader/data/dogs.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

import csv
rows = []
with open("/Users/frankjr./assignments-2/csv-reader/data/cats.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

class Pet():

    defin a function that opens either of the cat file or dog file.