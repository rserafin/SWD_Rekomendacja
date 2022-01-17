import random
import pandas as pd
from topsis import *

def random_reco(database, columns):
    results = pd.DataFrame(columns= columns)
    size = len(database)
    numbers = []
    for i in range(3):
        numbers.append(random.randint(0, size))
        result = database[numbers[i]:numbers[i]+1][columns]
        results = pd.concat([results, result], ignore_index = True, axis = 0)
    return results

def simple_reco(database, columns):
    results = pd.DataFrame(columns= columns)
    m = database['Votes'].quantile(0.9)
    C = database['Score'].mean()
    q_data = database.copy().loc[database['Votes']>=m]
    def weighted_rating(x, m=m, C=C):
        v = x['Votes']
        R = x['Score']
        return (v/(v+m) * R) + (m/(m+v) * C)
    q_data['score'] = q_data.apply(weighted_rating, axis = 1)
    q_data = q_data.sort_values('score', ascending=False)
    for i in range(3):
        result = q_data[i:i+1][columns]
        results = pd.concat([results, result], ignore_index = True, axis = 0)
    return results

def topsis_reco(database, columns, weights = [1, 1, 1, 1, 1], criterias = [True, True, True, True, False]):
    results = pd.DataFrame(columns= columns)
    e_m = database[:][['Performance', 'Camera', 'Audio', 'Battery', 'Price']]
    evaluation_matrix = e_m.to_numpy()
    t = Topsis(evaluation_matrix, weights, criterias)
    t.calc()
    for i in range(3):
        numbers = t.rank_to_best_similarity()[:3]
        result = database[numbers[i]:numbers[i]+1][columns]
        results = pd.concat([results, result], ignore_index = True, axis = 0)
    #print(t.rank_to_best_similarity())
    return results