from pymongo import MongoClient

database_name = 'Iris_db'
mongo_port = 27017

url = f"mongodb://localhost:{mongo_port}/{database_name}"
myclient = MongoClient(url)
db = myclient[database_name]

collection_user= db['user_detail']
collection_prediction = db['prediction_details']

def registeration(user_detail):
    user_details_dict={}
    user_details_dict['Name'] = user_detail['Name']
    user_details_dict['Password'] = user_detail['Password']
    user_details_dict['Mail_Id'] = user_detail['Mail_Id']
    user_details_dict['Phone'] = user_detail['Phone']
    collection_user.insert_one(user_details_dict)
    return 'Registration done successfully'

def login(login_details):
    user_details_dict={}
    user_details_dict['Name']=login_details['Name']
    user_details_dict['Password']=login_details['Password']
    verify= collection_user.find_one(user_details_dict)

    if not verify:
        return 'Invalid User id or Password'
    return 'You have logged in successfully.'

def save_predict_details(SepalLengthCm,SepalWidthCm,PetalLengthCm, PetalWidthCm):
    details= {'SepalLengthCm':SepalLengthCm, 'SepalWidthCm': SepalWidthCm, 'PetalLengthCm':PetalLengthCm,
              'PetalWidthCm': PetalWidthCm }
    collection_prediction.insert_one(save_predict_details)

    return 'data saved successfully'
