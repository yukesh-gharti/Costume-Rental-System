import datetime
dic ={}
costume_name = []
costume_brand = []
costume_price = []
costume_quantity = []

def costume_return():
    print("---------------------------------------------------------------------------")
    print(" ID \t Costume name \t Costume Brand \t Price \t Quantity")
    print("---------------------------------------------------------------------------")
    file = open("MainStock.txt","r")
    costume_list = file.read()
    file.close()
    costume_list = costume_list.split("\n")

    while("" in costume_list):
        costume_list.remove("")

    for i in range(len(costume_list)):
        if costume_list != []:
            dic[i+1] = costume_list[i].split(",")
        else:
            print("Costume_list is in the list form and not in dictionary form")
    display()
        
def display():
    for key,value in dic.items():
        print(key,end="\t")
        for i in value:
            print(i,end="\t")
        print("\n")
    print("---------------------------------------------------------------------------")
    validate()

def validate():
    victory = True
    while victory == True:
        ID_costume = int(input("Enter the id of the costume you want to return: "))
        if ID_costume > 0 and ID_costume <= len(dic):
            print("The costume id is: ",ID_costume)
            print("+++++++++++++++++++++++++++++++++++++++"+"\n")
            print("***************************************"+"\n")
            print("Costume is available in the rental shop"+"\n")
            print("***************************************"+"\n")
            print("+++++++++++++++++++++++++++++++++++++++"+"\n")
            print("\n")
            quty = int(input("Enter the number of quantity you want to return: "))
            quantity_validation(quty,ID_costume)
            victory = False
        else:
            print("------------------------------------------------------------")
            print("Please enter the valid id of the costume you want to return.")
            print("------------------------------------------------------------")
            
def quantity_validation(qu,ci):
    quantity = qu
    ID_costume = ci
    item_select = dic[ID_costume]
    if quantity <= int(item_select[3]):
        item_costume = dic[ID_costume]
        update_quantity = int(item_costume[3])+quantity
        item_costume[3] = str(update_quantity)
        print(item_costume)
        print(dic)
        costume_name.append(item_costume[0])
        costume_brand.append(item_costume[1])
        costume_price.append(float(item_costume[2].strip().strip("$"))*quantity)
        costume_quantity.append(float(item_costume[3]))
        
        stock_update()
        loopp = True
        while loopp == True:
            choices = input("Please enter 'y' to return the another costume again")
            if choices == "y":
                costume_return()
                break
            else:
                name = input("Enter the name of the customer: ")
                '''
                days = int(input("Enter the number of days if the customer is late for submission: "))
                cost_price = sum(costume_price)
                cos_price = cost_price
                print(cos_price)
                #if the customer return the costume item in 5 days then
                if days <= 5 and days > 0:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("********************************************************")
                    print("               The custome is returned                  ")
                    print("********************************************************")
                #if the customer return the costume item after 5 days then fine should be added
                else:
                    fine = (cos_price/5)*days
                    print("Customer return the costume after 5 days and the fine will be: $",str(fine))
                '''
                days = int(input("Enter the number of days if the customer is late for submission: "))
                cost_price = sum(costume_price)
                cos_price = cost_price
                fine = (cos_price/5)*days
                generate_bill(name,fine,days)
                break
                

def generate_bill(name,fine,days):
    cudt = datetime.datetime.now()
    y = str(cudt.year)
    m = str(cudt.month)
    d = str(cudt.day)
    h = str(cudt.hour)
    mi = str(cudt.minute)
    s = str(cudt.second)
    newcudt = y+"-"+m+"-"+d+" "+h+":"+mi+":"+s
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("*******************************************************")
    print("                   Bill details                        ")
    print("*******************************************************")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("The date and time returned by the customer is: " , newcudt)
    print("The name of the customer is : ",name)
    print("Costume item which is being return are : ",costume_name)
    print("Costume brand which are : ",costume_brand)
    print("The total bill price of the customer is : $",sum(costume_price))
    print("quantity of costume: ",str(costume_quantity))
    
    
    #days = int(input("Enter the number of days if the customer is late for submission: "))
    #if the customer return the costume item in 5 days then
    days = days
    
    if days <= 5 and days > 0:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("********************************************************")
        print("               The custome is returned                  ")
        print("********************************************************")
    #if the customer return the costume item after 5 days then fine should be added
    else:
        #fine = (cos_price/5)*days
        fine = fine
        print("Customer return the costume after 5 days and the fine will be: $",str(fine))
    
    try:
        file_name = y+m+d+h+mi+s+"_return.txt"
        bill = open(file_name,"w")
        bill.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+"\n")
        bill.write("***********************************************************************"+"\n")
        bill.write("                         Bill Details                                  "+"\n")
        bill.write("***********************************************************************"+"\n")
        bill.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+"\n")
        bill.write("The name of the customer is: "+str(name)+"\n")
        returned_item = (",".join(costume_name))
        bill.write("Returned item name is: "+str(returned_item)+"\n")
        brand_item = (",".join(costume_brand))
        bill.write("brand items are: "+str(brand_item)+"\n")
        bill.write("Date and time returned by the customer is: "+str(newcudt)+"\n")
        total_price = sum(costume_price)
        bill.write("The total price of the customer is : $"+str(total_price)+"\n")
        bill.write("The quantity of the customer is : "+str(costume_quantity)+"\n")
        bill.write("The total price and fine with of the customer is: $"+str(fine)+"\n")
        bill.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)

   
       
        
def stock_update():
    print("++++++++++++++++++++++++++++++++++++")
    print("************************************")
    print("           stock update             ")
    print("************************************")
    print("++++++++++++++++++++++++++++++++++++")
    file = open("MainStock.txt","w")
    for value in dic.values():
        string = (",".join(value))
        file.write(string)
        file.write("\n")
    file.close()
        



        
    






costume_return()
