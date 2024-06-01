def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("Caesar Cipher Program")
    while True:
        choice = input(
            "Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice in ['E', 'D']:
            message = input("Enter your message: ")
            shift = int(input("Enter shift value: "))
            if choice == 'E':
                result = encrypt(message, shift)
                print(f"Encrypted message: {result}")
            else:
                result = decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice, please select either 'E' or 'D'.")

        another = input(
            "Do you want to process another message? (yes/no): ").lower()
        if another != 'yes':
            break


if __name__ == "__main__":
    main()
