import string



def getKeyToLenght(key, password):
    while len(key) <= len(password):
        key = key + key

    return key


def loadLetters():
    letters = string.ascii_letters
    letters = letters + string.digits
    letters = letters + string.punctuation
    try:
        with open("unknownLetters.csv", "r", encoding='utf-8') as f:
            for line in f.readline().split(","):
                
                letters = letters + line
    except:
        open("unknownLetters.csv", "w")
        print("file create")
    return letters


def addLetter(letter):
    try:
        with open("unknownLetters.csv", "a", encoding='utf-8') as f:
            f.write(letter+",")
    except:
        open("unknownLetters.csv", "w")
        print("file create")

def encrypt(password, key1):
    letters = loadLetters()
    key = getKeyToLenght(key1, password)
    passwordPositon =[]
    keyPositon =[]
    encrypted =""
    keyIsKnow =False
    for i2 in password:
    
        for i in range(len(letters)):
            if i2 == letters[i]:
                passwordPositon.append(i)
                keyIsKnow=True
                break
        if keyIsKnow == False:
            addLetter(i2)
            return encrypt(password, key)
            
        keyIsKnow = False
                
    for i2 in key:
    
        for i in range(len(letters)):
            if i2 == letters[i]:
                keyPositon.append(i)
    try:
        for i in range(len(password)):
            try:
                encrypted=encrypted+ str(letters[int(keyPositon[i]) +int(passwordPositon[i])])
            except:
                encrypted =encrypted+ str(letters[int(keyPositon[i]) +int(passwordPositon[i])-len(letters)])
    except:
        encrypt()
    return encrypted

def decrypt(passwordEncrypt, key1):
    letters = loadLetters()
    key = getKeyToLenght(key1, passwordEncrypt)
    passwordPositon =[]
    keyPositon =[]
    decrypted =""
    for i2 in passwordEncrypt:
    
        for i in range(len(letters)):
            if i2 == letters[i]:
                passwordPositon.append(i)
    for i2 in key:
    
        for i in range(len(letters)):
            if i2 == letters[i]:
                keyPositon.append(i)
    for i in range(len(passwordEncrypt)):
        try:
            decrypted=decrypted+ str(letters[int(passwordPositon[i]) -int(keyPositon[i])])
        except:
            decrypted =decrypted+ str(letters[int(passwordPositon[i]) -int(keyPositon[i])+len(letters)])
    return decrypted
    
