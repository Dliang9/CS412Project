import csv

rd = open("../mushrooms.csv") 
a = csv.reader(rd, delimiter=' ')
count = 0

# contain the headers
header = []

# 2d array that contains data
data = []

for b in a:
   if (count ==0):
      header = b[0].split( ",")
   else:
      data.append(b[0].split(",")) 
   count += 1

# test
#print(header)
#for tmp in data:
#    print(tmp)
#    print("\n")
