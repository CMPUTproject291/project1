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

def search_1(curs,connection):
    print( "===== List All Information OF the driver =====")
    
    s_name = ("SELECT NAME FROM PEOPLE")
    curs.execute(s_name)
    lname = curs.fetchall()
    listname = []
    #print (lSerial_no)
    for i in lname:
        listname.append(i[0].strip())    
    
    s_licence = ("SELECT licence_no FROM drive_licence")
    curs.execute(s_licence)
    llicence = curs.fetchall()
    listlicence = []
    #print (lSerial_no)
    for i in llicence:
        listlicence.append(i[0].strip())          
    print (listlicence)
    print (listname)
    option = input("1 Enter Name of the Driver \n2 Enter DriverLicence No\n")
    while option !="1" and option !="2":
        print ("Invalild input please input '1' or '2' ")
        option = input("1 Enter Name of the Driver \n2 Enter DriverLicence No")
        
    if option == "1":
        name = input("Name:")
        while name not in listname:
            print ("Name does not exist, please input again")
            name = input("Name:")   
        nameconstr = ("SELECT p.name,d.licence_no,p.addr,p.birthday,d.class,dc.description,d.expiring_date FROM people p,drive_licence d,driving_condition dc, restriction r WHERE dc.c_id = r.r_id AND r.licence_no = d.licence_no AND p.sin = d.sin AND UPPER(p.name) ='"+name.upper()+"'")
        curs.execute(nameconstr)
        result = curs.fetchall()
        print (result)
               
        for j in result:     
            print ("Name:",j[0],"\nlicence No",j[1],"\nAddress",j[2],"\nBirthday",j[3],"\nDriving Class",j[4],"\nDriving_condition",j[5],"\nExpiring data",j[6],"\n")
            
        
        
    else:
        licence_no = input("licence NO:")
        while licence_no not in listlicence:
            print ("licence_no does not exist, please input again")
            licence_no = input("licence NO:")
        licenceconstr = ("SELECT p.name,d.licence_no,p.addr,p.birthday,d.class,dc.description,d.expiring_date FROM people p, drive_licence d, driving_condition dc, restriction r WHERE UPPER(p.sin) = UPPER(d.sin) AND dc.c_id = r.r_id AND d.licence_no = '"+licence_no+"' AND r.licence_no = d.licence_no")
        curs.execute(licenceconstr)
        result = curs.fetchall()
        print (result)         
        for j in result:     
            print ("Name:",j[0],"\nlicence No",j[1],"\nAddress",j[2],"\nBirthday",j[3],"\nDriving Class",j[4],"\nDriving_condition",j[5],"\nExpiring data",j[6],"\n")        
    
    print( "===== End Of List All Information OF the driver =====")
        
    return 0

def search_2(curs,connection):
    print ("===== List All violation infromation OF the driver =====")
    s_sin = ("SELECT SIN FROM PEOPLE")
    curs.execute(s_sin)
    lsin = curs.fetchall()
    listsin = []
    #print (lSerial_no)
    for i in lsin:
        listsin.append(i[0].strip())    
    
    s_licence = ("SELECT licence_no FROM drive_licence")
    curs.execute(s_licence)
    llicence = curs.fetchall()
    listlicence = []
    #print (lSerial_no)
    for i in llicence:
        listlicence.append(i[0].strip())          
    print (listlicence)
    print (listsin)
    option = input("1 Enter Sin Number of the Driver \n2 Enter DriverLicence No\n")
    while option !="1" and option !="2":
        print ("Invalild input please input '1' or '2' ")
        option = input("1 Enter Sin Number of the Driver \n2 Enter DriverLicence No")
        
    if option == "1":
        sin = input("SIN:")
        while sin not in listsin:
            print ("SIN does not exist, please input again")
            sin = input("SIN:")   
        sinconstr = ("SELECT p.name,t.ticket_no, t.violator_no, t.vehicle_id,t.office_no,t.vtype,t.vdate,t.place,t.descriptions, tt.fine FROM people p,ticket t, ticket_type tt WHERE t.violator_no = '"+sin+"' AND t.violator_no = p.sin AND t.vtype = tt.vtype")
        curs.execute(sinconstr)
        result = curs.fetchall()
        #print (result)
               
        for j in result:     
            print ("Name:",j[0],"\nTicket No:",j[1],"\nViolator No:",j[2],"\nVehicle Id:",j[3],"\nOffice No:",j[4],"\nViolator type:",j[5],"\nPlace:",j[6],"\nDescription:",j[7],"\nFine:",j[8],"\n")
            
        
        
    else:
        licence_no = input("licence NO:")
        while licence_no not in listlicence:
            print ("licence_no does not exist, please input again")
            licence_no = input("licence NO:")
        licence_noconstr = ("SELECT p.name,t.ticket_no, t.violator_no, t.vehicle_id,t.office_no,t.vtype,t.vdate,t.place,t.descriptions , tt.fine FROM people p, drive_licence d, ticket t,ticket_type tt WHERE p.sin = t.violator_no AND UPPER(p.sin) = UPPER(d.sin) AND UPPER(d.licence_no) = '"+licence_no+"' AND t.vtype = tt.vtype")
        curs.execute(licence_noconstr)
        result = curs.fetchall()
        #print (result)
               
        for j in result:     
            print ("Name:",j[0],"\nTicket No:",j[1],"\nViolator No:",j[2],"\nVehicle Id:",j[3],"\nOffice No:",j[4],"\nViolator type:",j[5],"\nPlace:",j[6],"\nDescription:",j[7],"\nFine:",j[8],"\n")    
    
    print ("===== End of List All violation infromation OF the driver =====")    
    return 0

def search_3(curs,connection):
    print ("===== The Vehicle History =====")

    s_serial = ("SELECT licence_no FROM drive_licence")
    curs.execute(s_serial)
    lserial = curs.fetchall()
    listserial = []
    #print (lSerial_no)
    for i in lserial:
        listserial.append(i[0].strip())          
    print (listserial)
    
    serial_no = input("Serial No:")

    while serial_no not in listserial:
        print ("Invalid input")
        serial_no = input("Serial No:")

        while True:
            try:
                vhstrcur = "DROP VIEW vehicle_history"
                curs.execute(vhstrcur)
                connection.commit()
                
                break
            except:
                print ("droperror")
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
    #print (vhconstr)
    curs.execute(vhconstr)
    connection.commit()                    
    result = curs.fetchall()  
    #print (result)
    for j in result:     
        print ("Vehicle No:",j[0],"\nNumber of Sales:",j[1],"\nAverage Price:",j[2],"\nTotal Tickets:",j[3],"\n")  
    print ("===== End Of The Vehicle History =====")    
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
            elif buyer_id == seller_id:
                print ("Seller can not buy car from sellerself")
            else:
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
    
    s_date = input("Seller Date [DD-MMM-YYYY] :")
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
    
def Driver_Licence_Registration(curs,connection):
    print ("\n ====== Driver Licence Registration ====== \n")   
    s_sin = ("SELECT SIN FROM PEOPLE")
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

    s_licence_no = ("SELECT SIN FROM PEOPLE")
    curs.execute(s_licence_no)
    llicence_no = curs.fetchall()
    listlicence_no = []      
    for i in llicence_no:
        if i[0].strip() not in listlicence_no:
            listlicence_no.append(i[0].strip())     
            
    while True:
        try:
            licence_no = input("licence No:")
            if licence_no in listsin:
                print ("The Driver licence No already exist")
            else:
                break
        except:
            print ("Invalid licence No input")
        else:
            pass
     
    while True:
        try:
            driveclass = input("Drive Class:")
            break
        except:
            print ("Invalid driveclass input")
        else:
            pass               
    

    issuing_date = input ("Issuing Date [DD-MMM-YYYY] :")
    while len(issuing_date) != 11 : #note the might error
        print("Invalid input, please try agian")
        issuing_date = input("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")       
    

    expiring_date = input ("Expiring Date [DD-MMM-YYYY] :")
    while len(expiring_date) != 11 : #note the might error
        print("Invalid input, please try agian")
        expiring_date = input("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")     
        
    '''    
    # information for the new row
    pid=101
    title="Window"
    place="Utah"
    '''
    #Load image into memory from local file 
    #(Assumes a file by this name exists in the directory you are running from)
    
    while True:
        try:    
            image = f_image.read()
            break
        except:
            f_image = input("the local file name: ") 
            break
    
    #f_image  = open('window-sm.jpg','rb')
    image  = f_image.read()
    curStr = connection.cursor()
    # prepare memory for operation parameters
    curStr.setinputsizes(image = cx_Oracle.BLOB)
    
    #while True:
        #try:
    insert = """insert into drive_licence(licence_no,sin,class,photo,issuing_date,expiring_date)
        values (:licence_no, :sin, :class, :photo, :issuing_date, :expiring_date)"""
    print (insert)
    print("Good!")
    i = input ("")

    
    curs.execute(insert,{'licence_no':licence_no, 'sin':sin,'class':driveclass, 'photo':image,'issuing_date':issuing_date,'expiring_date':expiring_date})
    #connection.commit()          
    print ("Nice")
    f_image.close()
    '''   
            break
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print( sys.stderr, "Oracle code:", error.code)
            print( sys.stderr, "Oracle message:", error.message)
            print( "===== Data insertion is fail. Reinput the data again! =====")     
    '''   

    # Housekeeping...

    return 0
    
def Violation_Record(curs,connection):
    print ("\n ====== Violation Record ====== \n")
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
    
    s_vtype = ("SELECT vtype FROM ticket_type")
    curs.execute(s_vtype)
    lvtype = curs.fetchall()
    listvtype = []
    for i in lvtype:
        if i[0].strip() not in listvtype:
            listvtype.append(i[0].strip())              
     
    s_ticket_no = ("SELECT ticket_no FROM ticket")
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
                    ticket_no = randint(0,1000000)
                    if ticket_no not in listticket_no:
                        break
    else:
        while True:
            ticket_no = int(input("Ticket No:"))
            if ticket_no in listticket_no:
                print ("The Ticket No already Exist")
            else :
                break
    
    
    violator_no = input("Violator No :")
    while len(violator_no) > 15:
        print ("violator_no invalid input")
        violator_no = input("Violator No :")
        
    while violator_no not in listsin:
        print ("People Sin did not found, please register first")
        People_Information(curs,connection,violator_no)


    vehicle_id = input("vehicle id No :")
    while len(vehicle_id) > 15:
        print ("violator_no invalid input")
        vehicle_id = input("vehicle id No :")
        
    while vehicle_id not in listvehicle:
        print ("Vehicle Id did not found, please register first")
        back = input("Do you want to go back to Main menu? \n'y' go back to Main menu \nelse reinput a vehicle id\n").lower()
        if back == "y":
            return 0
        else:
            vehicle_id = input("Violator No :")
            while len(vehicle_id) > 15:
                    print ("violator_no invalid input")
                    vehicle_id = input("Violator No :")            
    
    office_no = input("Office No:")
    while len(office_no) > 15:
        print ("Office No invalid input")
        office_no = input("Office No :")    
    
    print ("Here is All Ticket Type")
    print (listvtype)    
    vtype = input("Variable of Ticket Type:")


    while vtype not in listvtype:
        print ("Not This Kind Of Ticket Type")
        vtype = input("Variable of Ticket Type:")           
        while len(vtype) > 10:
            print ("Variable of Ticket Type invalid input")
            vtype = input("Variable of Ticket Type:")   
    
    
    print ("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")          
    vdate = input("Date:")
    while len(vdate) != 11:
        print ("Note that we need the date in format looks like '01-Mar-2015'\nDOB [DD-MMM-YYYY] ")          
        
        print ("Date invalid input")
        vdate = input("Date :")     
        
    place = input("Place:")
    while len(place) >= 20:
        print ("Place invalid input")
        place = input("Place :")    
        
    descriptions = input("descriptions:")
    while len(descriptions) > 1024:
        print ("descriptions invalid input")
        descriptions = input("descriptions :")          
    
    
    while True:
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
    
def Search_Engine(curs,connection):
    print ("====== Search Engine ====== ")
    
    while True:
        print ("1 List All Basic Information OF the driver")
        print ("2 List All violation infromation OF the driver")
        print ("3 The Vehicle History")   
        print ("Exit Exit the search Engine")
        
        sechoice = input("\n").lower()
        while sechoice != "1" and sechoice != "2" and sechoice != "3" and sechoice != "exit":
            print ("Invalid input, please input")
            print ("1 List All Basic Information OF the driver")
            print ("2 List All violation infromation OF the driver")
            print ("3 The Vehicle History")
            print ("Exit Exit the search Engine")
            sechoice = input("\n")
            
        if sechoice == "1":
            search_1(curs,connection)
        elif sechoice == "2":
            search_2(curs,connection)
        elif sechoice == "3":
            search_3(curs,connection)
        else:
            break
    
    return 0   

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
            
    connection.close()

main()