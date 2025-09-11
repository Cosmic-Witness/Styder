# Styder: A Stochastic Encryption Scheme

Styder is a custom-built stochastic encryption tool designed for research and analysis, particularly for machine learning applications. It encrypts a given text character by character, with each character being processed by a randomly selected encryption scheme from a predefined pool. The randomization is controlled by a fixed seed, ensuring that the encryption process is reproducible, which is vital for analyzing the resulting ciphertext with machine learning models.

## How It Works

The core of Styder is a character-by-character encryption loop. For each character in the input plaintext, the system randomly chooses one of the available encryption schemes and applies it. This process generates a highly randomized ciphertext that is non-trivial to reverse without understanding the underlying patterns.

To allow for analysis, the system also generates a detailed log file that records which encryption scheme was used for each character. This log, along with the seeded nature of the randomization, provides a clear path for a machine learning model to study the "stochastic landscape" of the ciphertext.

### Key Features

- **Stochastic Encryption:** Each character is encrypted with a randomly chosen scheme.
- **Reproducibility:** A fixed seed ensures the same output for the same input, which is crucial for ML model training.
- **Diverse & Simple Schemes:** The pool of encryption methods is intentionally diverse but lightweight to ensure efficiency.
- **Detailed Logging:** A CSV log file maps each character to the scheme that encrypted it.
- **Modular Design:** The encryption schemes are designed to be swappable, making it easy to add, remove, or modify them without changing the core encryption logic.

## Project Structure

The project is organized into the following directories and files:

- `src/`: Contains the main source code.
  - `encryption_schemes.py`: Defines the pool of available encryption schemes. Each scheme is a separate function with a unified interface.
  - `encryptor.py`: Contains the main `Encryptor` class that orchestrates the encryption process.
- `main.py`: The main execution script to run the encryption.
- `output/`: The default directory for the output files.
  - `encrypted_message.txt`: The generated ciphertext.
  - `encryption_log.csv`: The log file detailing the encryption process.
- `README.md`: This file, providing a detailed overview of the project.

## The Encryption Schemes

The following encryption schemes are currently implemented in `src/encryption_schemes.py`:

1.  **Shift Cipher (Caesar Cipher):**
    - **Description:** Shifts the character's ASCII value by a fixed key (default is 3).
    - **Nature:** A simple substitution cipher based on a linear shift.

2.  **XOR Cipher:**
    - **Description:** Performs a bitwise XOR operation on the character's ASCII value with a fixed key (default is `0x5A`).
    - **Nature:** A symmetric-key algorithm that is simple and fast.

3.  **Simple Substitution Cipher:**
    - **Description:** Replaces characters based on a fixed substitution map (e.g., 'a' becomes 'z', 'b' becomes 'y').
    - **Nature:** A classic substitution cipher with a predefined, non-linear mapping.

4.  **Base64 Encoding:**
    - **Description:** Encodes the character into its Base64 representation.
    - **Nature:** A data encoding scheme, not true encryption, but adds diversity to the output format.

5.  **Bit Reversal:**
    - **Description:** Reverses the bits of the character's 8-bit ASCII representation.
    - **Nature:** A simple bitwise manipulation that obfuscates the character's value.

## How to Run the Code

To run the encryption process, simply execute the `main.py` script from the root of the project directory:

```bash
python3 main.py
```

### Configuration

You can customize the encryption by modifying the `main.py` script:

- **`plaintext`**: Change the value of this variable to the message you want to encrypt.
- **`seed`**: Change the integer value of the seed to produce a different, but still reproducible, encryption.
- **`output_file`** and **`log_file`**: Modify the file paths to save the output to a different location.

The script will print a confirmation message to the console upon completion, indicating where the files have been saved.
