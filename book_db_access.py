from db_connect import DBConnect
from Fields import *
from Book import Book

def retrieve_by_isbn(isbn):
    db = DBConnect("project2").connect()
    result = db.books.find_one({ISBN: isbn})
    if result:
        return Book(
            result[TITLE],
            result[ISBN],
            result[PAGECOUNT],
            result.get(PUBDATE, "Unknown"),
            result.get(SHORTDESCR, None),
            result.get(LONGDESCR, None),
            result[STATUS],
            result[AUTHORS],
            result[CATEGORIES]
        )
    return None

def list_categories():
    db = DBConnect("project2").connect()
    return db.books.distinct(CATEGORIES)

def retrieve_books_by_category(category):
    db = DBConnect("project2").connect()
    results = db.books.find({CATEGORIES: category})
    return [Book(
        result[TITLE],
        result[ISBN],
        result[PAGECOUNT],
        result.get(PUBDATE, "Unknown"),
        result.get(SHORTDESCR, None),
        result.get(LONGDESCR, None),
        result[STATUS],
        result[AUTHORS],
        result[CATEGORIES]
    ) for result in results]


def retrieve_books_by_letter(letter): #interesting query if a person wants to know
    #what books start with a specific letter
    db = DBConnect("project2").connect()
    results = db.books.find(
        {"title": {"$regex": f"^{letter}", "$options": "i"}}
    ).sort("title", 1).limit(10)  #sorts by title alphabetically and limit to 10
    return [Book(
        result[TITLE],
        result[ISBN],
        result[PAGECOUNT],
        result.get(PUBDATE, "Unknown"),
        result.get(SHORTDESCR, None),
        result.get(LONGDESCR, None),
        result[STATUS],
        result[AUTHORS],
        result[CATEGORIES]
    ) for result in results]

def retrieve_books_by_page_count(min_page_count):
    db = DBConnect("project2").connect()
    #interesting query for books with a page count greater than the specified value
    #useful for someone who needs a summer book that is a certain page number
    results = db.books.find(
        {"pageCount": {"$gt": min_page_count}}
    ).sort("pageCount", 1).limit(10)
    return [Book(
        result[TITLE],
        result[ISBN],
        result[PAGECOUNT],
        result.get(PUBDATE, "Unknown"),
        result.get(SHORTDESCR, None),
        result.get(LONGDESCR, None),
        result[STATUS],
        result[AUTHORS],
        result[CATEGORIES]
    ) for result in results]

