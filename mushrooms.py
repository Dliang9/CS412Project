import csv

rd = open("mushrooms.csv")
lines = csv.reader(rd, delimiter=' ')
count = 0

# contain the headers
header = []

# 2d array that contains data
data = []
edible_count = 0

for line in lines:
   if (count ==0):
      header = line[0].split( ",")
      header.pop(0)   # the first item is result
   else:
      tmp = line[0].split(",")
      if (tmp.pop(0) == 'e'):
          edible_count += 1
      data.append(tmp)
   count += 1
 
# calcuate the prior distribution for P(y=edible)
p_e = edible_count/count
