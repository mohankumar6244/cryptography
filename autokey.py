def encrypt(plaintext, key):
    extended_key = key + plaintext  # Append plaintext to the key
    ciphertext = ""
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(extended_key[i]) - ord('A')
        c = chr((p + k) % 26 + ord('A'))
        ciphertext += c
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    extended_key = key
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        k = ord(extended_key[i]) - ord('A')
        p = chr((c - k + 26) % 26 + ord('A'))
        plaintext += p
        extended_key += p  # Extend key with decrypted plaintext
    return plaintext

def main():
    plaintext = input("Enter plaintext (uppercase letters only): ").upper()
    key = input("Enter key (uppercase letters only): ").upper()
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()