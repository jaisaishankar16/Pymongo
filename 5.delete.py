import pymongo

if __name__=="__main__":
    # print("Welcome")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    # print(client)
    db=client["database"]
    collection=db['mySampleCollection']
    rec={'Name':"Sai"}
    # Delete One
    collection.delete_one(rec)

    # Delete Many
    collection.delete_many(rec)

    c1=collection.delete_many(rec)
    print(c1.deleted_count)
