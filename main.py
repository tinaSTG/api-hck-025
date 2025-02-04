from fastapi import FastAPI
import pandas as pd

#create API object
app = FastAPI()

# read data
data =pd.read_csv('data.csv')

# coba buat root hoom API (get)
@app.get("/")
def root():
    return{'message': 'Hello HCK 025 !'}

# endpoint sapaan
@app.get("/name/{name}")
def greet(name):
    return{'message': f'Hai {name}, how are you ?'}

# endpoint return data
@app.get("/data")
def get_data():
    return data.to_dict(orient='records')

# http://127.0.0.1:8000/data

# get data by id
@app.get("/data/{id}")
def search_data(id:int):
    result = data[data['id']==id]
    return {'result': result.to_dict(orient='records')}


# untuk menampilkan swagerai http://127.0.0.1:8000/docs

# menambahkan data
@app.post("/data/add")
def add_data(new_data:dict):
    global data
    
    new_row = pd.DataFrame([new_data])
    data = pd.concat([data, new_row], ignore_index=True)

    return {'message':data.to_dict(orient='records')}









