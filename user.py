import json
class User:
    def __init__(self):
        self.user_reg = { }
        self.user_id=len(self.user_reg)+1
    def new_registration(self):
        self.Fullname=input("Enter user Fullname : ")
        self.Phonenumber=int(input("Enter user Phonenumber : "))
        self.email=input("Enter user email id : ")
        self.address=input("Enter user address : ")
        self.password=input("Enter user password : ")
        self.info={"User name":self.Fullname,"phone number":self.Phonenumber,"Email id":self.email,"Address":self.address,"Password":self.password}
        self.user_id=len(self.user_reg)+1
        self.user_reg[self.user_id]=self.info
        with open("User_info","w") as f:
            json.dump(self.user_reg,f,indent=2)
            print("*"*10,"User registration complete","*"*10)
        return self.user_reg
    def user_login(self):
        self.login_email=input("Enter login email : ")
        self.login_password=input("Enter login password : ")
        if self.login_email==self.email and self.login_password==self.password:
                print("*"*50,"LOGIN WAS SUCCESSFULL","*"*50)
        else:
            print("*"*50,"Incorrect email or password","*"*50)
        return("*"*50,"WELCOME TO ZOTO APP","*"*50)
    
s=User()
print(s.new_registration())
print(s.user_login())

while True:
    print("*"*100)
    print("Press P -- for place new order")
    print("Press O -- for order history")
    print("Press U -- for Update Profile")
    print("Press T -- for exit")
    print("*"*100)
    option = input("choose your option : ")
    if option == "P"  or option == "p":
        print("Place new order")
        with open("Food_item.json","r") as f:
            menu=json.load(f)
            print(menu)
            k = 3
            res = dict(list(menu.items())[0:k])
            print("Selected items from menu : "+ str(res))
    elif option == "O" or option == "o":
        print("Get order history : "+ str(res))
    elif option == "U" or option == "u":
        print("Update profile")
        jsonFile=open("User_info","r+")
        data=json.load(jsonFile)   
        tmpn = data["1"]
        data["1"]={"User name": "Sudarshan Shinde", "phone number": 9380732737, "Email id": "shindesudarshan58@gmail.com", "Address": "New Adarsh ColonyBIDAR", "Password": "sud000100"}
        jsonFile.write(json.dumps(data))
        print("*"*50,"USER DATA UPDATED","*"*50)
    elif option =="T" or option == "t":
        print("THANKYOU FOR ORDERING")
        break
    else:
        print("Please enter correct choice")