
S = {"pie", "cream", "ice"} #set(множество)
S.add("coffe") 
D = {"key1": 333, "key3": 222, 1: "pizza"} #dict словарь
D["key4"] = 555
spisok = ["meat", "cake"] #список
spisok.append("sake")

#print(S)
print(D)
#print(spisok)

print("If you want check your dict: \nPress: [A]dd [S]earch [K]ey to the [L]ist or [E]xit")
#for key in D:
while True:

    if input().upper == "A":
        D[input("Enter new key: ")] = input("Enter new data: ") 
    
print(D)


#    elif input().upper == "S":
#        input("Enter key: ") in D:
#        print("You data: ", D[key]),


#    elif input().upper == "K":
#        print(D[key]),


#    elif input().upper() == "L":
#        print(D),


 #   elif input().upper == "E":
 #       print("No code"),

   
        
    #else input("Enter key: ") in D:
    #    print("You data:", D[key])
        
    #elif:
    #    D[input("Enter new key: ")] = input("Enter new data: ")
    #elif:



#def entxt():
    
#D[input("new key: ")] = input("new data: ") 