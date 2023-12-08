import sqlite3
from inventory import Inventory
from tabulate import tabulate

class Cart:
    def __init__(self, databaseName = 'MainDatabase.db', tableName = 'Cart'):
        self.databaseName = databaseName
        self.tableName = tableName
        self.connection = sqlite3.connect('MainDatabase.db')
        self.cursor = self.connection.cursor()

    # VIEW CART
    def viewCart(self, userID):
        query = f"SELECT ISBN, Title, Stock  FROM {self.tableName} WHERE userID = ?"
        self.cursor.execute(query, (userID,))
        cart_items = self.cursor.fetchall()

        if not cart_items:
            print("Your cart is empty.")
            print()
        else:
            print("Items in the cart:")
            headers = ["ISBN", "Title", "Stock"]
            table_data = []

            for item in cart_items:
                ISBN = item[0]
                Title = item[1]
                Stock = item[2]
                table_data.append([ISBN, Title, Stock])

            table = tabulate(table_data, headers=headers, tablefmt="grid", showindex="always")
            print(table)
            print()

    # ADD TO CART
    def addToCart(self, userID, ISBN):
        query = f"SELECT Stock FROM {self.tableName} WHERE userID = ? AND ISBN = ?"
        self.cursor.execute(query, (userID, ISBN,))

        if self.cursor.fetchone() is None:
            current_stock = 0
        else:
            query = f"SELECT Stock FROM {self.tableName} WHERE userID = ? AND ISBN = ?"
            self.cursor.execute(query, (userID, ISBN,))
            current_stock = self.cursor.fetchone()[0]

        query = "SELECT Title FROM Inventory WHERE ISBN = ?"
        self.cursor.execute(query, (ISBN,))
        title = self.cursor.fetchone()[0]

        if int(current_stock) == 0:
            query = f"INSERT INTO {self.tableName} (userID, ISBN, Title, Stock) VALUES (?,?,?,?)"
            self.cursor.execute(query, (userID, ISBN, title, 1))
            self.connection.commit()
            print(f"Item {ISBN} added to the cart!")

        else:
            new_stock = current_stock + 1
            query = f"UPDATE {self.tableName} SET Stock = {new_stock} WHERE userID = ? AND ISBN = ?"
            self.cursor.execute(query, (userID, ISBN,))
            self.connection.commit()
            print(f"The item already exists in the cart; the stock has been updated now!")
            print()


    # REMOVE FROM CART
    def removeFromCart(self, userID, ISBN):
        query = f"SELECT Stock FROM {self.tableName} WHERE userID = ? AND ISBN = ?"
        self.cursor.execute(query, (userID, ISBN,))
        if self.cursor.fetchone() is None:
            print(f"Item {ISBN} is not in your cart.")
            print()
        else:
            query = f"SELECT Stock FROM {self.tableName} WHERE userID = ? AND ISBN = ?"
            self.cursor.execute(query, (userID, ISBN,))
            current_stock = self.cursor.fetchone()[0]
            print(f"Current quantity: {current_stock}.")
            num = int(input("How many do you wish to remove? "))
            if num > current_stock or num < 0:
                print("Invalid amount. Please try again.")
                print()
            else:
                new_stock = current_stock - num
                query = f"UPDATE {self.tableName} SET Stock = {new_stock} WHERE userID = ? AND ISBN = ?"
                self.cursor.execute(query, (userID, ISBN))
                self.connection.commit()
                print(f"{num} copy/copies of item {ISBN} removed from the cart!")
                print()
            query = f"DELETE FROM {self.tableName} WHERE userID = ? AND ISBN = ? AND Stock = 0"
            self.cursor.execute(query, (userID, ISBN))
            self.connection.commit()

    # CHECKOUT
    def checkOut(self, userID):
        query = f"SELECT COUNT(*) FROM {self.tableName} WHERE userID = ?"
        self.cursor.execute(query, (userID,))
        item_len = self.cursor.fetchone()[0]

        if item_len == 0:
            print("Cart is empty! No checkout at this time.")
        else:
            print("Checking out your items: ")
            query = f'SELECT ISBN, Stock FROM {self.tableName} WHERE userID = ?'
            self.cursor.execute(query, (userID,))
            cart_items = self.cursor.fetchall()

            # this will be used to call the decreaseStock function
            inventory = Inventory(self.databaseName, 'Inventory')

            headers = ["ISBN", "Stock"]
            table_data = []

            for item in cart_items:
                table_data.append(list(item))

            table = tabulate(table_data, headers=headers, tablefmt="grid", showindex="always")
            print(table)

            for item in cart_items:
                x = 0
                while x < item[1]:
                    inventory.decreaseStock(item[0])
                    x = x + 1

            clear_cart_query = f"DELETE FROM {self.tableName} WHERE userID = ?"
            self.cursor.execute(clear_cart_query, (userID,))
            self.connection.commit()
            print("Checkout complete! Cart has been cleared.")
