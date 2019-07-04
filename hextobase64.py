###pseudocode
#
#start with hexidecimal string
#
#convert string to bytes
# f: character -> 4-bit
#
#convert bytes to base64
# g: 6-bit -> character

import base64

#initial input as string
hexstr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
correctbase64str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hex_to_base64(hexidecimal_string):

    #string -> bytes
    hexbytes = bytes.fromhex(hexstr)

    #hexbytes -> base64bytes
    base64bytes = base64.b64encode(hexbytes)

    #base64bytes -> string
    base64str = base64bytes.decode('utf-8')

    #print(hexbytes)
    #print(base64bytes)

    return base64str

#check function result
assert correctbase64str == hex_to_base64(hexstr)

print("The function works")

#To be more thorough could read in a whole list of hexstr and correctbase64str
