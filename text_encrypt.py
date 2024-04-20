import time, os, sys, transpostionEncrypt, transposition_decrypt


def main():
    file_to_encrypt = "ls.txt"
    file_name_after_encrytion = "encrypted_ls.txt"

    encryption_key = 17

    # mode to uses encryt or decrypt

    mode = "decrypt"

    if not os.path.exists(file_to_encrypt):
        print(f"The file {file_to_encrypt} is non-existent.Exiting the program....")
        sys.exit()

    if os.path.exists(file_name_after_encrytion):
        print(
            f"This will overwrite data in the file {file_name_after_encrytion}.(C)ontinue or (Q)uit ? "
        )

        user_command = input(":> ")

        if not user_command.lower().startswith("c"):
            sys.exit()

    read_file = open(file_to_encrypt)

    data_in_file = read_file.read()

    read_file.close()

    print(f"{mode.title()}ing")

    starting_time = time.time()

    if mode == "encrypt":
        translated_text = transpostionEncrypt.encrypt_message(
            encryption_key, data_in_file
        )
    elif mode == "decrypt":
        translated_text = transposition_decrypt.decrypt_message(
            encryption_key, data_in_file
        )

    total_amount_of_time = time.time() - starting_time

    print(f"{mode.title()}ion time : {total_amount_of_time} seconds")

    with open(f"{file_name_after_encrytion}", "w") as wr:
        wr.write(translated_text)

    print(f"Done {mode}ing {file_to_encrypt} {len(data_in_file)} characters")
    print(f"{mode.title()}ed file is {file_name_after_encrytion}")


if __name__ == "__main__":
    main()
