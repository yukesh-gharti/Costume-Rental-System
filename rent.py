import datetime
costume_dic = {}
item_rent=[]
item_brand=[]
item_price =[]

def costume_rent():
    #This is used to count the data in dictionary
    print("---------------------------------------------------------------------------")
    print(" ID \t Costume Name \t Costume Brand \t Price \t Quantity")
    print("---------------------------------------------------------------------------")

        
    #Creating a file variable to open MainStock text file in read mode
    file = open("MainStock.txt", "r")
    
    #Creating the variable to store the file in here for reading the all content
    costume_data = file.read()
    file.close()

    #now splitting the number of string and putting them in a list of variable costume_data
    costume_data = costume_data.split("\n")

    
    #For removing the empty list we use the while loop
    while("" in costume_data):
        costume_data.remove("")
        
    for i in range(len(costume_data)):
        #for checking the empty list
        if costume_data[i] != []:
            costume_dic[i+1] = costume_data[i].split(",")
    display()

    
def display():
    for key,value in costume_dic.items():
        print(key,end="\t")
        for i in value:
            print(i,end="\t")
        print("\n")
    print("----------------------------------------------------------------------------")
    validate()

def validate():
    success = False
    while success == False:
        Costume_id = int(input("Enter the ID of costume you want to rent: "))
        if Costume_id > 0 and Costume_id <= len(costume_dic):
            print("Costume Id is ",Costume_id)
            print("++++++++++++++++++++")
            print("Costume is available")
            print("++++++++++++++++++++")
            qty = int(input("Enter the quantity of costume:"))
            quantity_validate(qty,Costume_id)
            success = True
        else:
            print("Please provide a valid costume ID!!!:")
            break 
    
def quantity_validate(qu,c_id):
    quantity = qu
    Costume_id = c_id
    selected_item = costume_dic[Costume_id]
    if quantity <= int(selected_item[3]):
        selected_costume = costume_dic[Costume_id]
        update_qty = int(selected_costume[3])-quantity
        selected_costume[3] =str(update_qty)
        print(quantity)
        item_rent.append(selected_item[0])
        item_brand.append(selected_item[1])
        item_price.append(float(selected_item[2].strip().strip("$"))*quantity)
        print(costume_dic)
        stock_update()
        loop = True
        while (loop == True):
            choice =input("please enter 'y' if costumer rent another costume from the rental shop: ")
            if choice == 'y':
                costume_rent()
                loop=False
            else:
                name = input("name of costumer")
                print("")
                generate_bill(name)
                
                loop = False        
        else:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            
            

            

def generate_bill(name):
    crdt=datetime.datetime.now()
    y=str(crdt.year)
    m=str(crdt.month)
    d=str(crdt.day)
    h=str(crdt.hour)
    mi=str(crdt.minute)
    s=str(crdt.second)
    newcrdt = y+"-"+m+"-"+d+" "+h+":"+mi+":"+s
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                       Bill Details                                 ")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("The name of the costumer is: ",name)
    print("Date and time borrow by the customer is: ",newcrdt)
    print("Costume Item which are rented are:",item_rent)
    print("Costume brand are: ",item_brand)
    print("The total bill is: $",sum(item_price))

    try:

        file_name = y+m+d+h+mi+s+"_rent.txt"
        bill = open(file_name,"w")
        bill.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
        bill.write("\t \tBill Details \n")
        bill.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
        bill.write("Customer Name : "+str(name)+"\n")
        Rented_item=(",".join(item_rent))
        bill.write("Rented Items : " +str(Rented_item)+"\n")
        brand_item = (",".join(item_rent))
        bill.write("Brand Items are :" +str(brand_item)+"\n")
        bill.write("Date and time borrow by the customer: "+newcrdt+"\n")
        total_price = str(sum(item_price))
        bill.write("The total bill of the customer price: $"+total_price+"\n")
        bill.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
        bill.close()
    except Exception as e:
        print(e)
    
def stock_update():
    print("++++++++++++++++++++++++++++++++++++++")
    print("**************************************")
    print("           Stock updated              ")
    print("**************************************")
    print("++++++++++++++++++++++++++++++++++++++")
    file = open("MainStock.txt","w")
    for value in costume_dic.values():
          string = (",".join(value))
          file.write(string)
          file.write("\n")
    file.close()

#costume_rent()










