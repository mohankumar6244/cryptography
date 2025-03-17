import math

def get_key_order(key):
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    return [i for i, _ in key_order]

def encrypt(plaintext, key):
    key_order = get_key_order(key)
    rows = math.ceil(len(plaintext) / len(key))
    grid = [['X' for _ in range(len(key))] for _ in range(rows)]

    index = 0
    for i in range(rows):
        for j in range(len(key)):
            if index < len(plaintext):
                grid[i][j] = plaintext[index]
                index += 1

    ciphertext = ''.join(grid[i][col] for col in key_order for i in range(rows))
    return ciphertext

def decrypt(ciphertext, key):
    key_order = get_key_order(key)
    rows = len(ciphertext) // len(key)
    grid = [['' for _ in range(len(key))] for _ in range(rows)]

    index = 0
    for col in key_order:
        for i in range(rows):
            grid[i][col] = ciphertext[index]
            index += 1

    plaintext = ''.join(grid[i][j] for i in range(rows) for j in range(len(key)))
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
