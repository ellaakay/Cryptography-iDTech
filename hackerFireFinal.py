def xor(s1,s2):
    '''XOR two strings. Be sure to decode hex-encoded strings before using this'''
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def slide(xored, index, word):
    for l in range(len(xored)):
        print len(xored) - l
        crib = word.ljust(len(xored) - l, ' ')
        crib = crib.rjust(len(xored), ' ')
        print 'cipher '+ str(index[0]) + ',' + str(index[1]) +' |', repr(xored)
        print 'crib  |', repr(crib)

        m = xor(xored, crib) # xored ^ the
        print 'm     |', repr(m)
        raw_input('waiting..')

c1 = '29044d472f1c0d4538161405017f0b0301532a1a1f3a4b0109570600061b51'
c2 = '2e09410f1a1048113a0a551f0d30111c041d0a4f193a05554f3f3a4f19110f'
c3 = '050404035b0000003244001b452b0b4f111b0b4f00301b4e00117f1b1c155d'
c4 = '0e050d0b5754290b3b441d0e4532051d061b0b0b542b030b02573b00031e5d'
c5 = '070b000e155a48243100551c0d3a0a4f111b0b1654280e1c0a572a1f585009'
c6 = '0e0918470c111a007f110547451e0a0b4504060a1a7f1f060a0e7f18110218'
c7 = '46080e101558481137010c4b123a160a451701181a734b2f01137f181c1513'
c8 = '4618090202541f002d0155040b331d4f0d12020959280a174f022f43542415'
c9 = '031541101e060d4531011c1f0d3a164f10034e011b2d4b0a00003141543f36'

ciphers = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

# for first in range(len(ciphers)):
#     for second in range(len(ciphers)):
#         if first != second:
#             string = 'down'
#             ciphers_xored = xor(ciphers[first].decode('hex'), ciphers[second].decode('hex'))
#             print ciphers_xored.encode('string_escape')

# for ciphertext in range(len(ciphers)):
#     for ciphertext2 in range(len(ciphers)):
#         if ciphertext != ciphertext2:
#             slide(xor(ciphers[ciphertext].decode('hex'), ciphers[ciphertext2].decode('hex')), (ciphertext, ciphertext2), 'Oh, The')

# for i in range(len(ciphers)):
#     print 'cipher text at index ' + str(i) + ' with all'
#     for index in range(len(ciphers)):
#         #guess = 'Oh, the grand Duke of York'
#         #guess = 'He had ten thousand men;' 
#         #guess = 'top of the hill, '
#         #guess = 'And he marched them '
#         #guess = ' hill, And he marched them '
#         #guess = ' again. And when they were '
#         #guess = ' they were up, And when '
#         #guess = 'Oh, The grand old Duke of Y'
#         #guess = ' down, they were down, '
#         guess = ' they were only half-way up '
#         #guess = ' they were neither up nor down '
#         #guess = 'ched them up to the top;'
#         if i != index:
#             string = ''
#             ciphers_xored = xor(ciphers[i].decode('hex'), ciphers[index].decode('hex'))
#             print xor(ciphers_xored, guess.ljust(len(ciphers_xored), ' ')).decode('string_escape')
#     print guess.ljust(len(xor(ciphers[i].decode('hex'), ciphers[index].decode('hex'))), ' ').decode('string_escape') + 'guess with padding '
#     print '\n'


print xor(c1.decode('hex'),"Oh, The grand old Duke of York")



# Oh, The grand old Duke of York.  He had ten thousand men; He marched them up to the top of the hill, And he marched them down
# again. And when they were up they were up, And when they were down, they were down, And when they were half-way up, 
#they were neither up nor down.