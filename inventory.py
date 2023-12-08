import sqlite3
from tabulate import tabulate
# tabulate installation guide: https://pypi.org/project/tabulate/

class Inventory:
    def __init__(self, databaseName = 'MainDatabase.db', tableName = 'Inventory'):
        self.databaseName = databaseName
        self.tableName = tableName
        self.connection = sqlite3.connect(databaseName)
        self.cursor = self.connection.cursor()

    def viewInventory(self):
        self.cursor.execute("SELECT * FROM Inventory")
        bookInventory = self.cursor.fetchall()

        print("Book Inventory:")

        headers = ["ISBN", "Title", "Author", "Genre", "Pages", "Release Date", "Stock"]
        table_data = []

        for book in bookInventory:
            table_data.append(list(book))

        table = tabulate(table_data, headers=headers, tablefmt="grid", showindex="always")
        print(table)

    def searchInventory(self):

        data = input("Enter the unique ISBN of the book (xxx-x-xxxxx-xxx-x): ")
        print()
        query = "SELECT * FROM Inventory WHERE ISBN = ?"
        self.cursor.execute(query, (data,))

        ## fetches those rows that match with the entered book title
        searchBook = self.cursor.fetchall()


        if any(data in i for i in searchBook):
            print("Book found:")
            headers = ["ISBN", "Title", "Author", "Genre", "Pages", "Release Date", "Stock"]
            table_data = []

            for book in searchBook:
                table_data.append(list(book))

                table = tabulate(table_data, headers=headers, tablefmt="grid", showindex="always")
                print(table)

        else:
            print("There's no book titled", data, "in our inventory.")

    def decreaseStock(self, ISBN):

        query = "SELECT Stock FROM Inventory WHERE ISBN = ?"
        self.cursor.execute(query, (ISBN,))
        searchBook = self.cursor.fetchone()
        currentQuantity = int(searchBook[0])
        newQuantity = currentQuantity - 1
        self.cursor.execute("UPDATE Inventory SET Stock = ? WHERE ISBN = ?", (newQuantity, ISBN))
        self.connection.commit()
