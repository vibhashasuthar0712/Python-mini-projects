"""mini project:grocery list manager!!"""

grocery_list=[]
while True:
 print("\noption:add/remove/show/exit")
 action=input("what you would like to do?\n ")

 if action=="add":
  item=input("enter item to add:")
  grocery_list.append(item)
  print(f"{item}added.")



 elif action=="remove":
  item=input("enter the item which you want to remove:")
  if item in grocery_list:
       grocery_list.remove(item)
       print(f"{item} removed.")
  else:
   print("item not found!!")



 elif action=="show":
  print("YOUR GROCERY LIST:")
  for item in grocery_list:
    print(item)
    
 
 elif action=="exit":
   print("--------------THANK YOU!! VISIT AGAIN------------")
   break
   
 else:
   print("invalid option!!") 

