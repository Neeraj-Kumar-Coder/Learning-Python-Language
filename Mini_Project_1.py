# Library Management System
def gettime():
    import datetime
    return datetime.datetime.now()


class Library:
    books = {"The C Programming Language": "Brian W. Kernighan and Dennis M. Ritchie",
             "Wings of Fire": "A.P.J. Abdul Kalam",
             "My experiment with truth": "Mahatma Ghandhi",
             }
    donater = {}
    renter = {}
    rent_period = "3 days"
    fine = "Rs.5/days"

    def displayBooks(self):
        print()
        for key, value in self.books.items():
            print(key + " : " + value)
        print()

    def displayRenters(self):
        if len(self.renter)==0:
            print("No renters found!!!")
        else:
            for key, value in self.renter.items():
                print(key + " : " + value)

    def displayDonaters(self):
        if len(self.donater)==0:
            print("No donaters found!!!")
        else:
            for key, value in self.donater.items():
                print(key + " : " + value)

    def addBook(self, name, details):
        store = details.split("-")
        self.books.update({store[0]: store[1]})
        self.donater.update({f"{name}-[ {gettime()} ]": details})
        print("Book added successfully!!!")

    def lendBook(self, name, details):
        store = details.split("-")
        if self.books[store[0]].endswith("(NOT AVAILABLE)"):
            print("This book is not available")
        else:
            self.renter.update({f"{name}-[ {gettime()} ]": details})
            self.books.update({store[0]: f"{store[1]} (NOT AVAILABLE)"})
            print("Book rented successfully!!!")
            print(f"Lending Time = {self.rent_period}\nFine = {self.fine}")

    def returnBook(self, name, details):
        store = details.split("-")
        self.books.update({store[0]: f"{store[1]}"})
        self.renter[name] = f"{name} - [{gettime()}] (RETURNED)"
        print("Book returned successfully!!!")


# MAIN CODE
library_1 = Library()
while(True):
    action = int(input("What you want to do?\n1. Display Books\n2. Add Book\n3. Rent Book\n4. Return Book\n5. Renters\n6. Donaters\n7. TO QUIT\n==> "))
    if action == 1:
        print("\n# LIST OF BOOKS")
        library_1.displayBooks()
    elif action == 2:
        name = input("Enter your name: ")
        book = input("Enter the book (e.g. bookname-author): ")
        try:
            library_1.addBook(name, book)
        except Exception as reason:
            print(f"Book adding failed : {reason}")
    elif action == 3:
        name = input("Enter your name: ")
        book = input("Enter the book (e.g. bookname-author): ")
        try:
            library_1.lendBook(name, book)
        except Exception as reason:
            print(f"Book lending failed : {reason}")
    elif action == 4:
        name = input("Enter your name: ")
        book = input("Enter the book (e.g. bookname-author): ")
        try:
            library_1.returnBook(name, book)
        except Exception as reason:
            print(f"Book returning failed : {reason}")
    elif action == 5:
        library_1.displayRenters()
    elif action == 6:
        library_1.displayDonaters()
    elif action == 7:
        print("Exiting Library...")
        break
    else:
        print("Enter a valid input!!!")
