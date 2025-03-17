def encrypt(plaintext, a, b):
    ciphertext = ""
    plaintext = plaintext.upper()
    
    for ch in plaintext:
        if ch.isalpha():
            x = ord(ch) - ord('A')  # Convert character to numerical value (0-25)
            c = (a * x + b) % 26  # Apply Affine Cipher formula
            ciphertext += chr(c + ord('A'))  # Convert back to character
        else:
            ciphertext += ch  # Append non-alphabetic characters unchanged
    
    return ciphertext


def decrypt(ciphertext, a, b):
    plaintext = ""
    ciphertext = ciphertext.upper()
    
    a_inv = find_multiplicative_inverse(a, 26)  # Find modular multiplicative inverse of 'a'
    for ch in ciphertext:
        if ch.isalpha():
            c = ord(ch) - ord('A')  # Convert character to numerical value (0-25)
            x = (a_inv * (c - b + 26)) % 26  # Apply decryption formula
            plaintext += chr(x + ord('A'))  # Convert back to character
        else:
            plaintext += ch  # Append non-alphabetic characters unchanged
    
    return plaintext


def find_multiplicative_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    raise ValueError("Multiplicative inverse does not exist for the given 'a' and 'm'.")


def main():
    a = 3  # Multiplier
    b = 12  # Shift
    
    plaintext = input("Enter the plaintext: ")
    encrypted_text = encrypt(plaintext, a, b)
    print("Encrypted Text:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, a, b)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
