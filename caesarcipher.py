# Read the encoded message
encoded_message = input()

# Read the key as an integer
key = input()

try:
    key = int(key)
    decoded_message = ""

    for char in encoded_message:
        if char.isalpha():
            # Determine the case of the character (upper or lower)
            is_upper = char.isupper()
            
            # Convert the character to its ASCII code
            char_code = ord(char.lower())

            # Decrypt the character by shifting it back with the key
            decrypted_char_code = char_code - key

            # Wrap around the alphabet if needed
            if decrypted_char_code < ord('a'):
                decrypted_char_code += 26

            # Convert the decrypted character code back to a character
            decrypted_char = chr(decrypted_char_code)

            # Restore the original case (upper or lower)
            if is_upper:
                decrypted_char = decrypted_char.upper()

            decoded_message += decrypted_char
        else:
            # If the character is not a letter, keep it unchanged
            decoded_message += char

    print(decoded_message)
except ValueError:
    print("Invalid input")
