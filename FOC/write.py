import re

def update_products(dict_of_products):
    file=open("laptop.txt","w")
    for values in dict_of_products.values():
            file.write(str(values[0]+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])))
            file.write("\n")
    file.close()

def create_sell_note(sell_note, today_date_and_time, name):
      name_of_file = name + str(today_date_and_time).replace(":","_").replace(" ","_") +".txt"
      with open(name_of_file,"w") as file:
        file.write(sell_note)


def create_buy_note(buy_note, today_date_and_time, name):
      name_of_file = name + str(today_date_and_time).replace(":","_").replace(" ","_") + ".txt"
      with open(name_of_file,"w") as file:
        file.write(buy_note)










