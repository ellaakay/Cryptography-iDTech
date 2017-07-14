message = raw_input("enter your message: ")
e = 3
lst = []

decrypted = []
encrypted = []

def encrypt(a,b):
    n = a*b
    phi = (a-1)*(b-1)
    privExp = ((2 * ((a-1)*(b-1))) +1)/n
    
    for i in message:
        lst.append(ord(i))
    
    for i in lst:
        encrypted.append(i**e % n)
    print encrypted
    return privExp
    
def decrypt(a,b,c):
    n = a*b
    e = 3
    privExp = (2 * ((a-1)*(b-1)) +1)/e
 
    for i in c:
        decrypted.append(chr(i ** privExp % n))
    print decrypted
        
encrypt(53,59)
decrypt(53,59,encrypted)

