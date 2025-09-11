import random
import csv
from src.encryption_schemes import ENCRYPTION_SCHEMES

class Encryptor:
    def __init__(self, schemes, seed):
        """
        Initializes the Encryptor with a set of encryption schemes and a fixed seed.
        """
        self.schemes = schemes
        self.seed = seed
        random.seed(self.seed)

    def encrypt(self, plaintext, output_path, log_path):
        """
        Encrypts the plaintext character by character using randomly selected schemes.
        - plaintext: The string to encrypt.
        - output_path: The file path to save the encrypted text.
        - log_path: The file path to save the encryption log.
        """
        ciphertext = []
        log_data = []

        scheme_names = list(self.schemes.keys())

        for char in plaintext:
            # Randomly select a scheme
            scheme_name = random.choice(scheme_names)
            scheme_func = self.schemes[scheme_name]

            # Encrypt the character
            encrypted_char = scheme_func(char)

            # Append to results
            ciphertext.append(str(encrypted_char))
            log_data.append({'character': char, 'scheme': scheme_name})

        # Write ciphertext to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("".join(ciphertext))

        # Write log to CSV file
        with open(log_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['character', 'scheme'])
            writer.writeheader()
            writer.writerows(log_data)

        print(f"Encryption complete. Ciphertext saved to {output_path}")
        print(f"Log file saved to {log_path}")
