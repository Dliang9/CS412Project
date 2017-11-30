import csv

class mushroom:

    def __init__(self, label, feature, prob):
        self.l = label
        self.f = feature
        self.p = prob
        
    def getProb(self) :
        return self.p

def likelihoodProbability(header,data,result):
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
            if result[c] == "e":
                count_pos[header[r]][data[c][r]] += 1
            else:
                count_neg[header[r]][data[c][r]] += 1
                    
    
    #edible probability of each variable 
    prob = {}
    for r in count_pos:
        print("##################################")
        print(r)
        for c in count_pos[r]:
            print(count_pos[r])
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
            
    #determining feature importance 
    features = [] 
    for r in count_pos:
        for c in count_pos[r]:
            features.append(mushroom(r, c, prob[r][c]))
            
    sortedElements = sorted(features, key=mushroom.getProb)
    
    #for e in sortedElements:
      #  print(e.l)
      #  print(e.f)
      #  print(e.p)    
    return prob
            
def calculate_predictor_prob(header, data):
    num_features = len(header)
    i = 0
    predictor_prob = {}
    while (i < num_features) :
         predictor_prob[header[i]] = {}
         for j in range (0, len(data)-1): 
             if (data[j][i] in predictor_prob[header[i]]):
                predictor_prob[header[i]][data[j][i]] += 1
             else:
                predictor_prob[header[i]][data[j][i]] = 0
         i += 1
    for feature in header:
        for value in predictor_prob[feature]:
            predictor_prob[feature][value] = predictor_prob[feature][value] / len(data)
         
    return predictor_prob;


def calculate_prediction(prob, predictor_probs, test_data, header, p_e, result):
    index = 0
    error = 0
    head = ''
    feature = ''
    for data in test_data:
        i = 0
        likelihood = 1.0
        predictor = 1.0
        while i < len(data):
            head = header[i]
            feature = data[i]
            likelihood = likelihood * prob[head][feature]
            predictor *= predictor_probs[header[i]][data[i]]
            i += 1

        # tmp_prob = likelihood * p_e / predictor
        tmp_prob = likelihood * p_e 
        if (tmp_prob >= 0.5): # edible
            if result[index] == 'e':
               error += 1
        if (tmp_prob < 0.5): # not edible
            if result[index] != 'e':
               error += 1
    print("error rate " + str(error) + "/" + str(len(result)))



#to be adapted to this project -- likely wrapped into def main()
def k_fold_cv(X, K, rand = False):
    if rand: from random import shuffle; X=list(X); shuffle(X)
    for k in range(K):
        train =[x for i, x in enumerate(X) if i % K != k]
        validation = [x for i, x in enumerate(X) if i % K == k]
        yield train, validation

X = [i for i in range(10)]
for train, validation in k_fold_cv(X, K=2):
    for x in X: assert (x in train) ^ (x in validation), x

    
def main():
    rd = open("mushrooms.csv")
    lines = csv.reader(rd, delimiter=' ')
    count = 0

    # contain the headers
    header = []

     # 2d array that contains data
    data = []
    edible_count = 0
    result = []

    for line in lines:
        if (count ==0):
            
            header = line[0].split( ",")
            header.pop(0)   # the first item is result
        else:
            tmp = line[0].split(",")
            if (tmp[0] == 'e'):
                edible_count += 1
            result.append(tmp[0])
            tmp.pop(0)
            data.append(tmp)
        count += 1
 
    # calcuate the prior distribution for P(y=edible)
    p_e = edible_count/count
    
    prob = likelihoodProbability(header,data,result)
    predictor_probs = calculate_predictor_prob(header, data)
    calculate_prediction(prob, predictor_probs, data, header, p_e, result )


if __name__=="__main__":
    main()
