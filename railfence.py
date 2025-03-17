def encrypt(plaintext, depth):
    rail = [['\n' for _ in range(len(plaintext))] for _ in range(depth)]
    down = False
    row, col = 0, 0

    for char in plaintext:
        if row == 0 or row == depth - 1:
            down = not down
        rail[row][col] = char
        col += 1
        row += 1 if down else -1

    ciphertext = ''.join(''.join(row) for row in rail if row)
    return ciphertext.replace('\n', '')

def decrypt(ciphertext, depth):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(depth)]
    down = False
    row, col = 0, 0

    # Mark positions to be filled
    for i in range(len(ciphertext)):
        if row == 0 or row == depth - 1:
            down = not down
        rail[row][col] = '*'
        col += 1
        row += 1 if down else -1

    index = 0
    # Fill rail with ciphertext characters
    for i in range(depth):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read in zig-zag order
    result = []
    row, col = 0, 0
    down = False
    for i in range(len(ciphertext)):
        if row == 0 or row == depth - 1:
            down = not down
        result.append(rail[row][col])
        col += 1
        row += 1 if down else -1

    return ''.join(result)

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    depth = int(input("Enter depth: "))

    ciphertext = encrypt(plaintext, depth)
    print("Ciphertext:", ciphertext)

    decrypted_text = decrypt(ciphertext, depth)
    print("Decrypted text:", decrypted_text)
