
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.6rzqn.mongodb.net/pytech?authSource=admin&replicaSet=atlas-e5rplc-shard-0&readPreference=primary&ssl=true&ssl=true&ssl_cert_reqs=CERT_NONE";

client = MongoClient(url)

db = client.pytech

#print("-- pytech Collection List --")
#print(db.list_collection_names())
#print("End of program, press any key to exit ")

Collections = db.students

#Displays students from the find Query
cursor = Collections.find({})
for record in cursor:
    print(record)


#find_one method to locate student_id 1010
print("find_one method to locate student_id 1010")
cursor = db.students.find_one({"student_id": "1010", "first_name": "Peter", "last_name": "parker"})
print(cursor)
del1 = db.students.delete_one({"student_id": "1010"})
print(del1)
#print("-- Displaying student document 1007 ")
#results = db.students.find_one({"student_id": "1007"})



