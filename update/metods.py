import random
import pandas as pd

def random_reco(database, columns):
    results = pd.DataFrame(columns= columns)
    size = len(database)
    numbers = []
    for i in range(3):
        numbers.append(random.randint(0, size))
        result = database[numbers[i]:numbers[i]+1][columns]
        results = pd.concat([results, result], ignore_index = True, axis = 0)
    return results