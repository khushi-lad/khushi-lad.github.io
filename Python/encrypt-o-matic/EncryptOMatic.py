"""
******************************
Encrypt-o-Matic
******************************
This file is used to encode and decode text by using a key to shift the text using a caesar cipher
or a vigenere cipher. The functions will check the input, raise errors, and return the count of
all processed characters.
"""

import os

# Uses caesar cipher to encrypt text in input file by shifting the text by the key, writes the encrypted text in output file, returns count of all processed characters
def encrypt_caesar(input_file, output_file, key):
    if os.path.isfile(input_file) is False:
        raise FileNotFoundError(f"The input file '{input_file}' does not exist.") # Raise error if file does not exist
    if type(key) is not int:
        raise TypeError("The given key value is the wrong type!")  # Raise error if key is not int type
    if os.path.isfile(output_file) is True:
        raise FileExistsError(f"The output file '{output_file}' already exists.")  # Raise error if output file already exists
    else:
        if os.path.isfile(input_file):
            count = 0
            input_text = open(input_file, "r") # Open input file in read mode
            output_text = open(output_file, "w") # Open output file in write mode
            for line in input_text:
                count += len(line) # Count all characters in the line and add it to count
                line = line.strip("\n") # Remove newline from each line in input text
                for i in line:
                    if i.isalpha():
                        num = ord(i.upper()) + key # Get ASCII value for each alpha character and shift it by adding the key to it
                        while num > ord("Z"):
                            num -= 26 # If the shifted ASCII value goes past Z, wrap it around to go back to A
                        while num < ord("A"):
                            num += 26 # If the shifted ASCII value goes past A, wrap it around to go back to Z
                        output_text.write(chr(num)) # Get alpha character using ASCII value
                    else:
                        output_text.write(i) # Write non-alpha characters from input file in output file
                output_text.write("\n") # Add newline after each line is written in output file
            input_text.close()
            output_text.close()
            return count # Returns count of all processed characters

# Uses caesar cipher to decrypt text in input file by shifting the text by the key, writes the decrypted text in output file, returns count of all processed characters
def decrypt_caesar(input_file, output_file, key):
    if os.path.isfile(input_file) is False:
        raise FileNotFoundError(f"The input file '{input_file}' does not exist.") # Raise error if file does not exist
    if type(key) is not int:
        raise TypeError("The given key value is the wrong type!")  # Raise error if key is not int type
    if os.path.isfile(output_file) is True:
        raise FileExistsError(f"The output file '{output_file}' already exists.")  # Raise error if output file already exists
    else:
        if os.path.isfile(input_file):
            count = 0
            input_text = open(input_file, "r") # Open input file in read mode
            output_text = open(output_file, "w") # Open output file in write mode
            for line in input_text:
                count += len(line) # Count all characters in the line and add it to count
                line = line.strip("\n") # Remove newline from each line in input text
                for i in line:
                    if i.isalpha():
                        num = ord(i.upper()) - key # Get ASCII value for each alpha character and shift it by subtracting the key from it
                        while num > ord("Z"):
                            num -= 26 # If the shifted ASCII value goes past Z, wrap it around to go back to A
                        while num < ord("A"):
                            num += 26 # If the shifted ASCII value goes past A, wrap it around to go back to Z
                        output_text.write(chr(num)) # Get alpha character using ASCII value
                    else:
                        output_text.write(i) # Write non-alpha characters from input file in output file
                output_text.write("\n") # Add newline after each line is written in output file
            input_text.close()
            output_text.close()
            return count # Returns count of all processed characters

# Uses vigenere cipher to encrypt text in input file by shifting the text by the key, writes the encrypted text in output file, returns count of all processed characters
def encrypt_vigenere(input_file, output_file, key):
    if os.path.isfile(input_file) is False:
        raise FileNotFoundError(f"The input file '{input_file}' does not exist.") # Raise error if file does not exist
    if type(key) is not str:
        raise TypeError("The given key value is the wrong type!")  # Raise error if key is not int type
    if os.path.isfile(output_file) is True:
        raise FileExistsError(f"The output file '{output_file}' already exists.")  # Raise error if output file already exists
    else:
        if os.path.isfile(input_file):
            count = 0
            input_text = open(input_file, "r") # Open input file in read mode
            output_text = open(output_file, "w") # Open output file in write mode
            key_index = 0
            for line in input_text:
                count += len(line) # Count all characters in the line and add it to count
                line = line.strip("\n") # Remove newline from each line in input text
                for i in line:
                    if i.isalpha():
                        if key_index >= len(key): # If key index goes past the key length, the key index is reset to zero
                            key_index = 0
                        shift = ord(key[key_index].upper()) - ord("A") # Get ASCII value for letter in key at key index and subtract by ASCII value for A to get the shift value
                        num = ord(i.upper()) + shift # Add the shift value to the ASCII value for each alpha character to get the shifted character
                        while num > ord("Z"):
                            num -= 26 # If the shifted ASCII value goes past Z, wrap it around to go back to A
                        output_text.write(chr(num)) # Get alpha character using ASCII value
                        key_index += 1 # Increment key index each time
                    else:
                        output_text.write(i) # Write non-alpha characters from input file in output file
                output_text.write("\n") # Add newline after each line is written in output file
            input_text.close()
            output_text.close()
            return count # Returns count of all processed characters

# Uses vigenere cipher to decrypt text in input file by shifting the text by the key, writes the decrypted text in output file, returns count of all processed characters
def decrypt_vigenere(input_file, output_file, key):
    if os.path.isfile(input_file) is False:
        raise FileNotFoundError(f"The input file '{input_file}' does not exist.") # Raise error if file does not exist
    if type(key) is not str:
        raise TypeError("The given key value is the wrong type!")  # Raise error if key is not int type
    if os.path.isfile(output_file) is True:
        raise FileExistsError(f"The output file '{output_file}' already exists.")  # Raise error if output file already exists
    else:
        count = 0
        input_text = open(input_file, "r") # Open input file in read mode
        output_text = open(output_file, "w") # Open output file in write mode
        key_index = 0
        for line in input_text:
            count += len(line) # Count all characters in the line and add it to count
            line = line.strip("\n") # Remove newline from each line in input text
            for i in line:
                if i.isalpha():
                    if key_index >= len(key): # If key index goes past the key length, the key index is reset to zero
                        key_index = 0
                    shift = ord(key[key_index].upper()) - ord("A") # Get ASCII value for letter in key at key index and subtract by ASCII value for A to get the shift value
                    num = ord(i.upper()) - shift # Add the shift value to the ASCII value for each alpha character to get the shifted character
                    while num < ord("A"):
                        num += 26 # If the shifted ASCII value goes past A, wrap it around to go back to Z
                    output_text.write(chr(num)) # Get alpha character using ASCII value
                    key_index += 1 # Increment key index each time
                else:
                    output_text.write(i) # Write non-alpha characters from input file in output file
            output_text.write("\n") # Add newline after each line is written in output file
        input_text.close()
        output_text.close()
        return count # Returns count of all processed characters