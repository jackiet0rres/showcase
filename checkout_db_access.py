from db_connect import DBConnect
from Fields import *
from Checkout import Checkout

def insert_checkout(checkout):
    db = DBConnect("project2").connect()
    result = db.Checkouts.insert_one({
        "patronid": checkout.patronid,
        "isbn": checkout.isbn,
        "fname": checkout.fname,
        "lname": checkout.lname,
        "status": checkout.status
    })
    return result.inserted_id

def return_book(patronid, isbn):
    db = DBConnect("project2").connect()
    result = db.Checkouts.update_one(
        {"patronid": patronid, "isbn": isbn, "status": "checked out"},
        {"$set": {"status": "returned"}}
    )
    return result.modified_count

def num_records(patronid, status):
    db = DBConnect("project2").connect()
    return db.Checkouts.count_documents({"patronid": patronid, "status": status})