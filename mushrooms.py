import csv

def featureProbability(header,data):
    #count number of each variable for each feature
    count = {}
    for r in range(0,len(data)):
        if data[r][0] == "e":
            for c in range(0,len(header)):
                if not header[c] in count:
                    count[header[c]] = {}
                if not data[r][c] in count[header[c]]:
                    count[header[c]][data[r][c]] = 0
                count[header[c]][data[r][c]] += 1
    
    #edible probability of each variable 
    prob = {}
    for r in count:
        print(r)
        for c in count[r]:
            
            if not r in prob:
                prob[r] = {}
            if not c in prob[r]:
                prob[r][c] = 0
            
            #need to divide by no. of each variable not data\s length
            prob[r][c] = count[r][c]/len(data)
            print(c)
            print(prob[r][c])
            

    
def main():
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
            if (tmp[0] == 'e'):
                edible_count += 1
            data.append(tmp)
        count += 1
 
    # calcuate the prior distribution for P(y=edible)
    p_e = edible_count/count
    
    featureProbability(header,data)
    
if __name__=="__main__":
    main()
