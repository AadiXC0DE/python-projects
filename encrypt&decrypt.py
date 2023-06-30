def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message


message = input("Enter a message: ")
key = int(input("Enter a key (0-25): "))

encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
