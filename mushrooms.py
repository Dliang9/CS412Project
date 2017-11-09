import csv

rd = open("../Project/mushrooms.csv")
a = csv.reader(rd, delimiter=' ')

for b in a:
    print(b)
    exit
