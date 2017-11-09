import csv

rd = open("mushrooms.csv")
lines = csv.reader(rd, delimiter=' ')
count = 0

# contain the headers
header = []

# 2d array that contains data
data = []

for line in lines:
   if (count ==0):
      header = line[0].split( ",")
   else:
      data.append(line[0].split(","))
   count += 1
 
