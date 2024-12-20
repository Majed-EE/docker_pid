import bson 
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, render_template
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
import logging
import sys

load_dotenv(find_dotenv())
# from logging import Logger
connection_string=os.getenv("MONGO_PWD") # this works- dont use environ.get
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

mongo_client=MongoClient(connection_string)
try:
    dbs=mongo_client.list_database_names()
except Exception as e:
    print("Exception: ")
    print(e)
    sys.exit(0)  
bookshelf_db = mongo_client.bookshelf  ## name of the db
collection = bookshelf_db.books ## name of the collection 
def insert_book(book):
    
    collection.insert_one(book)
# insert_book({"title": "Atlas Shrugged", "author": "Raynd Ayn","pages":785})
# logging.debug(f"Collections {collection}")
logging.debug(f"dbs: {dbs}")


dbs=mongo_client.list_database_names()
logging.debug(f"dbs: {dbs}")
collections=bookshelf_db.list_collection_names()

app = Flask(__name__)

# print(connection_string)
client=MongoClient(connection_string)


# CREATE and READ
@app.route("/books", methods=["GET", "POST"])


def books():
    if request.method == "POST":
        # CREATE
        title:str=request.json["title"]
        pages: str=request.json["pages"]
        author: str=request.json["author"]

        # isnert new book into our books collection in Atlas
        collection.insert_one({"title": title, "author": author, "pages": pages})
                              
        
        # book = request.form.to_dict()
        # insert_book(book)
        return "Book added successfully"
    elif request.method=="GET":
        # READ
        bookshelf = list(collection.find())
        novels=[]

        for titles in bookshelf:
            title=titles["title"]
            pages=titles["pages"]
            author=titles["author"]
            shelf={"title":title,"pages":pages,"author":author}
            novels.insert(0,shelf)

        return novels

# UPDATE



# DELETE









@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)