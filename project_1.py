import sys
import cx_Oracle
import getpass
from random import randint

def People_Information(curs,connection,sin):
    print ("\n ====== People Information ====== \n")
    
    while True:
        try:
            '''
            sin=input("Sin:")
            '''
            
            name = input("Name:")
            while True:
                try :
                    height = int(input("Height [cm]:"))            
                    if height < 1000 and height > 0:
                        break
                    else:
                        print ("Enter the exactly integer.")
                except:
                    print ("Enter the exactly integer.")
            while True:
                try:
                    weight = int(input("Weight [KG]:"))
                    if weight < 1000 and weight > 0:
                        break
                    else:
                        print ("Enter the exactly integer.")
                except:
                    print ("Enter the exactly integer.")
                
            eyecolor = input("Eyecolor: ")
            haircolor = input("Haircolor: ")
            addr = input("Address: ")
            genderinput = input("Gender [f or m]: ")
            gender=genderinput.lower()
            while gender != 'f' and gender != 'm':    #check
                print("Our system only accept the male and the female\n 'f' and 'm' only.")
                gender = input("Gender [f or m] ")                        
            birthday = input("birthday [DD-MMM-YYYY] ")
            while len(birthday) != 11 : #note the might error
                print("Invalid input, please try agian")
                birthday = input("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")      
            curStr = ("INSERT INTO PEOPLE VALUES('%s','%s',%s,%s,'%s','%s','%s','%s','%s')"
                              %(sin,name,height,weight,eyecolor,haircolor,addr,gender,birthday))  
            curs.execute(curStr)
            connection.commit()
            break
        #http://stackoverflow.com/questions/7465889/cx-oracle-and-exception-handling-good-practices
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print( sys.stderr, "Oracle code:", error.code)
            print( sys.stderr, "Oracle message:", error.message)
            print( "===== Data insertion is fail. Reinput the data again! =====")
    return 0    

    
   
def New_Vehicle(curs,connection):
    print ("\n ====== New Vehicle Registration ====== \n")
    status = True
    while True:
        try:
            while True:
                try:
                    s_serialno = ("SELECT SERIAL_NO FROM VEHICLE")
                    curs.execute(s_serialno)
                    lSerial_no = curs.fetchall()
                    listSerial_no = []
                    #print (lSerial_no)
                    for i in lSerial_no:
                        listSerial_no.append(i[0].strip())
                     
                    #listSerial_no is ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '3', '4', '5', '6', '7', '8', '9']
                    break
                except:
                    print("Invalid input, please try agian")
                else:
                    pass
                
            serial_no = input("Serial_no [within 20 number]:")
            while serial_no in listSerial_no or serial_no.split() == []:
                print ("That is not a valid input")
                serial_no = input("Serial_no [within 20 number]:")
            
            maker = input("Maker [within 20 Char]:")
            model = input("Model [within 20 Char]:")
            
            while True:
                try:
                    year = int(input("Year:"))
                    if year  <= 9999:
                        break
                    else:
                        print ("Not a valid input please enter a year less equal than 9999")
                        
                except:
                    print("Invalid input, please try agian")
                else:
                    pass
                
            colour = input("Colour:")
            
            while True:
                try:
                    s_typeid = ("SELECT TYPE_ID FROM VEHICLE")
                    curs.execute(s_typeid)
                    ltypeid = curs.fetchall()
                    listtypeid = []
                    print (ltypeid)
                    #print (lSerial_no)
                    for i in ltypeid:
                        if i[0] not in listtypeid:
                            listtypeid.append(i[0])
                     
                    #listSerial_no is ['1', '2']
                    break
                except:
                    print ("error")
            #print (listtypeid)
            while True:
                try:
                    type_id = int(input("Select a Type ID {} :".format(listtypeid)))
                    if type_id in listtypeid :
                        break
                except:
                    print ("Invalid input")
                else:
                    pass
            #print (type_id)   
            curStrvehicle = ("INSERT INTO VEHICLE VALUES('%s','%s','%s',%s,'%s',%s)"
                                          %(serial_no,maker,model,year,colour,type_id))    
            curs.execute(curStrvehicle)
            connection.commit()
                
            break
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print( sys.stderr, "Oracle code:", error.code)
            print( sys.stderr, "Oracle message:", error.message)
            print( "===== Data insertion is fail. Reinput the data again! =====")
        else:
            pass
    
        

    
    while True:
        try:
            s_sin = ("SELECT SIN FROM PEOPLE")
            curs.execute(s_sin)
            lsin = curs.fetchall()
            listsin = []
            for i in lsin:
                listsin.append(i[0].strip())
             
            #listSerial_no is ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '3', '4', '5', '6', '7', '8', '9']
            break
        except:
            print("Invalid input, please try agian")
        else:
            pass    
    
    sin = input("Sin:")
    if sin not in listsin:
        print ("This is a new Sin number")
        print ("Please register your personal information first====>>>>")
        print ("====== Loading ======")
        People_Information(curs,connection,sin)
    
    while True:
        try:
            owner_id = sin
            vehicle_id = serial_no
            is_primary_ownerinput = input("Is Primary Owner ?[y or n]: ")
            is_primary_owner=is_primary_ownerinput.lower()
            while is_primary_owner != 'y' and is_primary_owner != 'n':    #check
                print("Our system only accept the yes and no \n 'y' and 'n' only.")
                is_primary_ownerinput = input("Gender [f or m] ")                 
                is_primary_owner=is_primary_ownerinput.lower()
                
            curStrOwner = ("INSERT INTO OWNER VALUES('%s','%s','%s')"
                                          %(owner_id,vehicle_id,is_primary_owner))    
            curs.execute(curStrOwner)
            connection.commit()    
            break
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print( sys.stderr, "Oracle code:", error.code)
            print( sys.stderr, "Oracle message:", error.message)
            print( "===== Data insertion is fail. Reinput the data again! =====")
        else:
            pass
            
    print ("====== BACK TO THE MAIN MENUE ======")        
    return 0
    
def Auto_Transaction(curs,connection):
    print ("\n ====== Auto Transaction ====== \n")
    s_sin = ("SELECT SIN FROM PEOPLE")
    curs.execute(s_sin)
    lsin = curs.fetchall()
    listsin = []      
    for i in lsin:
        if i[0].strip() not in listsin:
            listsin.append(i[0].strip())    
            
    s_vehicle = ("SELECT SERIAL_NO FROM VEHICLE")
    curs.execute(s_vehicle)
    lvehicle = curs.fetchall()
    listvehicle = []
    for i in lvehicle:
        if i[0].strip() not in listvehicle:
            listvehicle.append(i[0].strip()) 
            
    s_transaction_id = ("SELECT SERIAL_NO FROM VEHICLE")
    curs.execute(s_transaction_id)
    ltransaction_id = curs.fetchall()
    listtransaction_id = []
    for i in ltransaction_id:
        if i[0].strip() not in listtransaction_id:
            listtransaction_id.append(i[0].strip())       
    
    
    print (listtransaction_id)
    print (listvehicle)
    print (listsin)  
    
    while True:
        try:
            seller_id = input("Seller_id:")
            if seller_id not in listsin:
                print ("The personal information is not register")
                print ("Please register the personal inforamtion first")
                People_Information(curs,connection,seller_id)
            break
        except:
            print ("Invalid seller_id input")
        else:
            pass
        
    while True:
        try:
            buyer_id = input("Buyer_id:")
            if buyer_id not in listsin:
                print ("The personal information is not register")
                print ("Please register the personal inforamtion first")
                People_Information(curs,connection,buyer_id)
            break
        except:
            print ("Invalid buyer_id input")
        else:
            pass    
    
    while True:
        try:
            vehicle_id = input("Vehicle id :")
            if vehicle_id not in listsin:
                print ("Please register the Vehicle first")
                goto = input("Do you want to go to New Vehicle system['y' or 'n'] \n 'n' Go To Main menu").lower()
                while goto !="y" and goto != "n":
                    goto = input("Do you want to go to New Vehicle system['y' or 'n'] \n 'n' Go To Main menu").lower()
                    
                if goto == "y":
                    New_Vehicle(curs,connection)
                elif goto == "n":
                    return 0          
            break
        except:
            print ("Invalid buyer_id input")
        else:
            pass      
    
    s_date = input("Seller Date [DD-MMM-YYYY] ")
    while len(s_date) != 11 : #note the might error
        print("Invalid input, please try agian")
        s_date = input("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")          
    
    while True:
        try:
            price = round(float(input("Price [0-999999]:")),2)
            if price < 100000000 and price > 0 :
                break
            else:
                print ("Invalid Price Input")
        except:
            print ("Invalid Price Input")
    
    getTraniD = input("Do you want to enter transaction_id?\n 'y' is enter an ID, 'n' is automatic get an id ").lower()
    while getTraniD != "y" and getTraniD != "n":
        getTraniD = input("Do you want to enter transaction_id?\n 'y' is enter an ID, 'n' is automatic get an id ").lower()
    if getTraniD == "y":
        while True:
            try:
                transaction_id = int(input("Transaction ID:" ))
                if transaction_id in listtransaction_id:
                    print ("The transaction id already exist, please input again")
                else:
                    break
            except:
                print ("Invalid transaction id input")
    else:
        while True:
            transaction_id = randint(0,10000)
            if transaction_id not in listtransaction_id:
                break
            else :
                print (transaction_id,"exist")
            
    print("Transaction ID: ",transaction_id)        
        
    curStr = ("INSERT INTO auto_sale VALUES(%s,'%s','%s','%s','%s','%s')"
                                      %(transaction_id,seller_id,buyer_id,vehicle_id,s_date,price))
    curs.execute(curStr)

    checkSelect = "DELETE FROM owner WHERE vehicle_id = '" + vehicle_id + "'"
    curs.execute(checkSelect)
    print ("The Original OnwnerShip deleted")
    
    is_primary_owner = 'y'
    curStr = ("INSERT INTO OWNER VALUES('%s','%s','%s')"%(buyer_id,vehicle_id,is_primary_owner))  
    curs.execute(curStr)
    print ("The new OnwnerShip added")
    
    while True:
            non_primary = input("Does this vehicle has more than one owner? Enter 'y' or 'n'\n")
            if non_primary.lower() == 'y':
                nonprimarysin = input("Non-primary Owner Sin : ")
                if nonprimarysin not in listsin:
                    People_Information(curs,connection,nonprimarysin)
                    
                try:
                    is_primary_owner = 'n'
                    curStr = ("INSERT INTO OWNER VALUES('%s','%s','%s')"%(nonprimarysin,vehicle_id,is_primary_owner)) 
                    curs.execute(curStr)
                except cx_Oracle.DatabaseError as exc:
                    error, = exc.args
                    print( sys.stderr, "Oracle code:", error.code)
                    print( sys.stderr, "Oracle message:", error.message)
                    print( "===== Data insertion is fail. Reinput the data again! =====")
                       
            elif non_primary.lower() == 'n':
                print ("===== Go back to Main Menu =====")
                break
            else:
                print("Invalid input.\n")        
    
            
    return 0
    
def Driver_Licence_Registration():
    print ("\n ====== Driver Licence Registration ====== \n")    
    return 0
    
def Violation_Record():
    print ("\n ====== Violation Record ====== \n")
    return 0
    
def Search_Engine():
    print ("\n ====== Search Engine ====== \n")
    return 0   

def main():
    #Systemnumber = input("ask");
    #connectionTest = True
    #Get username and password for connection.
    connect = False   
       
    while connect == False:
        try:
            #Retrieve login information
            '''
            user=input("Username [%s]: " % getpass.getuser())
            if not user:
                user.getpass.getuser()
            pw=getpass.getpass()
           
            #establish connection
            conString=user+'/'+pw+'@gwynne.cs.ualberta.ca/CRS'
            '''
            s = input(" ")
            conString="weijie2"+'/'+"sun1wei2jie3sun"+'@gwynne.cs.ualberta.ca/CRS'
            
           
            connection=cx_Oracle.connect(conString)
            #cursor=connection.cursor()
            connect = True
        except:
            print ("error")
           
        else:
            pass
    curs = connection.cursor()
    #People_Information(curs,connection)
                  
    status = False   
    print ("====== WELCOME TO THE VEHICLE SYSTEM ======")

    while (status == False):
        print ("====== PLEASE CHOOSE THE PROGRAM ======")
        print ("1 New Vehicle Registration \n2 Auto Transaction \n3 Driver Licence Registration\n4 Violation Record\n5 Search Engine\nExit Exit the program")    
        Systemnumber = input("Please input 1-5 or Exit");
        
        if (Systemnumber == "1"):
            #go to New Vehicle Registration
            New_Vehicle(curs,connection)
            connection.commit()
            
        elif (Systemnumber == "2"):
            Auto_Transaction(curs,connection)
            
            
        elif (Systemnumber == "3"):
            Driver_Licence_Registration()
        elif (Systemnumber == "4"):
            Violation_Record()
        elif (Systemnumber == "5"):
            Search_Engine()
        elif (Systemnumber.lower() == "exit"):
            print ("Exit the system")
            status = True
        else : 
            print ("invalid input please try again")
            
    connection.close()

main()