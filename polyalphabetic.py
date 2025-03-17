def vigenere_encrypt(plaintext, keyword):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = plaintext.upper().replace(' ', '')
    keyword = keyword.upper().replace(' ', '')
    ciphertext = []

    keyword_repeated = (keyword * ((len(plaintext) // len(keyword)) + 1))[:len(plaintext)]

    for p_char, k_char in zip(plaintext, keyword_repeated):
        p_index = alphabet.index(p_char)
        k_index = alphabet.index(k_char)
        c_index = (p_index + k_index) % 26
        ciphertext.append(alphabet[c_index])

    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, keyword):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ciphertext.upper().replace(' ', '')
    keyword = keyword.upper().replace(' ', '')
    plaintext = []

    keyword_repeated = (keyword * ((len(ciphertext) // len(keyword)) + 1))[:len(ciphertext)]

    for c_char, k_char in zip(ciphertext, keyword_repeated):
        c_index = alphabet.index(c_char)
        k_index = alphabet.index(k_char)
        p_index = (c_index - k_index + 26) % 26
        plaintext.append(alphabet[p_index])

    return ''.join(plaintext)

if __name__ == "__main__":
    choice = input("Choose (E)ncrypt or (D)ecrypt: ").upper()
    if choice == 'E':
        plaintext = input("Enter the plaintext: ")
        keyword = input("Enter the keyword: ")
        encrypted_message = vigenere_encrypt(plaintext, keyword)
        print(f"Ciphertext: {encrypted_message}")
    elif choice == 'D':
        ciphertext = input("Enter the ciphertext: ")
        keyword = input("Enter the keyword: ")
        decrypted_message = vigenere_decrypt(ciphertext, keyword)
        print(f"Plaintext: {decrypted_message}")
    else:
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")
