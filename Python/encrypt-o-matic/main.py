"""
******************************
Encrypt-o-Matic
******************************
This file is used to perform a frequency analysis, print a frequency graph, and print the menu
options. The frequency analysis will return a dictionary with the occurrence of each letter in
the text. The frequency graph will print a bar graph using the data from the frequency analysis.
The menu options will be printed and will ask for user input for whether they would like to
encrypt or decrypt, and if they would like to use the caesar or vigenere cipher.
"""

from EncryptOMatic import *

# Creates a dictionary with the letters of the alphabet as the keys and the number of occurrences of each letter as the values
def frequency_analysis(ciphertext):
    result = {} # Create empty dictionary
    for i in ciphertext:
        if i.isalpha():
          if i.upper() in result.keys():
              result[i.upper()] += 1 # If uppercase i is already in the keys, increment its value
          else:
              result[i.upper()] = 1 # If uppercase i is not in the keys, add it with a value of 1
    return result # Return the dictionary with all the keys and their values

# Uses the dictionary and prints an asterisk for each occurrence of each letter in a bar graph
def print_frequency_graph(frequency_dict):
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if i in frequency_dict.keys():
            percent = frequency_dict[i] / sum(frequency_dict.values()) # Calculate the frequency of i as a percentage
        else:
            frequency_dict[i] = 0 # If the letter is not in the dictionary, then set its frequency value to zero
            percent = frequency_dict[i] / sum(frequency_dict.values()) # Calculate the frequency of i as a percentage
        total_occur = round(percent * 100) * "*" # Multiply the rounded frequency percentage by an asterisk
        print(f"{i}: {total_occur}") # For each letter, print its rounded frequency percentage represented by asterisks

# Prints the menu options and asks for valid input, if the input is not valid it prints invalid input
def print_menu():
    valid = False
    selection = None
    while not valid:
        print("Encryption options:"
              "\n1) Caesar Cipher"
              "\n2) Vigenere Cipher"
              "\n3) Frequency Analysis"
              "\n4) Exit")
        selection = input("Input menu option (1 to 4): ") # Allow user to input a selection
        if selection.isdigit():
            selection = int(selection) # If the selection is a digit, turn it into int type
            if 1 <= selection <= 4:
                valid = True # If the selection is between 1 and 4, set valid to true
            else:
                print("Invalid input!") # If selection is not between 1 and 4, tell the user the input is invalid
        else:
            print("Invalid input!") # If selection is not a digit, tell the user the input is invalid
    return selection # Return the selection

# Asks user for selection, returns count of all processed characters or prints a frequency graph, and catches exceptions and prints an error message
def main():
    selection = 0
    while selection != 4: # Keeps looping until the selection is 4
        try:
            selection = print_menu()
            if selection == 1: # Ask user if encrypting or decrypting, input file name, output file name, and key
                crypt_type = input("Are you encrypting or decrypting (e/d)? ").strip().lower()
                input_file_name = input("Enter the input file name: ").strip()
                output_file_name = input("Enter the output file name: ").strip()
                key_int = input("Enter the key (integer): ").strip()
                if crypt_type == "e":
                    count = encrypt_caesar(input_file_name, output_file_name, key_int)
                    print(f"Number of characters processed: {count}") # Returns count of all processed characters
                elif crypt_type == "d":
                    count = decrypt_caesar(input_file_name, output_file_name, key_int)
                    print(f"Number of characters processed: {count}") # Returns count of all processed characters
            elif selection == 2: # Ask user if encrypting or decrypting, input file name, output file name, and key
                crypt_type = input("Are you encrypting or decrypting (e/d)? ").strip().lower()
                input_file_name = input("Enter the input file name: ").strip()
                output_file_name = input("Enter the output file name: ").strip()
                key_str = input("Enter the key (string): ").strip()
                if crypt_type == "e":
                    count = encrypt_vigenere(input_file_name, output_file_name, key_str)
                    print(f"Number of characters processed: {count}") # Returns count of all processed characters
                elif crypt_type == "d":
                    count = decrypt_vigenere(input_file_name, output_file_name, key_str)
                    print(f"Number of characters processed: {count}") # Returns count of call processed characters
            elif selection == 3: # Ask user for input file name, perform a frequency analysis, and print a frequency graph
                cipher_file_name = input("Enter the cipher text file name: ").strip()
                cipher_file = open(cipher_file_name, "r")
                cipher_text = cipher_file.read()
                cipher_file.close()
                dict = frequency_analysis(cipher_text)
                print_frequency_graph(dict)
            elif selection == 4:
                print("Exiting the program.")
                break
        except Exception as e: # Catch exceptions and print an error message
            print("Error:", e)

if __name__ == "__main__":
    main()
