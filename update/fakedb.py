import random
import pandas as pd

filename = 'fake_mobile.csv'
brand_names = ['Kony', 'Siaomi', 'Szamsung', 'Rolomoto', 'PearPhone', 'Real', 'Okia', 'TwoPlus', 'POOP', 'Hulej']
model_names = ['Galaktyka', 'A', 'S', 'K', 'Mi', 'Not', 'West', 'COTO']

nr_low = 50
nr_mid = 100
nr_hi = 50

columns = ['Brand', 'Phone', 'Score', 'Votes', 'Performance', 'Camera', 'Audio', 'Battery', 'Price']
fake_db = pd.DataFrame(columns= columns)

for i in range(nr_low):
    brand = random.choice(brand_names)
    phone = f'{random.choice(model_names)}{random.randint(2, 20)}'
    score = round(random.normalvariate(6, 1.2), 2)
    votes = int(random.normalvariate(5000, 1000))
    gene = [brand, phone, score, votes, 0, 0, 0, 0, 0]
    genes = pd.Series(gene, index= fake_db.columns)
    fake_db = fake_db.append(genes, ignore_index = True)
fake_db.to_csv(filename)
print(fake_db)