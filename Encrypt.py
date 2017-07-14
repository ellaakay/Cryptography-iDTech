import string

ignoreChars = string.digits + string.punctuation + string.whitespace

message = raw_input("Input the string that you would like to encrypt: ").lower()
shift = int(raw_input("Input the shift that you would like to apply: "))
encrypted = " "

for letter in message:

    if (ord(letter)+shift) >= 122:

       encrypted += chr((97 - 1) + (ord(letter) + shift) % 122)

    else:
        encrypted += chr(ord(letter) + shift)
        

print encrypted


    
        
