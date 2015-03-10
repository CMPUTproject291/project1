import sys
import cx_Oracle
import getpass

def People_Information(curs,connection):
    print ("\n ====== People Information ====== \n")
    
    while True:
        try:
            sin=input("Sin:")
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
                print("\nInvalid input, please try agian\n")
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
    
   
def New_Vehicle():
    print ("\n ====== New Vehicle Registration ====== \n")
    status = True
    '''
    while True:
        try:
            s_serialno = ("SELECT SERIAL_NO FROM VEHICLE")
            curs.execute(check)
            serial_no = 
    '''
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
    People_Information(curs,connection)
                  
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
            
    connection.close()

main()