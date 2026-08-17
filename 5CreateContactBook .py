import time
contacts={}
seconds = 2
while True :
    print("-----------")
    print("   MENU")
    print("-----------")

    print("  CONTACTS")
    print("   VIEW")
    print("   EXIT")
 
    select = input("select what u want (contacts:view:exit): ")
    if select == "contacts" :
            print("create contacts")
            name=input("enter contact name: ")
            phone = int(input("enter nummber: "))
            contacts[name] = phone
            time.sleep(seconds)
            print("contact added ✅")

    elif select == "view":
          print("U selected view contacts")
          print(contacts)
          time.sleep(seconds)

    elif select == "exit":
            break 

print(contacts)