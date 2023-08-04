import rent
import returned
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("*************************************************************************")
print("           Welcome to costome rental application                          ")
print("*************************************************************************")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n")

def main():
    #providing the heading text for output.
    while(True):
        try:
            print("Select the desirable option")
            print("(1) || Press 1 to rent a costume.")
            print("(2) || Press 2 to return a costume.")
            print("(3) || Press 3 to exit.")
            options = int(input("Choose the options (1,2,3) : "))
            print("\n")
            if options == 1:
                print("Let's rent a costume.")
                rent.costume_rent()
                print("\n")
                

            elif options == 2:
                print("Let's return a costume.")
                returned.costume_return()
                print("\n")

            elif options == 3:
                print("\t******************************************************************************")
                print("\t Hope you like our costume rental application.Thanks for using our application")
                print("\t******************************************************************************")
                break
            else:
                print("Invalid input has entered!!!")
                print("Please select the appropriate given value.")
                print("\n")
        except:
            print("Please provide the valid input")
    

main()

            
            
        
        
