import math

def decrypt_message(key,message):
    # determine number of colums
    numOfColumns = int(math.ceil(len(message) / float(key)))
    normalText = [''] * numOfColumns # represent the grid in form of an array
    numOfRows = key
    # find number of boxes in the grid that wont be used to decrypt the message
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    columm = 0
    row = 0

    for symbol in message:
       normalText[columm] += symbol
       columm +=1
       # checks if we have reached the rows with the unused grid boxes if so we skip them
       if (columm == numOfColumns) or (columm ==  numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
           columm = 0
           row += 1
    return ''.join(normalText)

message = str(input("Enter Message to Decrypt : "))
key = int(input("Enter encryption key : "))
print(f"Decrypted message is : {decrypt_message(key,message)}")
