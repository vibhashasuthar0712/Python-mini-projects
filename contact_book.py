"""mini project-Contact Book Dictionary"""

contact={}
while True:
    print("\noption:\n1.add\n2.view all\n3.search\n4.delete\n5.exit")
    choice=input("enter your choice:")

    if choice=='1':
        name=input("name:")
        phone=int(input("number:"))
        contact[name]=phone
        print("contact saved!!")

    elif choice=='2':      
        for name,phone in contact.items():
            print(f"{name}:{phone}")


    elif choice=='3':
        name=input("search name:")
        if name in contact:
            print(f"{name}'s phone:{contact[name]}")
        else:
            print("contact not found.")


    elif choice=='4':
        name=input("search name to delete:")
        if name in contact:
            del contact[name]
            print("deleted successfully!")

    elif choice=='5':
        break
    else:
        print("invalid choice.")    
 