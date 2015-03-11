import sys
import cx_Oracle
import getpass

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
            print("Data insertion is fail. Check the data again!\n")         
    return 0    
    
   
def New_Vehicle(curs,connection):
    print ("\n ====== New Vehicle Registration ====== \n")
    status = True
    #while True:
       # try:
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
    '''    
            break
        except :
            print("Invalid input, please try agian")
        else:
            pass
    '''
        

    
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
        except:
            print ("something wrong. please input again")
        else:
            pass
            
    print ("====== BACK TO THE MAIN MENUE ======")        
    return 0
    
def Auto_Transaction():
    print ("\n ====== Auto Transaction ====== \n")
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
            user=input("Username [%s]: " % getpass.getuser())
            if not user:
                user.getpass.getuser()
            pw=getpass.getpass()
           
            #establish connection
            conString=user+'/'+pw+'@gwynne.cs.ualberta.ca/CRS'
           
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
        Systemnumber = input("Please input 1-5 or Exit");
        print ("====== PLEASE CHOOSE THE PROGRAM ======")
        print ("1 New Vehicle Registration \n2 Auto Transaction \n3 Driver Licence Registration\n4 Violation Record\n5 Search Engine\n Exit Exit the program")        
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