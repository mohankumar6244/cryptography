import math

def get_key_order(key):
    return [sorted(key).index(k) for k in key]

def single_transposition(text, key):
    key_order = get_key_order(key)
    rows = math.ceil(len(text) / len(key))
    grid = [['X' for _ in range(len(key))] for _ in range(rows)]

    index = 0
    for i in range(rows):
        for j in range(len(key)):
            if index < len(text):
                grid[i][j] = text[index]
                index += 1

    ciphertext = ''.join(grid[i][col] for col in key_order for i in range(rows))
    return ciphertext

def single_decryption(text, key):
    key_order = get_key_order(key)
    rows = len(text) // len(key)
    grid = [['' for _ in range(len(key))] for _ in range(rows)]

    index = 0
    for col in key_order:
        for i in range(rows):
            grid[i][col] = text[index]
            index += 1

    plaintext = ''.join(grid[i][j] for i in range(rows) for j in range(len(key)))
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    key1 = input("Enter the first key: ")
    key2 = input("Enter the second key: ")

    # Perform double encryption
    intermediate_cipher = single_transposition(plaintext, key1)
    final_cipher = single_transposition(intermediate_cipher, key2)
    print("Ciphertext:", final_cipher)

    # Perform double decryption
    intermediate_plain = single_decryption(final_cipher, key2)
    original_plain = single_decryption(intermediate_plain, key1)
    print("Decrypted Text:", original_plain)
