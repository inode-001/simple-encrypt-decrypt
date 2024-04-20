import random, sys, transposition_decrypt, transpostionEncrypt


def main():
    random.seed(40)

    for i in range(20):
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4, 40)
        print(message)
        message = list(message)

        random.shuffle(message)
        message = "".join(message)

        print(f'Test #{i + 1}: "{message[:50]}"')

        for key in range(1, int(len(message) / 2)):
            encrypted = transpostionEncrypt.encrypt_message(key, message)
            decrypted = transposition_decrypt.decrypt_message(key, encrypted)

            if message != decrypted:
                print(f"Mismatch  with key {key} and message {message}")
                print("Decrypted as : " + decrypted)
                sys.exit()

    print("Transpostion cipher test passed")
    print('"')


if __name__ == "__main__":
    main()
