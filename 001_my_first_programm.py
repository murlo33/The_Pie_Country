
DataBase = {}

def add_data():
    '''A  Add data in DataBase'''
    '''need to add,  key == int()'''
    DataBase[input("Enter new search-key: ")] = input("Enter new data: ")
    print("Sucсess!")
    print_text()
    
def search_in_data():
    '''S '''
    print("Enter search-key:")
    key_s = input()
    if key_s in DataBase:
        print(DataBase[key_s])
    elif not key_s in DataBase:
        print("No such search-key")
    print_text()

def delete_data(): #not realesed
    '''D not released'''
    print_text()
    
def list_key():
    '''L Print full Database need fix for print only "key" '''
    print(DataBase[i], "\n")
    print_text()
    
    
def list_full_database(): #not released
    '''F  not released'''
    print(DataBase)
    input()
    print_text()
    

def print_text():
    print("If you want check your data:")
    print("Enter key: [A]dd key to [S]earch in the [L]ist or [E]xit")
    
print_text()

while True:
    button = input().upper()
    if button == "A":
        add_data()

    elif button == "S":
        search_in_data()

    elif button == "D":
        delete_data()

    elif button == "L":
        list_full_database()

    elif button == "E":
        break 
    elif not button == "A S D L E":
        print("\nUnkdown key\n")
        print_text()



