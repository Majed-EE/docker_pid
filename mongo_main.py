from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
import sys
load_dotenv(find_dotenv())
# from logging import Logger

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

password=os.getenv("MONGO_PWD") # this works- dont use environ.get
logging.debug(f'password: {password}')
# password="database1234"

connection_string=f"mongodb+srv://mikeashraf:{password}@cluster0.gfipe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
print(connection_string)
client=MongoClient(connection_string)
try:
    dbs=client.list_database_names()
except Exception as e:
    print("Exception: ")
    print(e)
    sys.exit(0)  

test_db=client.test
collections=test_db.list_collection_names()
logging.debug(collections)

# RDMS- relationational database management system, sql- structure query language

def insert_test_doc():
    collection=test_db.test
    test_document={"name":"mike","age":30,"type":"Test"}
    insert_id=collection.insert_one(test_document).inserted_id
    logging.debug(f"insert id: {insert_id}") ## this id is bson type not regular integer
    # print(collections)

# insert_test_doc()
production = client.production
new_collection=production.new_collection


def create_documents():
    first_names=["tim","shrimp","brimp"]
    last_names=["smith","jones","williams"]
    ages=[20,30,40]

    docs=[]

    for first_names,last_names,age in zip(first_names,last_names,ages):
        person_document={"first_name":first_names,"last_name":last_names,"age":age}
        logging.debug((f"person document: {person_document}"))
        # person_collection.insert_one(person_document)
        docs.append(person_document)
    logging.debug(f"docs: {docs}")
    new_collection.insert_many(docs)

# create_documents()
logging.debug(f"new colllections")

# logging.debug(f"person: {person}")
printer=pprint.PrettyPrinter(indent=4)
from bson.objectid import ObjectId
def find_person():
    people=new_collection.find()
    
    for person in people:
        printer.pprint(person)

    ####
    tim=new_collection.find_one({"first_name":"tim"})
    printer.pprint(tim)
    ############
    count=new_collection.count_documents(filter={})
    printer.pprint(count)
    person_id="6764febb346671aced969408"
    _id=ObjectId(person_id)
    person=new_collection.find_one({"_id":_id})
    printer.pprint(person)

def get_age_range(min_age,max_age):
    query={"age":{"$gte":min_age,"$lte":max_age}}
    people=new_collection.find(query)
    for person in people:
        printer.pprint(person)

def project_columns():
    query={"first_name":1,"last_name":1,"_id":0} # 0 means dont give me the ids
    people=new_collection.find({},query)
    for person in people:
        printer.pprint(person)


######### how to update a person #############
def update_person_by_id():
    person_id="6764febb346671aced969408"
    _id=ObjectId(person_id)
    # all_updates={
    #     "$set":{"new_field":True},
    #     "$inc":{"age":1},
    #     "$rename":{"first_name":"first","last_name":"last"}
    # }
    # new_collection.update_one({"_id":_id}, all_updates)


    new_collection.update_one({"_id":_id},{"$unset":{"new_field":""}})



update_person_by_id()