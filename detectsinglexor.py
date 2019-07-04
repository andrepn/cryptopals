###pseudocode
#
#import from singlebytexorcipher
#
#read in ex4.txt line by line and create a list with each line
#
#loop through each line finding potential cipher based on probability
#
#choose line with the highest score and print

from singlebytexorcipher import english_score, xor_against_single_character, most_likely_text

#/PATH assuming file in the same directory
filepath = "ex4.txt"
textfile = open(filepath)

def most_likely_object(textfile):
    textlist = [x.strip() for x in textfile]
    #print(textlist[1,2,3])

    best_score = 0
    line_number = 0
    most_likely_line = {}

    for line in textlist:
        temp_key = most_likely_text(bytes.fromhex(line))
        #key = {"char": , "text": , "score": }

        if temp_key.get("score", 0) > best_score:
            best_score = temp_key.get("score", 0)
            most_likely_line = {**temp_key, "line_number": line_number}  #add "line" so we can see which line was encrypted

        line_number += 1

    return most_likely_line


solution = most_likely_object(textfile)
print(solution)

assert solution.get("text", 0).strip() == b"Now that the party is jumping"
