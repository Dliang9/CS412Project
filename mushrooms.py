import csv
import numpy as np

class mushroom:

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
       
        for c in count_pos[r]:
            
            if not r in prob:
                prob[r] = {}
            if not c in prob[r]:
                prob[r][c] = 0
            #probability of each variable = # of edible / total # of the variable in its feature
            prob[r][c] = count_pos[r][c]/(count_pos[r][c]+count_neg[r][c])
           
            
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
        likelihood_ = 1.0
        predictor = 1.0
        flag = 0
        while i < len(header):
            head = header[i]
            feature = data[i]
            if not feature in prob[head]:
                prob[head][feature] = 0
            
            likelihood = likelihood * prob[head][feature]
            likelihood_ = likelihood_ *(1 - prob[head][feature])
            #predictor *= predictor_probs[header[i]][data[i]]
            i += 1
        
        tmp_prob = likelihood * p_e #/ predictor
                
        tmp_prob_ = likelihood_ * ( 1 - p_e )
        
        if (tmp_prob >= tmp_prob_): # edible
            if result[index] != 'e':
               error += 1
        if (tmp_prob < tmp_prob_): # not edible
            if result[index] == 'e':
               error += 1
        index += 1
    print("error rate " + str(error) + "/" + str(len(result)))          
    return error/len(result)

    
def main():
    rd = open("mushrooms.csv")
    lines = csv.reader(rd, delimiter=' ')
    count = 0
    error = []

    # contain the headers
    header = []

    # 2d array that contains data
    data = []
   
    result = []
    for line in lines:
        if (count ==0):
            
            header = line[0].split( ",")
            header.pop(0)   # the first item is result
        else:
            tmp = line[0].split(",")
            
            result.append(tmp[0])
            tmp.pop(0)
            data.append(tmp)
        
    
    #K-FOLD
    k = 10
    test_length = len(data)/k
    start = 0
    end = test_length
    for i in range(0,k):
        train = []
        train_cls = []
        test = []
        test_cls = []
        edible_count = 0
        for line in range(0,len(data)):
            if line >= start and line <= end:
                test.append(data[line])
                test_cls.append(result[line])
            else:
                train.append(data[line])
                train_cls.append(result[line])
        start += test_length
        end += test_length
        if i == k-1:
            end = len(data)
        
        # calcuate the prior distribution for P(y=edible)
        for ln in train_cls:
            if ln == "e":
                eduble_count += 1
        p_e = edible_count/len(train_cls)
            
        # calcuate the prior distribution for P(y=edible)
        p_e = edible_count/count
        # calculate the likelihood probability 
        prob = likelihoodProbability(header,data,result)
        # calculate the predictor probability
        predictor_probs = calculate_predictor_prob(header, data)
    
        # use likelihood, preditor, prior probabilities to calculate the predictions
        err = calculate_prediction(prob, predictor_probs, test, header, p_e, test_cls )
        error.append(err)
    print(np.mean(error))



if __name__=="__main__":
    main()
