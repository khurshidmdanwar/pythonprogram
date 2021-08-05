import csv
with open("student.csv", 'r') as arif:
    read = csv.DictReader(arif)
    for r in read:
        print(dict(r))