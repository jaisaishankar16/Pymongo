import pymongo

if __name__=="__main__":
    # print("Welcome")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    # print(client)
    db=client["database"]
    collection=db['mySampleCollection']
    # Insert One
    dictionary={'name':'jai','marks':70}
    collection.insert_one(dictionary)
    # dictionary2={'name':'sai','marks':60}
    # collection.insert_one(dictionary2)

    # Insert Many
    insertThese=[
        {'_id':1 ,'Name':'Sai','Age':40},
        {'_id': 2,'Name':'Jai','Age':45},
        {'_id': 3,'Name':'Shankar','Age':30},
        {'_id': 4,'Name':'Kona','Age':25}
    ]
    collection.insert_many(insertThese)

    # Id's must be unique
