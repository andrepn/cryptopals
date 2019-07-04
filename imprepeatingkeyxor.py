###pseudocode
#
#start with string to encrypt and repeating key
#
#convert string and key to bytes
#
#function to select next byte from string and modulo the key

string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
repeatkey = "ICE"
correctencryption = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

def repeating_key_encryption(bytestring, byterepeatkey):
    encrypted_bytes = b""

    for i in range(len(bytestring)):
        #print(i % len(byterepeatkey))
        encrypted_bytes += bytes([bytestring[i] ^ byterepeatkey[i % len(byterepeatkey)]])

    return encrypted_bytes

bytestring = string.encode()
byterepeatkey = repeatkey.encode()

encrypted = repeating_key_encryption(bytestring, byterepeatkey)
solution = bytes.hex(encrypted)

#print(encrypted)
#print(solution)

assert solution == correctencryption
