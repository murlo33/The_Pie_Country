
DataBase = {}

def add_data():
    '''A  Add data in DataBase'''
    '''need to add,  key == int()'''
    DataBase[input("Enter new number key: ")] = input("Enter new data: ")
    print("Sucсess!")
    print_text()
    
def search_in_data():
    '''S '''
    print_text()

def delete_data():
    '''D '''
    print_text()
    
def list_key():
    '''L '''
    print(DataBase[i], "\n")

    print_text()
    
    
def list_full_database():
    '''F  not used'''
    print(DataBase)
    input()
    print_text()
    

def print_text():
    print("If you want check your data:")
    print("Enter key: [A]dd key to [S]earch in the [L]ist or [E]xit")
    
print_text()

while True:
    key = input().upper()
    if key == "A":
        add_data()

    elif key == "S":
        search_in_data()

    elif key == "D":
        delete_data()

    elif key == "L":
        list_full_database()

    elif key == "E":
        break 
    elif not key == "A S D L E":
        print("\nUnkdown key\n")
        print_text()



