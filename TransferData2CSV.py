import csv
with open('abc.csv','w') as file:
    write = csv.writer(file)
    write.writerow(["Roll", "Name", "Age"])
    write.writerow([1, "Arif", 16])
    write.writerow([2, "Hamid", 17])


