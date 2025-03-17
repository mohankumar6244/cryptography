import re

# Generate key matrix
def generate_key_matrix(key):
    key = key.lower().replace("j", "i")
    key_matrix = []
    visited = set()

    for ch in key:
        if ch.isalpha() and ch not in visited:
            key_matrix.append(ch)
            visited.add(ch)

    for ch in "abcdefghiklmnopqrstuvwxyz":
        if ch not in visited:
            key_matrix.append(ch)

    return [key_matrix[i * 5:(i + 1) * 5] for i in range(5)]

# Find coordinates of a character in the key matrix
def find_coordinates(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None

# Encrypt the text
def encrypt(text, key_matrix):
    text = re.sub(r'[^a-zA-Z]', '', text.lower()).replace("j", "i")
    if len(text) % 2 != 0:
        text += 'x'

    encrypted_text = []
    for i in range(0, len(text), 2):
        coord1 = find_coordinates(key_matrix, text[i])
        coord2 = find_coordinates(key_matrix, text[i + 1])

        if coord1[0] == coord2[0]:  # Same row
            encrypted_text.append(key_matrix[coord1[0]][(coord1[1] + 1) % 5])
            encrypted_text.append(key_matrix[coord2[0]][(coord2[1] + 1) % 5])
        elif coord1[1] == coord2[1]:  # Same column
            encrypted_text.append(key_matrix[(coord1[0] + 1) % 5][coord1[1]])
            encrypted_text.append(key_matrix[(coord2[0] + 1) % 5][coord2[1]])
        else:  # Rectangle rule
            encrypted_text.append(key_matrix[coord1[0]][coord2[1]])
            encrypted_text.append(key_matrix[coord2[0]][coord1[1]])

    return ''.join(encrypted_text)

# Decrypt the text
def decrypt(text, key_matrix):
    decrypted_text = []
    for i in range(0, len(text), 2):
        coord1 = find_coordinates(key_matrix, text[i])
        coord2 = find_coordinates(key_matrix, text[i + 1])

        if coord1[0] == coord2[0]:  # Same row
            decrypted_text.append(key_matrix[coord1[0]][(coord1[1] - 1) % 5])
            decrypted_text.append(key_matrix[coord2[0]][(coord2[1] - 1) % 5])
        elif coord1[1] == coord2[1]:  # Same column
            decrypted_text.append(key_matrix[(coord1[0] - 1) % 5][coord1[1]])
            decrypted_text.append(key_matrix[(coord2[0] - 1) % 5][coord2[1]])
        else:  # Rectangle rule
            decrypted_text.append(key_matrix[coord1[0]][coord2[1]])
            decrypted_text.append(key_matrix[coord2[0]][coord1[1]])

    return ''.join(decrypted_text)

if __name__ == "__main__":
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")

    key_matrix = generate_key_matrix(key)
    encrypted_text = encrypt(plaintext, key_matrix)
    decrypted_text = decrypt(encrypted_text, key_matrix)

    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
