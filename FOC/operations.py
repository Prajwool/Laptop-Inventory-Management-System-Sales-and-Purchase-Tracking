def view_products(dict_of_products):
    print("S.N.  Name\t brand\t quantity \t price")
    for key,value in dict_of_products.items():
        print(str(key) +" "+ value[0] + "\t" + value[1] +"\t" + str(value[2]) +"\t"+ str(value[3]))

def generate_sell_note(name,phone_number,user_purchased_laptops,shipping_cost,total,grand_total):
    sell_note = "Mathi ko text"
    sell_note += "\nName of customer:" + name
    sell_note += "\nPhone number: " + str(phone_number)
    sell_note += "\nS.N.  Name \t Quantity\t Unit Price \t Total Price\n"
    for index in range(len(user_purchased_laptops)):
        sell_note += str(index+1) + user_purchased_laptops[index][0] +"\t"+ str(user_purchased_laptops[index][1])+"\t"+ str(user_purchased_laptops[index][2]) + "\t"+str(user_purchased_laptops[index][3])
    sell_note += "\nTotal before shipping" + str(total)
    sell_note += "\nShipping Cost: " + str(shipping_cost)
    sell_note += "\nTotal after shipping: " + str(grand_total)
    return sell_note


def generate_buy_note(name,phone_number,user_purchased_laptops,total):
    buy_note = "Mathi ko text"
    buy_note += "\nName of customer:" + name
    buy_note += "\nPhone number: " + str(phone_number)
    buy_note += "\nS.N.  Name \t Quantity\t Unit Price \t Total Price\n"
    for index in range(len(user_purchased_laptops)):
        buy_note += str(index+1) + user_purchased_laptops[index][0] +"\t"+ str(user_purchased_laptops[index][1])+"\t"+ str(user_purchased_laptops[index][2]) + "\t"+str(user_purchased_laptops[index][3])
    buy_note += "\nTotal before VAT" + str(total)
    buy_note += "\nVAT: " + str(int(0.13*total))
    buy_note += "\nTotal after VAT: " + str(int(1.13*total))
    return buy_note



