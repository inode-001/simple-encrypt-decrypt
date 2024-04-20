import caesarCipher, reverseCipher

content = open("encrypted_ls.txt")
encrypted = caesarCipher.cipher(1, content, "encrypt")
reverseCipher.encrypt(encrypted)
print(encrypted)
