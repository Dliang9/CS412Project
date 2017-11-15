import csv

def featureProbability(header,data):
    #count number of each variable for each feature
    count_pos = {}
    count_neg = {}
    
    for r in range(0, len(header)):
        if not header[r] in count_pos:
            count_pos[header[r]] = {}
        if not header[r] in count_neg:
            count_neg[header[r]] = {}
        for c in range(0, len(data)):
            if not data[c][r] in count_pos[header[r]]:
                count_pos[header[r]][data[c][r]] = 0
            if not data[c][r] in count_neg[header[r]]:
                count_neg[header[r]][data[c][r]] = 0
            if data[c][0] == "e":
                count_pos[header[r]][data[c][r]] += 1
            else:
                count_neg[header[r]][data[c][r]] += 1
                    
    
    #edible probability of each variable 
    prob = {}
    for r in count_pos:
        print("##################################")
        print(r)
        for c in count_pos[r]:
            #print(count_pos[r])
            if not r in prob:
                prob[r] = {}
            if not c in prob[r]:
                prob[r][c] = 0
            #probability of each variable = # of edible / total # of the variable in its feature
            prob[r][c] = count_pos[r][c]/(count_pos[r][c]+count_neg[r][c])
            print("++++++++++++++++++++++++++++++++++")
            print(c)
            print("e ",count_pos[r][c])
            print("p ",count_neg[r][c])
            print("----------------------------------")
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
