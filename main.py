from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()

fake_db = [{"name":"Anar","Price":50},{"name":"Banana","Price":30},{"name":"Apple","Price":80}]

class user_input(BaseModel):
    name:str
    Price:int

@app.get("/get_all")
def get_all():
    return {"data":fake_db,"message":"We get all data"}

@app.get("/get_one/{item_in}")
def get_one(item_in:int):
    f_data = fake_db[item_in]
    return {"data":f_data,"message":"Item got it"}

@app.post("/create_data")
def data_create(data:user_input):
    data_dict = {}
    data_dict["name"] = data.name
    data_dict["Price"] = data.Price
    fake_db.append(data_dict)
    return {"message":"Data created successfully!","data":data_dict}

