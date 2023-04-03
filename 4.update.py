import pymongo

if __name__=="__main__":
    # print("Welcome")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    # print(client)
    db=client["database"]
    collection=db['mySampleCollection']
    prev={'Name':"Sai"}
    # If there is no attribute with name "Age" then it adds it to the document
    nextt={"$set":{"Age":100}}
    # Update only One
    collection.update_one(prev,nextt)



    nextt={"$set":{"Age":100}}
    # Update Many
    collection.update_many(prev,nextt)

    # To get how many documents modified
    c=collection.update_many(prev,nextt)
    print(c.modified_count)
