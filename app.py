import pymongo
import pandas as pd
import json

# Connection to MongoDB / MongoDB bağlantısı
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['JobsData'] # Database name / Veritabanı adı
collection = db['Jobs'] # Collection name / Collection adı

# Read CSV file / veri okuma işlemi
csv_file_path = 'c:/Users/Ahmet/Desktop/BuyukVeri/dataset.csv'
df = pd.read_csv(csv_file_path)

# Convert dataframe to dictionary / dataframe'i dictionary'e çevirme
records = df.to_dict(orient='records')

# Insert collection
collection.insert_many(records)

print("Veri başarıyla MongoDB'ye aktarıldı.")

df.head()

print(db.list_collection_names()) #collection isimlerini listeleme

data = df.to_dict(orient='records') #verileri dictionary'e çevirme

db.jobs.insert_many(data) #verileri collection'a ekleme 

result = db.jobs.find().limit(2) #verileri listeleme / limit(2) ilk iki veriyi getirir
for r in result:
    print(r)
    print("\n")