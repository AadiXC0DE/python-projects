def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)


def main():
    while True:
        choice = input("Select an option (1: Encrypt, 2: Decrypt, 3: Quit): ")
        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            key = int(input("Enter the key (a number between 1 and 25): "))
            ciphertext = caesar_encrypt(plaintext, key)
            print("Ciphertext:", ciphertext)
        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            key = int(input("Enter the key (a number between 1 and 25): "))
            plaintext = caesar_decrypt(ciphertext, key)
            print("Plaintext:", plaintext)
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    print("Caesar Cipher")
    main()
