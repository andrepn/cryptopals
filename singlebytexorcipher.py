###pseudocode
#
#start with hexstring and most common letters in english language
#
#function to score English
    #score = sum(letterprobabilities)   #note second order would be stronger but wouldn't use the US army to kill an ant
#
#funtion to xor against a single character
#
#function loop to try every single character xor then give  English score
#
#convert string to bytes
#
#put bytes into loop
#
#select max score string with index cipher

from fixedxor import xor_bytes

#googled until I found this dictionary for copy/paste
#https://github.com/ricpacca/cryptopals/blob/master/S1C03.py
#http://www.data-compression.com/english.html
Character_Freq = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

hexstring = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

#function to assign a string a likelihood of being english
def english_score(input_bytes):
    score = 0

    #use lowercase character as key to add first order likelihood of a letter
    for byte in input_bytes:
        score += Character_Freq.get(chr(byte).lower(), 0)

    return score

#function to xor a string of bytes against one character
def xor_against_single_character(input_bytes, character):
    xor_bytes = b""

    for byte in input_bytes:
        xor_bytes += bytes([byte ^ character])

    return xor_bytes

#function to loop through all 256 possible character ciphers and return object with likey key and plaintext
def most_likely_text(encrypted_bytes):
    max_likelihood_cipher = {}
    best_score = 0

    for num in range(256):
        temp_xor_bytes = xor_against_single_character(encrypted_bytes, num)
        temp_score = english_score(temp_xor_bytes)

        temp = {
            "char" : num,
            "text" : temp_xor_bytes,
            "score" : temp_score  #only returning this in case needed later
        }

        if temp_score >= best_score:
            max_likelihood_cipher = temp
            best_score = temp_score

    return max_likelihood_cipher #could also return full list easily if this one wasnt right

#hex -> bytes
hexbytes = bytes.fromhex(hexstring)
key = most_likely_text(hexbytes)

#check it worked
assert key.get("text") == b"Cooking MC's like a pound of bacon"

#print("the deciphered sentence is", format(key.get("text").decode()))
#print("the key is", format(chr(key.get("char")).lower()))
