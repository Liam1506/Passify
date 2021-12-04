import os
from liCrypt import *
command, password, securityNumber, verification = input("Link: ").split(";")

# command = ["GET, POST, REQUEST"] => return operation
# password = password for website, which is requested 
# securitiNumber = number, to check that the pc is authorised to get passwort
# verification = name of file, where the password will be stored

if command == "POST":
    
    try:
		#print("Finish Writing")
        bytesOfArray = password.split("-")

        
        array2 = []
        bytesOfArray.pop(len(bytesOfArray)-1)
        bytesOfArray.pop(0)
        print(bytesOfArray)
        for i in bytesOfArray:
            array2.append(int(i))

    	
        finalString = bytes(array2)
        #print(finalString.decode("utf-8"))


        with open("keys2021//"+securityNumber+".py", "w", encoding='utf-8') as f:
            verify = verification.split(",")
            f.write(encrypt(finalString.decode("utf-8"), verify[1])+";zap;"+verify[0])
    except Exception as e:
        print("{ \n "+'"'+"result"+'"' +": "+'"'+str(e)+'"'+"\n }")
		#print("Finish Writing")
elif command == "GET":
    try:
        with open("keys2021//"+securityNumber+".py", "r", encoding='utf-8') as f:
            code, verificationNumber = f.readline().split(";zap;")
            verify = verification.split(",")
        if verificationNumber == verify[0]:
            #print(decrypt(code, verify[1]))

            password = decrypt(code, verify[1])
            if password[0] == "}":
                password = r=password[:0]+password[1:]
                
            print("{ \n "+'"'+"result"+'"' +": "+'"'+password+'"'+"\n }")
            with open("keys2021//"+securityNumber+".py", "w") as f2:

                f2.write("Access denied")
            


        else:
            print("{ \n "+'"'+"result"+'"' +": "+'"'+"Access denied"+'"'+"\n }")
    except Exception as e:
        print("{ \n "+'"'+"result"+'"' +": "+'"'+"Access denied"+'"'+"\n }")












