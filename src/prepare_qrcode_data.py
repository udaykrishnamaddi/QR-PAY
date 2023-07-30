from datetime import date, datetime
from src import encode_password as ep
import csv

def structure_data(stall_name, data):

    # preparing userData
    username = data["username"]
    password = data["password"]

    encryptedPassword=ep.encryptPassword(password)

    userData={"username":username, "encryptedPassword":encryptedPassword}

    # preparing qrcode metaData (generated time, date)
    metaData = {}

    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    metaData["generatedDay"]=current_date
    metaData["generatedTime"]=current_time

    # get food prices
    foodPrices = {}
    food_items = []

    file = open('./static/data/'+stall_name+'.csv')
    file_reader = csv.reader(file)

    for row in file_reader:
        print(row)
        foodPrices[row[0]]=row[1]

    file.close()

    data.pop("username")
    data.pop("password")

    foodData = {}

    for food_item in data:

        if food_item!='showpassword':
            foodData[food_item]=data[food_item]

    data = {"userData": userData, "metaData": metaData, "foodData": foodData, "foodPrices": foodPrices}

    print(data)

    return data