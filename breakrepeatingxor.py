###pseudocode
#
#read in file convert to ciphertext
#
#start with list of potential key sizes
#
#function to compute hamming distance
#
#function to randomly select 3 keysize of bytes then compute normalized distance for all
#combinations then compute average -> return list (keysize, normal-distance)
#
#function to test all keysizes and select the one with the lowest distance
#
#break ciphertext into blocks of keysize length
#
#now create transposed blocks and xor them looking for most likely key, single char xor on each list works bc we know the key repeats
#
#collect the chars from each one to create the key

import base64
from singlebytexorcipher import most_likely_text
from imprepeatingkeyxor import repeating_key_encryption

#/PATH assuming file in the same directory
filepath = "ex6.txt"
with open(filepath, "r") as textwrapper:
    textfile = textwrapper.read()

#number of blocks to determine min distrance
number_of_blocks = 4

testbytestring1 = b"this is a test"
testbytestring2 = b"wokka wokka!!!"

cipher = base64.b64decode(textfile)

#print(cipher[40])

keysizelist = range(1, 40)

#function to calculate hamming distance
def hamming_distance(bytes1, bytes2):
    hamming_distance = 0

    for x,y in zip(bytes1, bytes2):
        binary = bin(x ^ y)
        for bit in binary:
            if bit == "1":
                hamming_distance += 1

    return hamming_distance

#test hamming_distance
assert hamming_distance(testbytestring1, testbytestring2) == 37

#function to choose first blocks of x length and normalize distance between them
def blocks_hamming_distances(number_of_blocks, keysize, cipher): #cipher must be bytes
    list_of_blocks = []
    hdistsum = 0

    for i in range(number_of_blocks):
        newblock = cipher[i*keysize : (i+1)*keysize]
        list_of_blocks.append(newblock)

    for blockm in list_of_blocks:
        for blockn in list_of_blocks:
            normhdist = (hamming_distance(blockm, blockn)/keysize)
            hdistsum += normhdist

    return hdistsum


##### on paper I know that with keysize = 1, ciper = b'0110, number_of_blocks = 3 the answer is 4
assert blocks_hamming_distances(number_of_blocks = 3, keysize = 1, cipher = b"0110") == 4

#function to cycle through list of possible keysizes and choose the one with minimum distance
def choose_best_keysize(number_of_blocks, keysizelist, cipher):
    best_keysize = 0
    min_distance = len(keysizelist)*number_of_blocks

    for keysize in keysizelist:
        hdist = blocks_hamming_distances(number_of_blocks, keysize, cipher)

        if hdist < min_distance:
            min_distance = hdist
            best_keysize = keysize

    return best_keysize

#function that will take nth element of each block of keysize and create lists with those elements
#then it runs single char xor to attempt to find the key
def transpose_blocks_then_xor(keysize, cipher):
    keys = b''

    for index in range(keysize):
        transposed_block = b""
        #here we round down to the nearest int to avoid overindexing
        for element in range(index, len(cipher), keysize):
            #make a block with all the elements of cipher modulo index
            transposed_block += bytes([cipher[element]])

            #print(bytes([cipher[element]]))
            #print(transposed_block)

        keys += bytes([most_likely_text(transposed_block)["char"]])

    return keys

#run the loop
bestkey = choose_best_keysize(number_of_blocks, keysizelist, cipher)
print(bestkey)
key = transpose_blocks_then_xor(bestkey, cipher)
print(key)

assert key == b"Terminator X: Bring the noise"
