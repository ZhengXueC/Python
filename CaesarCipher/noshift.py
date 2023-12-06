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

def brute_force_decrypt(message):
    for shift in range(26):
        decrypted_message = decrypt(message, shift)
        print(f"Shift {shift}: {decrypted_message}")

def main():
    # Get input from the user
    message = input("Enter a message to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt(message, shift=3)  # You can choose any shift value here

    # Brute-force decrypt and print the results
    print("\nOriginal Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("\nBrute-force Decryption:")
    brute_force_decrypt(encrypted_message)

if __name__ == "__main__":
    main()
