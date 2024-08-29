import read
import operations
import write
import datetime

print("\n")
print("\t\t\t\t\t Welcome to AI1")
print("\t\t\t\t\t Address : Skill Lab")
print("\t\t\t----------------------------------------------------")
print("\t\t\t\tPlease select any of below option")
print("\t\t\t----------------------------------------------------")

continueLoop = True
while continueLoop:
    dict_of_products = read.read_products()
    print("\n")
    print("Press 1 to sell to customer")
    print("Press 2 to buy from manufacturer ")
    print("press 3 to exit from program")
    print("\n")
    userinput = int(input("Press from the above mentioned option"))
    if userinput == 1:
        name = (input("Enter your name"))
        phone_number = int(input("Enter your number"))
        continue_selling = True
        user_purchased_laptops = []
        while continue_selling:
            operations.view_products(dict_of_products)
            valid_id = int(input("Please provide the iD of the laptop you want to sell"))  
            print("\n")
            while valid_id <= 0 or valid_id > len(dict_of_products):
                print("Please provide a valid Laptop ID !!!")
                print("\n")
                valid_id=int(input("Please provide the iD of the laptop you want to buy:"))
            user_quantity=int(input("Please provide the number of quantity of the laptop you want to buy:"))
            print("\n")
            get_quantity = dict_of_products[valid_id][3]
            while user_quantity <= 0 or user_quantity > int(get_quantity):
                print("Dear Admin, the quantity you looking for is not available ")
                print("\n")
                user_quantity = int(input("Please Provide the number of quantity of laptop "))
            dict_of_products[valid_id][3]=int(dict_of_products[valid_id][3])-int(user_quantity)
            name_of_product = dict_of_products[valid_id][0]
            quantity_selected_by_user = user_quantity
            unit_price = dict_of_products[valid_id][2]
            price_of_selected_item = dict_of_products[valid_id][2].replace("$",'')
            total_price = int(price_of_selected_item)*int (quantity_selected_by_user)
            user_purchased_laptops.append([name_of_product, quantity_selected_by_user, unit_price, price_of_selected_item, total_price])
            wantMore = input("Do you want to continue?(y/n)").upper()
            if wantMore == "N":
                continue_selling = False
                write.update_products(dict_of_products)
        shipping = input ("Dear user do you want your laptop to be shipped?(y/n)").upper()
        if shipping == "Y":
            shipping_cost = 500
        else:
            shipping_cost = 0
        total=0
        for i in user_purchased_laptops:
            total+=int(i[3])
        grand_total = total+shipping_cost
        today_date_and_time = datetime.datetime.now()
        sell_note = operations.generate_sell_note(name,phone_number,user_purchased_laptops,shipping_cost,total,grand_total)
        write.create_sell_note(sell_note, today_date_and_time, name)
    elif userinput == 2:
        name = (input("Enter the manufacturer's name:"))
        phone_number = int(input("Enter the manufacturer's phone number:"))
        continue_buying = True
        user_purchased_laptops = []
        while continue_buying:
            operations.view_products(dict_of_products)
            valid_id = int(input("Please provide the iD of the laptop you want to buy"))  
            print("\n")
            while valid_id <= 0 or valid_id > len(dict_of_products):
                print("Please provide the ID of the laptop you want to buy:")
                print("\n")
                valid_id=int(input("Please provide the ID of the laptop you want to buy:"))
            user_quantity=int(input("Please provide the number of laptops you want to buy:"))
            print("\n")
            get_quantity = dict_of_products[valid_id][3]
            while user_quantity <= 0 or user_quantity > int(get_quantity):
                print("Sorry, the quantity you are looking for is not available")
                print("\n")
                user_quantity = int(input("Please Provide the number of quantity of laptop "))
            dict_of_products[valid_id][3]=int(dict_of_products[valid_id][3])-int(user_quantity)
            name_of_product = dict_of_products[valid_id][0]
            quantity_selected_by_user = user_quantity
            unit_price = dict_of_products[valid_id][2]
            price_of_selected_item = dict_of_products[valid_id][2].replace("$",'')
            total_price = int(price_of_selected_item)*int (quantity_selected_by_user)
            user_purchased_laptops.append([name_of_product, quantity_selected_by_user, unit_price, price_of_selected_item, total_price])
            wantMore = input("Do you want to continue?(y/n)").upper()
            if wantMore == "N":
                continue_buying = False
                write.update_products(dict_of_products)
      
        total=0
        for i in user_purchased_laptops:
            total+=int(i[3])
       
        today_date_and_time = datetime.datetime.now()
        buy_note = operations.generate_buy_note(name,phone_number,user_purchased_laptops,total)
        write.create_buy_note(buy_note, today_date_and_time, name)
    elif userinput==3:
        continueLoop = False
    else:
        print("Check option and continue")

print("Thanks for using the program!")






      