def substitution_cipher_encrypt(plaintext, substitution_map):
    """
    Encrypts the given plaintext using the provided substitution map.

    :param plaintext: The input text to encrypt.
    :param substitution_map: A dictionary mapping plaintext characters to their substitutions.
    :return: Encrypted ciphertext.
    """
    ciphertext = ""
    for char in plaintext:
        # Substitute only if the character exists in the map, otherwise leave it unchanged
        ciphertext += substitution_map.get(char, char)
    return ciphertext

def substitution_cipher_decrypt(ciphertext, substitution_map):
    """
    Decrypts the given ciphertext using the provided substitution map.

    :param ciphertext: The input text to decrypt.
    :param substitution_map: A dictionary mapping plaintext characters to their substitutions.
    :return: Decrypted plaintext.
    """
    # Reverse the substitution map for decryption
    reverse_map = {value: key for key, value in substitution_map.items()}
    plaintext = ""
    for char in ciphertext:
        # Substitute only if the character exists in the reversed map, otherwise leave it unchanged
        plaintext += reverse_map.get(char, char)
    return plaintext

# Example usage
if __name__ == "__main__":
    # Define a substitution map (example mapping for simplicity)
    substitution_map = {
        'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U',
        'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O',
        'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I',
        'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C',
        'Y': 'B', 'Z': 'A'
    }

    # Take input from the keyboard
    plaintext = input("Enter the plaintext: ").upper()

    # Encrypt the plaintext
    encrypted_text = substitution_cipher_encrypt(plaintext, substitution_map)
    print("Encrypted Text:", encrypted_text)

    # Decrypt the ciphertext
    decrypted_text = substitution_cipher_decrypt(encrypted_text, substitution_map)
    print("Decrypted Text:", decrypted_text)
