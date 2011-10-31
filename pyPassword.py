def asciiToPass(asciiPass):
    tmp = ''
    asciiPass = asciiPass.replace(","," ")
    for i in asciiPass.split():
        tmp += chr(int(i))
        return tmp

def passToAscii(password):
    #temp = ''
    strpass = ''
    for i in password:
        #temp += str(ord(i)-120) + ','
        asci = chr(ord(i)-120)
        strpass += asci
        #print(strpass)
    return strpass

def getInputText(password):
    print("=============================================================")
    print("Password: {0}".format(password))
    print("_____________________________________________________________")
    print (">>" + passToAscii(password))
    print("=============================================================")
    
def main():    
	while True:
		#Pide ingresar el password que esta 'encriptado'
		print("Ingresa password")		
		password = input()
		getInputText(password)	
	
	
main()
