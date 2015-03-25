#line 44. genderinput has been deleted
#all print tests have been deleted
#lines with long # need to be checked again
#code from line 615 to 638 need to be modified.
#didn't comment the main function.
#don't know how to comment form line 356 to 363

# Team Members: Tian Qi Xiao, Weijie Zhang, Qingdai Du
# Lecture Section: CMPUT291 B1

import sys
import cx_Oracle
import getpass
from random import randint


#This function will record the people information.

def People_Information(curs,connection,sin):
    print ("\n ====== People Information ====== \n")
    
    while True:
        try:
            name = input("Name:") #get the name of client.
            while True: 
                try :
            #excute the next step iff the input is valid.
                    #ask user for height input
                    height = int(input("Height [cm]:"))
                    #constrains for height.
                    if height < 1000 and height > 0: 
                        break
                    else:
                        print ("Enter the exactly integer.")
                except:
                    print ("Enter the exactly integer.")
            #excute the next step iff the input is valid.
            while True:
                try:
                    #ask user for weight input
                    weight = int(input("Weight [KG]:"))
                    #check if the weight input is valid
                    if weight < 1000 and weight > 0:
                        break
                    else:
                        print ("Enter the exactly integer.")
                except:
                    print ("Enter the exactly integer.")
            #ask user for eyecolor input    
            eyecolor = input("Eyecolor: ")
            #ask user for haircolot input
            haircolor = input("Haircolor: ")
            #ask user for addr input
            addr = input("Address: ")
            #ask user for gender input
            gender = input("Gender [f or m]: ").lower()
            #check whether it is an invalid input, if not, print a error message and ask for the input again
            while gender != 'f' and gender != 'm':
                print("Our system only accept the male and the female\n 'f' and 'm' only.")
                gender = input("Gender [f or m] ")                        
            birthday = input("birthday [DD-MMM-YYYY] ")
            while len(birthday) != 11 : #note the might error.
                print("Invalid input, please try agian")
                birthday = input("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")      
            #to store input information to the database
            curStr = ("INSERT INTO PEOPLE VALUES('%s','%s',%s,%s,'%s','%s','%s','%s','%s')"
                              %(sin,name,height,weight,eyecolor,haircolor,addr,gender,birthday))  
            curs.execute(curStr)
            connection.commit()
            break
        #reference of exception handling
        #http://stackoverflow.com/questions/7465889/cx-oracle-and-exception-handling-good-practices
        #autuor: Ben
        #edited at: Mar 24 2012 at 16:24
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print( sys.stderr, "Oracle code:", error.code)
            print( sys.stderr, "Oracle message:", error.message)
            print( "===== Data insertion is fail. Reinput the data again! =====")
    return 0    




#List the name, licence_no, addr, birthday, driving class, driving_condition, and 
#the expiring_data of a driver by entering either a licence_no or a given name. It 
#shall display all the entries if a duplicate name is given.

def search_1(curs,connection):
    print( "===== List All Information OF the driver =====")
    
    s_name = ("SELECT NAME FROM PEOPLE") #read name information from memory.
    curs.execute(s_name)
    lname = curs.fetchall()#fetch all (or all remaining) rows of a query result set and to return a list of tuples. 
                           #If no more rows are available, it returns an empty list.
    listname = []
    for i in lname:
        listname.append(i[0].strip())    
    
    s_licence = ("SELECT licence_no FROM drive_licence") #read licence information from memory.
    curs.execute(s_licence)
    llicence = curs.fetchall()
    listlicence = []
    for i in llicence:
        listlicence.append(i[0].strip())          
    print (listlicence) #print a list of licence number on the screen
    print (listname) #print a list of dirver's name on the screen
    option = input("1 Enter Name of the Driver \n2 Enter DriverLicence No\n") #based on clients' option, load key information of either name or licence number. 
    
    #check if the user input valid option number, if not, print a error message and ask for the input again
    while option !="1" and option !="2": #check if the user input valid option number
        print ("Invalild input please input '1' or '2' ")
        option = input("1 Enter Name of the Driver \n2 Enter DriverLicence No")
        
    if option == "1": #to match and load the client's name information from memory. 
        name = input("Name:")
        while name not in listname:
            print ("Name does not exist, please input again")
            name = input("Name:") #if name does not exist(a new client), update the new client's information to memory.
        nameconstr = ("SELECT p.name,d.licence_no,p.addr,p.birthday,d.class,dc.description,d.expiring_date FROM people p,drive_licence d,driving_condition dc, restriction r WHERE dc.c_id = r.r_id AND r.licence_no = d.licence_no AND p.sin = d.sin AND UPPER(p.name) ='"+name.upper()+"'")
        curs.execute(nameconstr)
        result = curs.fetchall() 
        print (result)
               
        for j in result: #based on the form of to data structure, to print all information of the new client.    
            print ("Name:",j[0],"\nlicence No",j[1],"\nAddress",j[2],"\nBirthday",j[3],"\nDriving Class",j[4],"\nDriving_condition",j[5],"\nExpiring data",j[6],"\n")
            
    else:
        licence_no = input("licence NO:") #get licence number
        while licence_no not in listlicence: #match licence number with data in memory
            print ("licence_no does not exist, please input again")
            licence_no = input("licence NO:") #if licence number does not exist(a new client), add the new client's information to memory.
        licenceconstr = ("SELECT p.name,d.licence_no,p.addr,p.birthday,d.class,dc.description,d.expiring_date FROM people p, drive_licence d, driving_condition dc, restriction r WHERE UPPER(p.sin) = UPPER(d.sin) AND dc.c_id = r.r_id AND d.licence_no = '"+licence_no+"' AND r.licence_no = d.licence_no")
        curs.execute(licenceconstr)
        result = curs.fetchall()
        print (result)
        #group all the personal information desired together and print on the screen 
        for j in result:     
            print ("Name:",j[0],"\nlicence No",j[1],"\nAddress",j[2],"\nBirthday",j[3],"\nDriving Class",j[4],"\nDriving_condition",j[5],"\nExpiring data",j[6],"\n")        
    
    print( "===== End Of List All Information OF the driver =====")
        
    return 0




#List all violation records received by a person if  the drive licence_no or sin 
#of a person is entered.

def search_2(curs,connection):
    print ("===== List All violation infromation OF the driver =====")
    s_sin = ("SELECT SIN FROM PEOPLE") #load sin number(key information) from memory.
    curs.execute(s_sin)
    lsin = curs.fetchall()
    listsin = []
    for i in lsin:
        listsin.append(i[0].strip())    
    
    s_licence = ("SELECT licence_no FROM drive_licence") #load licence number(one of the key information) from memory.
    curs.execute(s_licence) 
    llicence = curs.fetchall()
    listlicence = []
    for i in llicence:
        listlicence.append(i[0].strip())          
    print (listlicence)#print a list of licence number to the screen
    print (listsin)#print a list of sin number to the screen
    option = input("1 Enter Sin Number of the Driver \n2 Enter DriverLicence No\n")
    while option !="1" and option !="2":
        print ("Invalild input please input '1' or '2' ")
        option = input("1 Enter Sin Number of the Driver \n2 Enter DriverLicence No")
        
    if option == "1":
        sin = input("SIN:")
        while sin not in listsin:
            print ("SIN does not exist, please input again") #if SIN does not exist, get the new SIN from user input.
            sin = input("SIN:")
        sinconstr = ("SELECT p.name,t.ticket_no, t.violator_no, t.vehicle_id,t.office_no,t.vtype,t.vdate,t.place,t.descriptions, tt.fine FROM people p,ticket t, ticket_type tt WHERE t.violator_no = '"+sin+"' AND t.violator_no = p.sin AND t.vtype = tt.vtype") #get the new SIN updated in memory
        curs.execute(sinconstr)
        result = curs.fetchall()
               
        for j in result:     
            print ("Name:",j[0],"\nTicket No:",j[1],"\nViolator No:",j[2],"\nVehicle Id:",j[3],"\nOffice No:",j[4],"\nViolator type:",j[5],"\nPlace:",j[6],"\nDescription:",j[7],"\nFine:",j[8],"\n") 
            
        
        
    else:
        licence_no = input("licence NO:")
        while licence_no not in listlicence: #if licence number does not exist, get the new numeber from user input.
            print ("licence_no does not exist, please input again")
            licence_no = input("licence NO:")
        licence_noconstr = ("SELECT p.name,t.ticket_no, t.violator_no, t.vehicle_id,t.office_no,t.vtype,t.vdate,t.place,t.descriptions , tt.fine FROM people p, drive_licence d, ticket t,ticket_type tt WHERE p.sin = t.violator_no AND UPPER(p.sin) = UPPER(d.sin) AND UPPER(d.licence_no) = '"+licence_no+"' AND t.vtype = tt.vtype")
        curs.execute(licence_noconstr)
        result = curs.fetchall()
               
        for j in result:     
            print ("Name:",j[0],"\nTicket No:",j[1],"\nViolator No:",j[2],"\nVehicle Id:",j[3],"\nOffice No:",j[4],"\nViolator type:",j[5],"\nPlace:",j[6],"\nDescription:",j[7],"\nFine:",j[8],"\n")    
    
    print ("===== End of List All violation infromation OF the driver =====")    
    return 0




#Print out the vehicle_history, including the number of times that a vehicle has 
#been changed hand, the average price, and the number of violations it has been 
#involved by entering the vehicle's serial number.

def search_3(curs,connection):
    print ("===== The Vehicle History =====")

    s_serial = ("SELECT licence_no FROM drive_licence")
    curs.execute(s_serial)
    lserial = curs.fetchall()
    listserial = []
    for i in lserial:
        listserial.append(i[0].strip())          
    
    serial_no = input("Serial No:")

    while serial_no not in listserial: #if serial number does not exist, get the new numeber from user input.
        print ("Invalid input")
        serial_no = input("Serial No:") 

        while True:
            try:
                vhstrcur = "DROP VIEW vehicle_history" #drop view table
                curs.execute(vhstrcur)
                connection.commit()
                
                break
            except:
                print ("droperror")#handle drop error
                break
        while True:
            try:
                vhstrcur = "CREATE VIEW vehicle_history (vehicle_no, number_sales, average_price, total_tickets) AS SELECT  h.serial_no, count(DISTINCT transaction_id), avg(price), count(DISTINCT t.ticket_no) FROM vehicle h, auto_sale a, ticket t WHERE t.vehicle_id (+) = h.serial_no AND a.vehicle_id (+) = h.serial_no GROUP BY h.serial_no;"
                curs.execute(vhstrcur)
                connection.commit()                
                break
            except:
                print ("vh error")
            
    vhconstr = ("SELECT * FROM vehicle_history vh WHERE vh.vehicle_no = "+serial_no+" ")
    curs.execute(vhconstr)
    connection.commit()                   
    result = curs.fetchall()   
    for j in result:     
        print ("Vehicle No:",j[0],"\nNumber of Sales:",j[1],"\nAverage Price:",j[2],"\nTotal Tickets:",j[3],"\n")  
    print ("===== End Of The Vehicle History =====")    
    return 0




#This function is used to register a new vehicle by an auto registration officer. 
#By a new vehicle, we mean a vehicle that has not been registered in the database. 
#The component shall allow an officer to enter the detailed information about the 
#vehicle and personal information about its new owners, if it is not in the database. 
#You may assume that all the information about vehicle types has been loaded in 
#the initial database.

def New_Vehicle(curs,connection):
    print ("\n ====== New Vehicle Registration ====== \n")
    status = True
    while True:
        try:
            while True:
                try:
                    s_serialno = ("SELECT SERIAL_NO FROM VEHICLE") #load serial number from memory.
                    curs.execute(s_serialno)
                    lSerial_no = curs.fetchall()
                    listSerial_no = []
                    for i in lSerial_no:
                        listSerial_no.append(i[0].strip())
                     
                    break
                except:
                    print("Invalid input, please try agian")
                else:
                    pass
                
            serial_no = input("Serial_no [within 20 number]:")
            while serial_no in listSerial_no or serial_no.split() == []:#check whether the vehicle information already exists
                print ("That is not a valid input")
                serial_no = input("Serial_no [within 20 number]:")
            
            maker = input("Maker [within 20 Char]:") #get more information about the new vehicle
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
                    s_typeid = ("SELECT TYPE_ID FROM VEHICLE") # load type id from database
                    curs.execute(s_typeid)
                    ltypeid = curs.fetchall()
                    listtypeid = []
                    print (ltypeid)#print a list of type id 
                    for i in ltypeid:
                        if i[0] not in listtypeid:
                            listtypeid.append(i[0])#load information in ltypeid to listtypeid
                     
                    break
                except:
                    print ("error")#data cannot load from type id, print error message
            while True:
                try:
                    type_id = int(input("Select a Type ID {} :".format(listtypeid)))#get new information of type id
                    if type_id in listtypeid :
                        break
                except:
                    print ("Invalid input")
                else:
                    pass
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
            s_sin = ("SELECT SIN FROM PEOPLE")#load SIN from memory
            curs.execute(s_sin)
            lsin = curs.fetchall()
            listsin = []
            for i in lsin:
                listsin.append(i[0].strip())
             

            break
        except:
            print("Invalid input, please try agian")
        else:
            pass    
    
    sin = input("Sin:")#get owner informaiton about the new vihecle
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
            while is_primary_owner != 'y' and is_primary_owner != 'n':    
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




#This component is used to complete an auto transaction. Your program shall allow 
#the officer to enter all necessary information to complete this task, including, 
#but not limiting to, the details about the seller, the buyer, the date, and the 
#price. The component shall also remove the relevant information of the previous 
#ownership.
def Auto_Transaction(curs,connection):
    print ("\n ====== Auto Transaction ====== \n")
    s_sin = ("SELECT SIN FROM PEOPLE")#load SIN form memory
    curs.execute(s_sin)
    lsin = curs.fetchall()
    listsin = []      
    for i in lsin:
        if i[0].strip() not in listsin:
            listsin.append(i[0].strip())    
            
    s_vehicle = ("SELECT SERIAL_NO FROM VEHICLE")#load serial number from memory
    curs.execute(s_vehicle)
    lvehicle = curs.fetchall()
    listvehicle = []
    for i in lvehicle:
        if i[0].strip() not in listvehicle:
            listvehicle.append(i[0].strip()) 
            
    s_transaction_id = ("SELECT SERIAL_NO FROM VEHICLE")#load serial number of vehicle which will be transacted
    curs.execute(s_transaction_id)
    ltransaction_id = curs.fetchall()
    listtransaction_id = []
    for i in ltransaction_id:
        if i[0].strip() not in listtransaction_id:
            listtransaction_id.append(i[0].strip())       
    
    
    print (listtransaction_id)#print a list of transaction_id to the screen
    print (listvehicle)#print a list of vehicle to the screen
    print (listsin)#print a list of sin number to the screen
    
    while True:
        try:
            seller_id = input("Seller_id:")#get SIN of the person who is going to sell the vehicle
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
            buyer_id = input("Buyer_id:")#get SIN of person who is going to buy the vehicle
            if buyer_id not in listsin:
                print ("The personal information is not register")
                print ("Please register the personal inforamtion first")
                People_Information(curs,connection,buyer_id)
                break
            elif buyer_id == seller_id:#transaction in the same person is not permitted
                print ("Seller can not buy car from sellerself")
            else:
                break
        except:
            print ("Invalid buyer_id input")
        else:
            pass    
    
    while True:
        try:
            vehicle_id = input("Vehicle id :")#get ID of vehicle which would be transacted
            if vehicle_id not in listsin:
                print ("Please register the Vehicle first")#handle the case which the vehicle hasn't been registrated yet.
                goto = input("Do you want to go to New Vehicle system['y' or 'n'] \n 'n' Go To Main menu").lower()#ask to registrate the vehicle first.
                while goto !="y" and goto != "n":
                    goto = input("Do you want to go to New Vehicle system['y' or 'n'] \n 'n' Go To Main menu").lower()
                    
                if goto == "y":#jump to Vehicle Registration.
                    New_Vehicle(curs,connection)
                elif goto == "n":
                    return 0          
            break
        except:
            print ("Invalid buyer_id input")
        else:
            pass      
    
    s_date = input("Seller Date [DD-MMM-YYYY] :")#require the date of transaction
    while len(s_date) != 11 : #note the might error
        print("Invalid input, please try agian")
        s_date = input("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")          
    
    while True:
        try:
            price = round(float(input("Price [0-999999]:")),2)#require the price of transacted vehicle
            if price < 1000000000 and price > 0 : #add a upperbound and lowerbound to avoid overflow
                break
            else:
                print ("Invalid Price Input")
        except:
            print ("Invalid Price Input")
    
    getTraniD = input("Do you want to enter transaction_id?\n 'y' is enter an ID, 'n' is automatic get an id ").lower()#ask for transaction id
    while getTraniD != "y" and getTraniD != "n":
        getTraniD = input("Do you want to enter transaction_id?\n 'y' is enter an ID, 'n' is automatic get an id ").lower()
    if getTraniD == "y":
        while True:
            try:
                transaction_id = int(input("Transaction ID:" ))#get transaction id from user input.
                if transaction_id in listtransaction_id:
                    print ("The transaction id already exist, please input again")#no duplicate of transaction id.
                else:
                    break
            except:
                print ("Invalid transaction id input")
    else:
        while True:
            transaction_id = randint(0,10000)#system creates a new transaction automatically
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
            non_primary = input("Does this vehicle has more than one owner? Enter 'y' or 'n'\n")#check if there exists another owner.
            if non_primary.lower() == 'y':
                nonprimarysin = input("Non-primary Owner Sin : ")#update another person to the owner.
                if nonprimarysin not in listsin:
                    People_Information(curs,connection,nonprimarysin)
                    
                try:
                    is_primary_owner = 'n'
                    curStr = ("INSERT INTO OWNER VALUES('%s','%s','%s')"%(nonprimarysin,vehicle_id,is_primary_owner)) 
                    curs.execute(curStr)
                    connection.commit()
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




#This component is used to record the information needed to issuing a drive licence, 
#including the personal information and a picture for the driver. You may assume 
#that all the image files are stored in a local disk system.

def Driver_Licence_Registration(curs,connection):
    print ("\n ====== Driver Licence Registration ====== \n")   
    s_sin = ("SELECT SIN FROM PEOPLE")#load SIN from memory
    curs.execute(s_sin)
    lsin = curs.fetchall()
    listsin = []      
    for i in lsin:
        if i[0].strip() not in listsin:
            listsin.append(i[0].strip())      
    sin = input ("SIN:")
    while sin in listsin:
        print ("Enter a New Sin")
        sin = input ("SIN:")
        
   
    People_Information(curs,connection,sin)

    s_licence_no = ("SELECT licence_no FROM drive_licence")#load SIN from memory
    curs.execute(s_licence_no)
    llicence_no = curs.fetchall()
    listlicence_no = []      
    for i in llicence_no:
        if i[0].strip() not in listlicence_no:
            listlicence_no.append(i[0].strip())     
    while True:
        try:
            while True:
                try:
                    licence_no = input("licence No:")#get driver licence number
                    if licence_no in listlicence_no:
                        print ("The Driver licence No. already exist")#no multiple licence-registration allowed
                    else:
                        break
                except:
                    print ("Invalid licence No input")
                else:
                    pass
             
            while True:
                try:
                    driveclass = input("Drive Class:")#get driver's class type
                    break
                except:
                    print ("Invalid driveclass input")
                else:
                    pass               
            
        
            issuing_date = input ("Issuing Date [DD-MMM-YYYY] :")#ask for the date licence issued
            while len(issuing_date) != 11 : #note the might error
                print("Invalid input, please try agian")
                issuing_date = input("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")       
            
        
            expiring_date = input ("Expiring Date [DD-MMM-YYYY] :")
            while len(expiring_date) != 11 : #note the might error
                print("Invalid input, please try agian")
                expiring_date = input("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")     
                
                
            #Load image into memory from local file 
            #(Assumes a file by this name exists in the directory you are running from)
            name = input("The local image file name: ")
            f_image = open(name,'rb')
            while True:
                try:    
                    photo = f_image.read()
                    break
                except:
                    f_image = input("the local file name: ")
            curs.setinputsizes(photo = cx_Oracle.BLOB)

            insert = """insert into drive_licence(licence_no,sin,class,photo,issuing_date,expiring_date)
                values (:licence_no, :sin, :class, :photo, :issuing_date, :expiring_date)"""
            print(insert)
            curs.execute(insert,{'licence_no':licence_no, 'sin':sin,'class':driveclass, 'photo':photo,'issuing_date':issuing_date,'expiring_date':expiring_date})
            connection.commit()
            f_image.close()
            break        
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print( sys.stderr, "Oracle code:", error.code)
            print( sys.stderr, "Oracle message:", error.message)
            print("Data insertion is fail. Check the data again!\n") 

#This component is used by a police officer to issue a traffic ticket and record 
#the violation. All the information about ticket_type has been loaded in the 
#initial database.

def Violation_Record(curs,connection):
    print ("\n ====== Violation Record ====== \n")
    s_sin = ("SELECT SIN FROM PEOPLE")#load SIN from memory
    curs.execute(s_sin)
    lsin = curs.fetchall()
    listsin = []      
    for i in lsin:
        if i[0].strip() not in listsin:
            listsin.append(i[0].strip())        
    
    s_vehicle = ("SELECT SERIAL_NO FROM VEHICLE")#load serial number from memory
    curs.execute(s_vehicle)
    lvehicle = curs.fetchall()
    listvehicle = []
    for i in lvehicle:
        if i[0].strip() not in listvehicle:
            listvehicle.append(i[0].strip())     
    
    s_vtype = ("SELECT vtype FROM ticket_type")#load vehicle type from memory
    curs.execute(s_vtype)
    lvtype = curs.fetchall()
    listvtype = []
    for i in lvtype:
        if i[0].strip() not in listvtype:
            listvtype.append(i[0].strip())              
     
    s_ticket_no = ("SELECT ticket_no FROM ticket")#load ticket number from memory
    curs.execute(s_ticket_no)
    lticket_no = curs.fetchall()
    listticket_no = []
    for i in lticket_no:
        if i[0] not in listticket_no:
            listticket_no.append(i[0])        
    print (listticket_no)
     
     
    chooseTicketNo = input("Do you want to automaticlly produce a random ticket No?\n'y' producet a random ticket No\n'n' enter ticket no manually\n").lower()
    if chooseTicketNo == 'y':
        while True:
                    ticket_no = randint(0,1000000)#system creates a ticket number automatically
                    if ticket_no not in listticket_no:
                        break
    else:
        while True:
            ticket_no = int(input("Ticket No:"))
            if ticket_no in listticket_no: #no duplicate ticket number allowed.
                print ("The Ticket No. already Exist")
            else :
                break
    
    
    violator_no = input("Violator No :")#get information of violators
    while len(violator_no) > 15:
        print ("violator_no invalid input")
        violator_no = input("Violator No :")
        
    while violator_no not in listsin:#check if it exists the information of the violator.
        print ("People Sin did not found, please register first")
        People_Information(curs,connection,violator_no)


    vehicle_id = input("vehicle id No :")#get the vehicle ID.
    while len(vehicle_id) > 15:
        print ("violator_no invalid input")
        vehicle_id = input("vehicle id No :")
        
    while vehicle_id not in listvehicle:#check if it exists the information of the vehicle.
        print ("Vehicle Id did not found, please register first")
        back = input("Do you want to go back to Main menu? \n'y' go back to Main menu \nelse reinput a vehicle id\n").lower()#ask person to check the typo
        if back == "y":
            return 0
        else:
            vehicle_id = input("Violator No :")
            while len(vehicle_id) > 15:
                    print ("violator_no invalid input")
                    vehicle_id = input("Violator No :")            
    
    office_no = input("Office No:")#get the office numebr
    while len(office_no) > 15:
        print ("Office No invalid input")
        office_no = input("Office No :")    
    
    print ("Here is All Ticket Type")#list all ticket type
    print (listvtype)    
    vtype = input("Variable of Ticket Type:")#get the violation type


    while vtype not in listvtype:
        print ("Not This Kind Of Ticket Type")#match input violation type with existing type
        vtype = input("Variable of Ticket Type:")           
        while len(vtype) > 10:
            print ("Variable of Ticket Type invalid input")
            vtype = input("Variable of Ticket Type:")   
    
    
    print ("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")#get the date of the violation          
    vdate = input("Date:")
    while len(vdate) != 11:
        print ("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")          
        
        print ("Date invalid input")
        vdate = input("Date :")     
        
    place = input("Place:")#get the place of the violation
    while len(place) >= 20:
        print ("Place invalid input")
        place = input("Place :")    
        
    descriptions = input("descriptions:")#get more detailed description of the violation
    while len(descriptions) > 1024:
        print ("descriptions invalid input")
        descriptions = input("descriptions :")          
    
    while True:#if all informations of violation are valid, update them to memory
        try:
            curStr = ("INSERT INTO ticket VALUES(%s,'%s','%s','%s','%s','%s','%s','%s')"
                              %(ticket_no,violator_no,vehicle_id,office_no,vtype,vdate,place,descriptions))
            curs.execute(curStr)
            connection.commit()            
            break
        except cx_Oracle.DatabaseError as exc:
                error, = exc.args
                print( sys.stderr, "Oracle code:", error.code)
                print( sys.stderr, "Oracle message:", error.error)
                print("Data insertion is fail. Check the data again!\n")
        else:
            Violation_Record(curs,connection)
    
    print (" ====== End Violation Record ====== ")
    return 0




#This function will manage all three search method. It will ask the user to choose
#a number from 1 to 3, and the function will call the co-responding search method
#to perform the search.
def Search_Engine(curs,connection):
    print ("====== Search Engine ====== ")
    
    while True:#list options in this search engine
        print ("1 List All Basic Information OF the driver")
        print ("2 List All violation infromation OF the driver")
        print ("3 The Vehicle History")   
        print ("Exit Exit the search Engine")
        
        sechoice = input("\n").lower()#handle invalid user input
        while sechoice != "1" and sechoice != "2" and sechoice != "3" and sechoice != "exit":
            print ("Invalid input, please input")
            print ("1 List All Basic Information OF the driver")
            print ("2 List All violation infromation OF the driver")
            print ("3 The Vehicle History")
            print ("Exit Exit the search Engine")
            sechoice = input("\n")
            
        if sechoice == "1":#go to the corresponding part based on user's input.
            search_1(curs,connection)
        elif sechoice == "2":
            search_2(curs,connection)
        elif sechoice == "3":
            search_3(curs,connection)
        else:
            break
    
    return 0 


#This is the main function of the program. This function will let user connect to
#the oracle and ask user to choose a number, then the program will call different
#function to meet user's desired requestion. 
def main():
    #Systemnumber = input("ask");
    #connectionTest = True
    #Get username and password for connection.
    connect = False   
       
    while connect == False:
        try:
            #Retrieve login information
            
            user=input("Username [%s]: " % getpass.getuser())
            if not user:
                user.getpass.getuser()
            pw=getpass.getpass()
           
            #establish connection
            conString=user+'/'+pw+'@gwynne.cs.ualberta.ca/CRS'
            
            #s = input(" ")
            #conString="weijie2"+'/'+"sun1wei2jie3sun"+'@gwynne.cs.ualberta.ca/CRS'
            
           
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
        print ("1 New Vehicle Registration \n2 Auto Transaction \n3 Driver Licence Registration\n4 Violation Record\n5 Search Engine\nExit Exit the program\n")    
        Systemnumber = input("Please input 1-5 or Exit\n");
        
        if (Systemnumber == "1"):
            #go to New Vehicle Registration
            New_Vehicle(curs,connection)
            connection.commit()
            
        elif (Systemnumber == "2"):
            Auto_Transaction(curs,connection)
            
            
        elif (Systemnumber == "3"):
            Driver_Licence_Registration(curs,connection)
        elif (Systemnumber == "4"):
            Violation_Record(curs,connection)
        elif (Systemnumber == "5"):
            Search_Engine(curs,connection)
        elif (Systemnumber.lower() == "exit"):
            print ("Exit the system")
            status = True
        else : 
            print ("invalid input please try again")
    curs.close()        
    connection.close()

main()
