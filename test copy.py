cipher= "031541101e060d4531011c1f0d3a164f10034e011b2d4b0a00003141543f36"
import random

key = ""
cipher = cipher.decode('hex')




for i in range (len(cipher)):
    key += str(random.randint(0,9))

    print key

    

