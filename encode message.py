#c=(x-n)%26
def encrypted(string,key):
    cipher=''
    for char in string:
        if char==" ":
            cipher=cipher+char
        elif char.isupper():
            cipher=cipher+chr((ord(char)+key-65)%26+65)
        else:
            cipher=cipher+chr((ord(char)+key-97)%26+97)
    return cipher

text=input("Enter message to encrypt: ")
s=int(input("Enter the key: "))
print("The encrypted message is: ",encrypted(text,s))
