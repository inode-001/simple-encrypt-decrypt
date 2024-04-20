def cipher(key, message, mode):
    translated = ""
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 .?!",-+=@#$%^&*()[]{};/|'
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            if mode == "encrypt":
                newIndex = symbolIndex + key
            elif mode == "decrypt":
                newIndex = symbolIndex - key

            if newIndex >= len(SYMBOLS):
                newIndex = newIndex - len(SYMBOLS)
            elif newIndex < 0:
                newIndex = newIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[newIndex]
        else:
            translated = translated + symbol
    return translated


def bruteForce(message):
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 .?!"

    for key in range(len(SYMBOLS)):
        decrypted = ""
        for text in message:
            if text in SYMBOLS:
                textIndex = SYMBOLS.find(text)
                decryptIndex = textIndex - key
                if decryptIndex < 0:
                    decryptIndex = decryptIndex + len(SYMBOLS)
                decrypted += SYMBOLS[decryptIndex]
            else:
                decrypted += text
        print(f"Try:#{key} : {decrypted}")


def main():
    print("Welcome to caesar cipher".center(50, "*"), "\n\n")

    print(
        "Would you like to (input either 1 or 2): \n\t 1) Encrypt message \n\t 2) Decrypt Message \n\t 3) Brute force (in case you forgot the encryption key) \n\t 0) Exit"
    )

    option = str(input(": > "))

    if option == "1":
        mode = "encrypt"
        message = str(input("Enter message to encrypt : "))
        key = int(
            input("Enter key to use to encrypt the message : (use integers only) : ")
        )
        encrypted = cipher(key, message, mode)
        print(f"\nEncrypted message is : {encrypted}")

    elif option == "2":
        mode = "decrypt"
        message = str(input("Enter message to decrypt : "))
        key = int(
            input("Enter key used to decrypt the message : (use integers only) : ")
        )

        decrypted = cipher(key, message, mode)
        print(f"\nDecrypted message is :{decrypted}")
    elif option == "3":
        message = str(input("Enter message to bruteforce : "))
        bruteForce(message)
    elif option == "0":
        quit()

    else:
        print("\nInvalid option input either 1,2,3 or 0")


if __name__ == "__main__":
    main()
