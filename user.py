import sqlite3
from tabulate import tabulate

# user class
class User:
    # constructor
    def __init__(self, databaseName = 'MainDatabase.db', tableName = 'User'):
        self.databaseName = databaseName
        self.tableName = tableName
        self.userID = None
        self.loggedIn = False
        self.connection = sqlite3.connect(databaseName)
        self.cursor = self.connection.cursor()

    # login function
    def login(self):
        try:
            login_email = input("Enter your email address to login: ")
            login_password = input("Enter your password to login: ")

            query = "SELECT userID FROM User WHERE Email = ? AND Password = ?"
            self.cursor.execute(query, (login_email, login_password))
            self.userID = self.cursor.fetchone()

            if self.userID is None:
                print("Could not log you in.")
                print()
            else:
                self.userID = self.userID[0]
                print("You have been logged in successfully.")
                print()
                self.loggedIn = True

        except sqlite3.Error as error:
            print("Failed to log in.", error)


    # logout function
    def logout(self):
        self.userID = None
        self.loggedIn = False
        print("You are now logged out successfully.")
        print()

    # view account information function
    def viewAccountInformation(self):
        if self.loggedIn:
            query = "SELECT * FROM User WHERE userID = ?"
            self.cursor.execute(query, (self.userID,))
            result = self.cursor.fetchall()

            print("Account information:")
            headers = ["userID", "Email", "Password", "FirstName", "LastName", "Address", "City", "State", "Zip", "Payment"]
            table_data = []

            for x in result:
                table_data.append(list(x))

            table = tabulate(table_data, headers=headers, tablefmt="grid")
            print(table)

    # create account function
    #https://pynative.com/python-sqlite-insert-into-table/
    def createAccount(self):
        try:
            user_id = input("Enter your desired user ID: ")
            email = input("Enter your email address: ")
            password = input("Enter new password: ")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            address = input("Enter your address: ")
            city = input("Enter the city in which you live: ")
            state = input("Enter the state in which you live: ")
            zip_code = int(input("Enter your zip code: "))
            payment = input("Enter your payment information: ")

            data = (user_id, email, password, first_name, last_name, address, city, state, zip_code, payment)
            query = "INSERT INTO User (userID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES (?,?,?,?,?,?,?,?,?,?)"
            self.cursor.execute(query, data)
            self.connection.commit()

            print("Successfully created a new account.")
            print()

        except sqlite3.Error as error:
            print("Failed to create account.", error)


    # login getter
    def getLoggedIn(self):
        return self.loggedIn

    # user ID getter
    def getUserID(self):
        return self.userID
