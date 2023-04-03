import pymongo

if __name__=="__main__":
    # print("Welcome")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    # print(client)
    db=client["database"]
    collection=db['mySampleCollection']
    # Find one document
    one = collection.find_one({'Name':'Shankar'})
    print(one)
    # Find many documents
    allDocs=collection.find({'name':'sai'})
    for i in allDocs:
        print(i)
    # To hide any attribute then make it 0 let's hide "id"
    allDocs=collection.find({'name':'sai'},{'name':1,"_id":0})
    for i in allDocs:
        print(i)
    # Conditional Search
    one = collection.find_one({'name':'sai','marks':{"$gte":70}})
    print(one)
