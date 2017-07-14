message = raw_input("Please enter the string you would like to decrypt")

import string
ignoreChar = string.digits + string.punctuation + string.whitespace

encrypted = " "

for shift in range (1,26):
        for letter in message:

                if (ord(letter) - shift >= 97):

                        encrypted += chr(ord(letter)-shift)
        
                else:
                        encrypted += chr(122-97%(ord(letter)-shift))

        encrypted += '\n'
print encrypted

#"uapv{ndj'kt_qtvjc_ndjg_rgneid_psktcijgth}"                              

print "?".decode('base64')                        
















