def encrypt_message(key, message):
    cipherText = [""] * key
    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]

            currentIndex += key

    return "".join(cipherText)
