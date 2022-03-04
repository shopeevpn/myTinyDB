import time
from tinydb import TinyDB, Query

with open('C:\\Users\\USER\\Desktop\\PROJECTS\\python\\python-1\\database\\tinydb\\db_location') as f:
    location = f.read()

data_base = TinyDB(location)


class TinyDatabase():
    def __init__(self):
        self.database = data_base
        self.lookup = Query()

    def insert_content(self):
        self.site_name = input("Sitename: ")
        self.user_name = input("Username: ")
        self.password = input("Password: ")

        self.database.insert(
            {
                'Site': self.site_name,
                'User': self.user_name,
                'Password': self.password
            }
        )
        for l in range(1):
            print()
            print("*"*20)
            time.sleep(0.5)

    def search_content(self):
        
        self.search_site = input("Enter sitename: ")
        print(self.database.search(self.lookup.Site == self.search_site))

    def delete_content(self):
        print("*"*30)
        print("Deletes user and related info")
        print("*"*30)
        self.delete_user = input("Enter username: ")
        self.database.remove(self.lookup.User == self.delete_user)
        print("Deleted <",self.delete_user,">")   

    def show_all_content(self):
        print(self.database.all())


def input_content():
    ask = input("Multpile or Single input(m/s)\n~$ ")
    if(ask == "m"):
        amount = int(input("How many: "))
        for x in range(amount):
            TinyDatabase().insert_content()
    else:
        TinyDatabase().insert_content()