import json
class Admin:
    def __init__(self):
        self.food_item={ }
        self.food_id=len(self.food_item)+1
    def add_new_food_item(self):
        self.name=input("Enter food name : ")
        self.quantity=int(input("Enter food quantity : "))
        self.price=int(input("Enter food price : "))
        self.stock=int(input("Enter food stock : "))
        self.discount=int(input("Enter food discount : "))
        self.item = {"Food name":self.name,"Food quantity":self.quantity,"Food price":self.price,"Food stock":self.price,"Food discount":self.discount}
        self.food_id=len(self.food_item)+1
        self.food_item[self.food_id]=self.item
        with open("Food_item.json","w") as f:
            json.dump(self.food_item,f)
        return self.food_item
    
    def view_food_item(self):
        return(list(self.food_item.items()))
    def edit_food_item(self):
        self.food_item[1]["Food name"]="Tandoori chicken"
        self.food_item[1]["Food quantity"]="4"
        self.food_item[1]["Food price"]="240"
        self.food_item[1]["Food stock"]="50"
        self.food_item[1]["Food discount"]="5"
        return(self.food_item)
    
    def remove_food_item(self):
        food_item = int(input("Enter the food item : "))
        del self.food_item[food_item]
        print("Remaining food item is : ",self.food_item)
        with open("Food_item.json","w") as f:
            json.dump(self.food_item,f)
        return self.food_item

c=Admin()
print(c.add_new_food_item())
print(c.add_new_food_item())
print(c.add_new_food_item())
print(c.add_new_food_item())

print("*"*100)
print("List of food items : ",c.view_food_item())
print("*"*100)
print(c.edit_food_item())
print("*"*100)
print("List of food items : ",c.view_food_item())
print("*"*100)
print(c.remove_food_item())
print("Remaining food item is : ",c.view_food_item())
