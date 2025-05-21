class Checkout:
    def __init__(self, patronid, isbn, fname, lname, status):
        self.patronid = patronid
        self.isbn=isbn
        self.fname = fname
        self.lname = lname
        self.status=status


    def display(self):
        print("Patron ID :" + self.patronid)
        print("ISBN :" + self.isbn)
        print("First name : " + fname)
        print("Last name : " + lname)
        print("Status : " + self.status)

