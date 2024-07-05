# Vigenere Cipher Encryption/Decryption Tool
This project is a Python program that performs Vigenere cipher encryption and decryption operations. 
Users can input a key and text from the command line to either encrypt or decrypt messages.

## Usage
The program operates using command-line arguments with `argparse`. Below are examples of usage.

### Encryption
To encrypt a plaintext, use the `-e` or `--encrypt` option followed by the key and text:

```bash
python vigenere_cipher.py -e KEY TEXT

Example:
python vigenere_cipher.py -e SECRET HELLO
```

### Decryption
To decrypt a ciphertext, use the -d or --decrypt option followed by the key and ciphertext:

```bash
python vigenere_cipher.py -d KEY CIPHERTEXT

Example:
python vigenere_cipher.py -d SECRET RIJVS
```

### Functions
vigenereTable(): Generates the Vigenere table.

genKeystream(key, text): Generates a keystream from the key based on the length of the text.

decryptVigenere(key, cipher): Decrypts the cipher text with the given key.

encryptVigenere(key, plaintext): Encrypts the plaintext with the given key.

prepareKeyAndText(keystream, text): Prepares pairs of keystream and text characters.

main(): Handles command-line arguments and calls appropriate encryption or decryption functions.


### Requirements
This project requires the following Python library: 
1) pandas

To install pandas:

```bash
pip install pandas
