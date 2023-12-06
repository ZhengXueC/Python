def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    # Get input from the user
    message = input("Enter a message to encrypt: ")
    shift = int(input("Enter shift value: "))

    # Encrypt and decrypt the message
    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)

    # Print the results
    print("\nOriginal Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()

