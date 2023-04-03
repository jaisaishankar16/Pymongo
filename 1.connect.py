import pymongo

if __name__=="__main__":
    print("Welcome")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    allDatabases= client.list_database_names()
    print(allDatabases)