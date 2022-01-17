import random
import pandas as pd

filename = 'fake_mobile.csv'
brand_names = ['Kony', 'Siaomi', 'Szamsung', 'Rolomoto', 'PearPhone', 'Real', 'Okia', 'TwoPlus', 'POOP', 'Hulej']
model_names = ['Galaktyka', 'A', 'S', 'K', 'Mi', 'Not', 'West', 'COTO']

nr_low = 25
nr_mid = 50
nr_hi = 25

columns = ['Brand', 'Phone', 'Score', 'Votes', 'Performance', 'Camera', 'Audio', 'Battery', 'Price']
fake_db = pd.DataFrame(columns= columns)

for i in range(nr_low):
    brand = random.choice(brand_names)
    phone = f'{random.choice(model_names)}{random.randint(2, 20)}'
    score = round(random.normalvariate(6, 1.2), 2)
    votes = int(random.normalvariate(5000, 1000))
    perfomarce = int(random.normalvariate(30000, 5000))
    camera = int(random.normalvariate(80, 10))
    audio = int(random.normalvariate(55, 5))
    battery = int(random.normalvariate(70, 5))
    price = random.randint(500, 1500)
    gene = [brand, phone, score, votes, perfomarce, camera, audio, battery, price]
    genes = pd.Series(gene, index= fake_db.columns)
    fake_db = fake_db.append(genes, ignore_index = True)
for i in range(nr_mid):
    brand = random.choice(brand_names)
    phone = f'{random.choice(model_names)}{random.randint(2, 20)}'
    score = round(random.normalvariate(6, 1.2), 2)
    votes = int(random.normalvariate(5000, 1000))
    perfomarce = int(random.normalvariate(60000, 10000))
    camera = int(random.normalvariate(95, 10))
    audio = int(random.normalvariate(60, 5))
    battery = int(random.normalvariate(80, 5))
    price = random.randint(1600, 3000)
    gene = [brand, phone, score, votes, perfomarce, camera, audio, battery, price]
    genes = pd.Series(gene, index= fake_db.columns)
    fake_db = fake_db.append(genes, ignore_index = True)
for i in range(nr_hi):
    brand = random.choice(brand_names)
    phone = f'{random.choice(model_names)}{random.randint(2, 20)}'
    score = round(random.normalvariate(6, 1.2), 2)
    votes = int(random.normalvariate(5000, 1000))
    perfomarce = int(random.normalvariate(150000, 15000))
    camera = int(random.normalvariate(130, 10))
    audio = int(random.normalvariate(65, 5))
    battery = int(random.normalvariate(80, 5))
    price = random.randint(3200, 5500)
    gene = [brand, phone, score, votes, perfomarce, camera, audio, battery, price]
    genes = pd.Series(gene, index= fake_db.columns)
    fake_db = fake_db.append(genes, ignore_index = True)
fake_db.to_csv(filename)
print(fake_db)