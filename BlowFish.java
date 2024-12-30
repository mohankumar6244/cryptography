import java.io.*;
import java.security.Key;
import javax.crypto.Cipher;
import javax.crypto.CipherOutputStream;
import javax.crypto.KeyGenerator;
import java.util.Base64;

public class BlowFish {
    public static void main(String[] args) {
        try {
            // Generate Blowfish Key
            KeyGenerator keyGenerator = KeyGenerator.getInstance("Blowfish");
            keyGenerator.init(128);
            Key secretKey = keyGenerator.generateKey();
            
            // Initialize Cipher
            Cipher cipherOut = Cipher.getInstance("Blowfish/CFB/NoPadding");
            cipherOut.init(Cipher.ENCRYPT_MODE, secretKey);
            
            // Print IV
            byte[] iv = cipherOut.getIV();
            if (iv != null) {
                System.out.println("Initialization Vector: " + Base64.getEncoder().encodeToString(iv));
            }

            // Open File Streams
            FileInputStream fin = new FileInputStream("inputFile.txt");
            FileOutputStream fout = new FileOutputStream("outputFile.txt");
            CipherOutputStream cout = new CipherOutputStream(fout, cipherOut);

            // Read and Encrypt File
            int input;
            while ((input = fin.read()) != -1) {
                cout.write(input);
            }

            // Close Streams (Important)
            fin.close();
            cout.close();  // Ensures all bytes are flushed to the file
            
            System.out.println("File Encrypted Successfully!");
            
        } catch (FileNotFoundException e) {
            System.err.println("File not found. Ensure inputFile.txt exists.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}