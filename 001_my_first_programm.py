
DataBase = {}

def add_data():
    '''add data in DataBase'''

    DataBase[input("Enter new key: ")] = input("Enter new data: ")
    print_text()
    
def search_in_data():
    print_text()

def delete_data():
    print_text()
    
def check_list_data():
    print_text()
    pass

def list_full_database():
    print_text()
    pass

def print_text():
    print("If you want check your data: \nPress: [A]dd [S]earch [K]ey to the [L]ist or [Q]uit")

print_text()

while True:
    key = input().upper()
    if key == "A":
        add_data()
    elif key == "S":
        search_in_data()
    elif key == "Q":
        break 
    elif key == "D":
        delete_data()
    elif key == "F":
        list_full_database()







