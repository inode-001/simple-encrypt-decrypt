def encrypt(message):
    translated = message[::-1]
    return translated
def decrypt(message):
      translated = message[::-1]
      return translated


print("Welcome to reverse cipher".center(50,'*'),"\n\n")

print("Would you like to (input either 1 or 2): \n\t 1) Encrypt message \n\t 2) Decrypt Message")

option = str(input(": > "))

if option == '1':
     message = input("Enter message to encrypt : ")
     encrypted = encrypt(message)
     print(f"\nEncrypted message is : {encrypted}")

elif option == "2":
     message = input("Enter message to decrypt : ")
     decrypted = decrypt(message)
     print(f"\nDecrypted message is : {decrypted}")

else:
     print("\nInvalid option input either 1 or 2")