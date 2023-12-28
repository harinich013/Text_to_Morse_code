def text_converter():
    morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                       'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                       '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}

    def encrypt(text):
        morse_code = ''
        for char in text:
            if char in morse_code_dict:
                morse_code += morse_code_dict[char] + ' '

        return morse_code.rstrip()

    def decrypt(text):
        decrypt_msg = ""
        for word in text:
            characters = word.split(" ")
            for char in characters:
                if char in morse_code_dict.values():
                    decrypt_msg += [k for k, v in morse_code_dict.items() if v == char][0]
            decrypt_msg += " "
        return decrypt_msg.rstrip()

    input_message = input("Enter E for encrypt or D for decrypt: ").upper()
    if input_message == "E":
        input_text = input("Enter the text to convert to Morse code: ")
        result = encrypt(input_text.upper())
        print(f"Morse Code: {result}")
    elif input_message == "D":
        input_text = input("Enter the Morse code to decrypt: ")
        result = decrypt(input_text.split("   "))  # Adjusted to triple space
        print(f"Decrypted Text: {result}")
    else:
        print("Enter valid letter (E or D).")
        text_converter()


# Call the function to start the program
text_converter()
