class Book:
    def __init__(self, title, isbn, pagecount, pubdate, shortdescr, longdescr, status,authors,categories):
        self.title = title
        self.isbn=isbn
        self.pagecount=pagecount
        self.pubdate=pubdate
        self.shortdescr = shortdescr if shortdescr else None
        self.longdescr=longdescr
        self.status=status
        self.authors=authors
        self.categories=categories

    def display(self):
        print("title :" + self.title)
        print("isbn :" + self.isbn)
        print("page count : " + str(self.pagecount))
        print("publication date : " + str(self.pubdate))

        if self.shortdescr:
            print("Short Description : " + self.shortdescr)
        else:
            print("Short Description : Not available")

        if self.longdescr:
            print("Long Description : " + self.longdescr)
        else:
            print("Long Description : Not available")

        print("Status : " + self.status)
        print("Authors", self.authors)
        print("Categories:", self.categories)


