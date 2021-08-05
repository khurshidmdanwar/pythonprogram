import csv
with open('abc.csv', 'r') as file:
    reader = csv.reader(file)
    try:
        for row in reader:
            print(row)
    except FileNotFoundError:
        print('Sorry File not found')