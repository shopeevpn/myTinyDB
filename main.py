import time
from tinydb import TinyDB, Query

with open('./db_location') as f:
    location = f.read()

data_base = TinyDB(location)



class TinyDatabase():
    def __init__(self):
        self.database = data_base
        self.lookup = Query() 
        self.site_name
        self.user_name
        self.password       


    def insertContent(self):
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

        
    def searchContent(self):
        pass

    def deleteContent(self):
        pass

    def showAllContent(self):
        print(self.database.all())    




def inputContent():
    ask = input("Multpile or Single input(m/s)\n : ")
    if(ask == "m"):
        ranger = int(input("How many: "))
        for x in range(ranger):
            TinyDatabase().insertContent()
    else:
        TinyDatabase().insertContent()


inputContent()