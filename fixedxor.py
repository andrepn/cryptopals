###pseudocode
#
#start with two hexstrings
#
#hexstrings to bytes
#
#bitwise XOR
#
#bytes to hex

hexstring1 = "1c0111001f010100061a024b53535009181c"
hexstring2 = "686974207468652062756c6c277320657965"
correctxorstring = "746865206b696420646f6e277420706c6179"

def xor_bytes(bytes1, bytes2):
    xor_bytes = b""

    #take tuples of bytes in order and apply bitwise xor (^)
    for x,y in zip(bytes1, bytes2):
        xor_bytes += bytes([x ^ y])

    return xor_bytes

#hex -> bytes
hexbytes1 = bytes.fromhex(hexstring1)
hexbytes2 = bytes.fromhex(hexstring2)

#print(hexbytes1)
#print(hexbytes2)

xor_bytes = xor_bytes(hexbytes1, hexbytes2)

#print(xor_bytes)

#bytes -> hex
xor_string = xor_bytes.hex()

assert xor_string == correctxorstring

#print(xor_string)
