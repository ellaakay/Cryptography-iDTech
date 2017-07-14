
def xor(c1,c2):
    
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(c1,c2))


def slide(xored, index, word):
    for l in range(len(xored)):
        print len(xored) - l
        guess = word.ljust(len(xored) - l, ' ')
        guess = guess.rjust(len(xored), ' ')
        print 'cipher '+ str(index[0]) + ',' + str(index[1]) +' |', repr(xored)
        print 'guess  |', repr(guess)

        m = xor(xored, guess) # xored ^ the
        print 'm     |', repr(m)
        raw_input('waiting..')


#initial ciphers

cipherOne = '29044d472f1c0d4538161405017f0b0301532a1a1f3a4b0109570600061b51'

cipherTwo = '2e09410f1a1048113a0a551f0d30111c041d0a4f193a05554f3f3a4f19110f'

cipherThree = '050404035b0000003244001b452b0b4f111b0b4f00301b4e00117f1b1c155d'

cipherFour = '0e050d0b5754290b3b441d0e4532051d061b0b0b542b030b02573b00031e5d'

cipherFive = '070b000e155a48243100551c0d3a0a4f111b0b1654280e1c0a572a1f585009'

cipherSix = 'e0918470c111a007f110547451e0a0b4504060a1a7f1f060a0e7f18110218'

cipherSeven = '46080e101558481137010c4b123a160a451701181a734b2f01137f181c1513'

cipherEight = '4618090202541f002d0155040b331d4f0d12020959280a174f022f43542415'

cipherNine = '031541101e060d4531011c1f0d3a164f10034e011b2d4b0a00003141543f36'

#decoded cipher from hex

c1 = cipherOne.decode('hex')

c2 =cipherTwo.decode('hex')

c3 =cipherThree.decode('hex')

c4 =cipherFour.decode('hex')

c5 =cipherFive.decode('hex')

c6= cipherSix.decode('hex')

c7 =cipherSeven.decode('hex')

c8 =cipherEight.decode('hex')

c9 = cipherNine.decode('hex')

ciphers = [c1, c2, c3, c4, c5, c6, c7, c8, c9]




for i in range(len(ciphers)):
    print 'cipher text at index' + str(i) + ' with all'
    for index in range (len(ciphers)):
        guess = 'the'
        if i != index:
            ciphers_xored = xor(ciphers[i], ciphers[index])
            print xor(ciphers_xored, guess.ljust(len(ciphers_xored), '')).decode('string_escape')

        print guess.ljust(len(xor(ciphers[i],ciphers[index])),' ').decode('string_escape') + 'guess with padding'

        print '\n'
    
               
