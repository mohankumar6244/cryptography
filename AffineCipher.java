import java.util.Scanner;

public class AffineCipher {

    // Function to encrypt a plaintext using the Affine Cipher formula: c = (a * x + b) % 26
    public static String encrypt(String plaintext, int a, int b) {
        StringBuilder ciphertext = new StringBuilder();
        plaintext = plaintext.toUpperCase();

        for (char ch : plaintext.toCharArray()) {
            if (Character.isLetter(ch)) {
                int x = ch - 'A'; // Convert character to numerical value (0-25)
                int c = (a * x + b) % 26; // Apply Affine Cipher formula
                ciphertext.append((char) (c + 'A')); // Convert back to character
            } else {
                ciphertext.append(ch); // Append non-alphabetic characters unchanged
            }
        }
        return ciphertext.toString();
    }

    // Function to decrypt a ciphertext using the Affine Cipher formula: x = a_inv * (c - b) % 26
    public static String decrypt(String ciphertext, int a, int b) {
        StringBuilder plaintext = new StringBuilder();
        ciphertext = ciphertext.toUpperCase();

        int a_inv = findMultiplicativeInverse(a, 26); // Find modular multiplicative inverse of 'a'
        for (char ch : ciphertext.toCharArray()) {
            if (Character.isLetter(ch)) {
                int c = ch - 'A'; // Convert character to numerical value (0-25)
                int x = (a_inv * (c - b + 26)) % 26; // Apply decryption formula
                plaintext.append((char) (x + 'A')); // Convert back to character
            } else {
                plaintext.append(ch); // Append non-alphabetic characters unchanged
            }
        }
        return plaintext.toString();
    }

    // Function to find the modular multiplicative inverse of 'a' under modulo 'm'
    public static int findMultiplicativeInverse(int a, int m) {
        for (int i = 0; i < m; i++) {
            if ((a * i) % m == 1) {
                return i;
            }
        }
        throw new IllegalArgumentException("Multiplicative inverse does not exist for the given 'a' and 'm'.");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Affine Cipher constants
        int a = 3; // Multiplier
        int b = 12; // Shift

        // Input plaintext
        System.out.print("Enter the plaintext: ");
        String plaintext = scanner.nextLine();

        // Encrypt the plaintext
        String encryptedText = encrypt(plaintext, a, b);
        System.out.println("Encrypted Text: " + encryptedText);

        // Decrypt the ciphertext
        String decryptedText = decrypt(encryptedText, a, b);
        System.out.println("Decrypted Text: " + decryptedText);

        scanner.close();
    }
}
