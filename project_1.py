def New_Vehicle():
    print ("\n ====== New Vehicle Registration ====== \n")
    return 0
    
def Auto_Transaction():
    print ("\n ====== Auto Transaction ====== \n")
    
    
def Driver_Licence_Registration():
    print ("\n ====== Driver Licence Registration ====== \n")    

    
def Violation_Record():
    print ("\n ====== Violation Record ====== \n")

    
def Search_Engine():
    print ("\n ====== Search Engine ====== \n")
    

def main():
    #Systemnumber = input("ask");

    status = False   
    
    while (status == False):
        Systemnumber = input("ask");
        
        if (Systemnumber == "1"):
            #go to New Vehicle Registration
            New_Vehicle()
            continue
        elif (Systemnumber == "2"):
            Auto_Transaction()
        elif (Systemnumber == "3"):
            Driver_Licence_Registration()
        elif (Systemnumber == "4"):
            Violation_Record()
        elif (Systemnumber == "5"):
            Search_Engine()
        elif (Systemnumber.lower() == "exit"):
            print ("Exit the system")
            break
        else : 
            print ("invalid input please try again")
            


main()