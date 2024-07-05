#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import argparse


def vigenereTable():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    vigenerList = []
    while i < 26: #26 is length of English alphabet. It could have been used like len(alphabet)
        vigenerLine = alphabet[i:] + alphabet[0:i] # shift left by 1
        vigenerList.append(vigenerLine)
        i += 1
    return pd.DataFrame(vigenerList) # generate datafram from output

def genKeystream(key, cipher): #GENERATE THE KEYSTREAM LIKE KEYKEYKEYKEYKE
        key = list(key)
        keystream = []

        j = 0
        for i in range(len(cipher)):
            if j >= len(key):
                j = 0
            keystream.append(key[j])
            j += 1
        return "".join(keystream).upper()

def prepareKeyAndText(keystream, text):
    return [[keystream[i], text[i]] for i in range(len(text))]

def decryptVigenere(key,cipher):
    key = key.upper()
    cipher = cipher.upper()
    keystream = genKeystream(key, cipher)
    ciphered = []
    for i in prepareKeyAndText(keystream, cipher):
        ciphered.append(chr(vigenereTableDataFrame[0][ord(i[0])-65].index(i[1])+65))
    return "".join(ciphered)


def encryptVigenere(key, plaintext):
    key= key.upper()
    plaintext = plaintext.upper()
    keystream = genKeystream(key,plaintext)
    ciphered = []
    for i in prepareKeyAndText(keystream, plaintext):
        ciphered.append(vigenereTableDataFrame[0][ord(i[0])-65][ord(i[1])-65])
    return "".join(ciphered)


def main():
    parser = argparse.ArgumentParser(description="Vigenere Cipher Encryption/Decryption Tool")
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the cipher text')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt a plain text')
    parser.add_argument('key', type=str, help='The key to use for decryption')
    parser.add_argument('data', type=str, help='The data to encrypt/decrypt')
    
    args = parser.parse_args()
    
    global vigenereTableDataFrame 
    vigenereTableDataFrame = vigenereTable()

    if args.decrypt:
        decrypted_text = decryptVigenere(args.key, args.data)
        print("Decrypted Text:", decrypted_text)
    if args.encrypt:
        encrypted_text = encryptVigenere(args.key, args.data)
        print("Encrypted Text:", encrypted_text)


if __name__ == "__main__":
    main()
