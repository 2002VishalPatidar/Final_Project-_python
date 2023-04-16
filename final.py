import json
 
filename="Fooditem.json"
fileuser="Userdata.json"
def  addfood_item():
    item_data={}
    with open(filename,"r")as f :
      temp=json.load(f) 
    item_data["Id"]=int(input("Id of item:") )
    item_data["Name"]=(input("name of item:") )
    item_data["price"]=int(input("price of item:") )
    item_data["Discount"]=int(input("Discount of item:") )
    item_data["Stock"]=int(input("Stock of item:") )
    temp.append(item_data)
    with open (filename,"w") as f:
     json.dump(temp,f,indent=4)


def editfood_item():
    view_fooditem()
    new_data = []
    with open(filename,"r")as f :
     temp=json.load(f)
    data_length=len(temp)-1
    print("which index number would you like to edit")  
    edit_option=input(f"Select a number 0-{data_length}:")
    i=0
    for entry in temp:
      if i == int(edit_option):
        Id=entry["Id"]
        Name=entry["Name"]
        price=entry["price"]
        Discount=entry["Discount"]
        Stock=entry["Stock"]
        

        print(f"Current ID:{Id}")
        Id= int(input("What would you like the new Id to be?"))
        print(f"Current Name:{Name}")
        Name= input("What would you like the new Name to be?")
        print(f"Current price:{price}")
        price= int(input("What would you like the new price to be?"))
        print(f"Current Discount:{Discount}")
        Discount= int(input("What would you like the new Discount to be?"))
        print(f"Current Stock:{Stock}")
        Stock= int(input("What would you like the new Stock to be?"))
        
        new_data.append({"Id":Id,"Name":Name,"price":price,"Discount":Discount,"Stock":Stock})
        i=i+1
      else:
        new_data.append(entry)
        i=i+1
      with open(filename,"w") as f:  
       json.dump(new_data,f,indent=4)     
def view_fooditem() :
    with open(filename,"r")as f:
     temp=json.load(f)
     i=0
     for entry in temp:
      Id=entry["Id"]
      Name=entry["Name"]
      price=entry["price"]
      Discount=entry["Discount"]
      Stock=entry["Stock"]
      print(f"Index Number{i}")
      print (f"id:{Id}")
      print (f"Name:{Name}")
      print (f"price:{price}")
      print (f"Discount:{Discount}")
      print (f"Stock:{Stock}")
      print ("\n\n")
      i=i+1
def deletefood_item(food_id):
    file=open(filename,"r+")
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Id"] == food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content,file,indent=4)
            file.close()
            return "sucess"
    return "please Enter valid food_id"
def adduser_data():
   user_data={}
   with open(fileuser,"r")as f :
     temp=json.load(f) 
     user_data["id"]=int(input("Id of user:") )
     user_data["Name"]=(input("name of user:") )
     user_data["password"]=(input("password of user:") )
     user_data["Age"]=(input("Age of user:") )
     user_data["Email"]=(input("Email of user:") )
     user_data["Address"]=(input("Address of user:") )
     user_data["phone_no"]=(input("phone of user:") )
     temp.append(user_data)
     with open (fileuser,"w") as f:
       json.dump(temp,f,indent=4)
       print("successful registration")
 



def user_place_order(user_id, food_name, quantity):
    global count
    file = open(fileuser, "r+")
    content = json.load(file)
    file1 = open(filename, "r+")
    content1 = json.load(file1)
    flag=0
    food_price=0
    for i in range(len(content1)):
        if content1[i]["Name"] == food_name:
            if content1[i]["Stock"] >= quantity:
                for j in range(len(content)):
                    if content[j]["id"] == user_id:
                        content1[i]["Stock"]-=quantity
                        food_price=content1[i]["price"]*quantity
                        
                        food_price=content1[i]["price"]*quantity
                        print("Food_price:",food_price)
                else:
                    
                    flag=1
                    food_price=content1[i]["price"]*quantity
                    print("Food_price:",food_price)
            else:
                print("Pls Enter less quantity")
                break   
    if flag==0:
        print("Order Not Available")
    elif(flag==1):
        print("Be Ready For Your Order") 
        if food_price>100:
            food_price_with_discount=food_price*0.2
            food_price=food_price-food_price_with_discount
            print("Congratulation you got 20 percent discount on Order paid only:",food_price,"rs")
        else:
            print("Sorry NO Dicount")

    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()

    file1.seek(0)
    file1.truncate()
    json.dump(content1, file1, indent=4)
    file1.close()


def user_Order_History(user_id):
    file=open(fileuser,"r+")
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["id"]==user_id:
            print("order history")
            print("Date | Order")
            for i,j in content[i]["order history"].items():
                print(f"{i} | {j}")
            file.close()
            return True
    return False

def edituserprofile_data():
  new_data = []
  with open(fileuser,"r")as f :
      temp=json.load(f)
      data_length=len(temp)-1
  print("which index number would you like to edit")  
  edit_option=input(f"Select a number 0-{data_length}:")
  i=0
  for entry in temp:
      if i == int(edit_option):
        id=entry["id"]
        Name=entry["Name"]
        password=entry["password"]
        Age=entry["Age"]
        Email=entry["Email"]
        Address=entry["Address"]
        phone_no=entry["phone_no"]
        print(f"Current ID:{id}")
        id= int(input("What would you like the new Id to be?"))
        print(f"Current Name:{Name}")
        Name= input("What would you like the new Name to be?")
        print(f"Current password:{password}")
        password= ( input("What would you like the new password to be?"))
        print(f"Current Age:{Age}")
        Age= (input("What would you like the new Age to be?"))
        print(f"Current Email:{Email}")
        Email= (input("What would you like the new Email to be?"))
        print(f"Current Adrress:{Address}")
        Address= input("What would you like the new Address to be?")
        print(f"Current phone_no:{phone_no}")
        phone_no= input("What would you like the new phone_no to be?")
        
        new_data.append({"id":id,"Name":Name,"password":password,"Age":Age,"Email":Email,"Address":Address,"phone_no":phone_no})
        i=i+1
      else:
        new_data.append(entry)
        i=i+1
  with open(fileuser,"w") as f:  
      json.dump(new_data,f,indent=4)  


choice=input("Enter the Online food orderining System y/n : ")

while choice =="y":
    print("MENU :")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
    option1=input("choose one value from the above : ")
    if option1=="1":
        adduser_data()
    elif option1== "2":
        print("Login")
        while True:
            print("1)User")
            print("2)Admin")
            print("3)Exit")
            option2=input("choose on value from above")
            if option2 =="1":
                print("User login")
                user=input("Enter Name :")
                password=input("Enter the Password :")
                file=open("Userdata.json","r+")
                content=json.load(file)
                flag=0 
                for i in range(len(content)):
                    if content[i]["Name"]==user:
                        if content[i]["password"]==password:
                            flag=1
                            while True:
                                print()
                                print("Please View the Menu Before Place The Order")
                                print("PLEASE, PLACE THE ORDER MORE THAN 100/- TO GET 15% DISCOUNT")
                                print("1) View Menu")
                                print("2) Place Order")
                                print("3) History of food_order")
                                print("4) Update Profile")
                                print("5) Exit")
                                option3=input("User Enter Your Choice :")
                                if option3=="1":
                                    view_fooditem()
                                elif option3=="2":
                                    print("Please Check the User_ID in User.json Then only put")
                                    user_id=int(input("Enter UserID :"))
                                    food_name=input("Enter the food want to eat :")
                                    quantity=int(input("enter the quantity of food :"))
                                    user_place_order( user_id, food_name, quantity)
                                elif option3=="3":
                                    user_id=int(input("Enter UserID :"))
                                    user_Order_History(user_id)
                                elif option3=="4":
                                    edituserprofile_data()
                                else:
                                    print("Thanks for the Visit")
                                    break

                if flag==0:
                    print("Please enter the correct USER NAME OR PASSWORD")     
            elif option2=="2":
                print("Admin")
                user=input("Enter Admin Name :")
                password=input("Enter the Password of Admin :")
                file = open("admin.json", "r+")
                content = json.load(file)
                if content["name"] == user:
                    if content["password"] == password:
                        while True:
                            print()
                            print("1) Add New Food")
                            print("2) Edit Food")
                            print("3) View Food")
                            print("4) Remove Food") 
                            print("5) Exit")
                            option4 = input("Enter Your Choice Admin!!")
                            if option4 =="1":
                                addfood_item()
                            elif option4 == "2":
                                editfood_item()
                            elif option4=="3":
                                view_fooditem()
                            elif option4=="4":
                                food_id=int(input("Enter a food id:"))
                                deletefood_item(food_id)
                            else:
                                file.close()
                                break
                    else:
                        print("Wrong Password!!")
                else:
                    print("Wrong Username!!")
            else:
                break
    else:                
        print("WELCOME")
 




   


