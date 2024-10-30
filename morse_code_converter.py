#8-4 PROGRAMMING EXERCISE
#WRITE A PROGRAM THAT ASKS THE USER TO ENTER 
#A STRING, THEN CONVERTS THAT STRING TO MORSE CODE

def text_to_morse():
    # CREATE MORSE CODE LIST
    morse_code_list = [
        "/", "--..--", ".-.-.-", "..--..", # SPACE, COMMA, PERIOD, QUESTION MARK
        "-----", ".----", "..---", "...--", "....-", ".....", # 0-5
        "-....", "--...", "---..", "----.", # 6-9
        ".-", "-...", "-.-.", "-..", ".", "..-.", # A-F
        "--.", "....", "..", ".---", "-.-", # G-K
        ".-..", "--", "-.", "---", ".--.", # L-P
        "--.-", ".-.", "...", "-", "..-", "...-", # Q-V
        ".--", "-..-", "-.--", "--.." # W-Z
    ]

    special_chars = [" ", ",", ".", "?"]
    numbers = "0123456789"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # GET USER INPUT
    user_input = input("PLEASE ENTER TEXT TO CONVERT TO MORSE CODE: ")
    morse_output = ""

    # CONVERT CHARACTER TO MORSE CODE
    for char in user_input:
        if char in special_chars:
            # RETRIEVE INDEX FOR SPACE, COMMA, PERIOD, QUESTION MARK
            morse_output += morse_code_list[special_chars.index(char)] + " "
        elif char in numbers:
            # GET INDEX FOR 0-9 
            morse_output += morse_code_list[4 + numbers.index(char)] + " "#INDEX STARTS AT FOURTH ELEMENT
        elif char in letters:
            # GET INDEX FOR A-Z
            morse_output += morse_code_list[14 + letters.index(char)] + " "#INDEX STARTS AT 14 ELEMENT
        else:
            print(f"ERROR:'{char}' CANNOT BE FOUND.")

    # DISPLAY MORSE CODE
    print("Morse Code:", morse_output.strip())

# Run the function
text_to_morse()




