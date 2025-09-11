from src.encryptor import Encryptor
from src.encryption_schemes import ENCRYPTION_SCHEMES

def main():
    # --- Configuration ---
    # The plaintext message to be encrypted
    plaintext = "This is a secret message for the machine learning model to analyze."

    # The fixed seed for the random number generator to ensure reproducibility
    seed = 42

    # Output file paths
    output_file = "output/encrypted_message.txt"
    log_file = "output/encryption_log.csv"

    # --- Execution ---
    # Initialize the encryptor with the available schemes and the seed
    encryptor = Encryptor(schemes=ENCRYPTION_SCHEMES, seed=seed)

    # Run the encryption process
    encryptor.encrypt(
        plaintext=plaintext,
        output_path=output_file,
        log_path=log_file
    )

if __name__ == "__main__":
    main()
