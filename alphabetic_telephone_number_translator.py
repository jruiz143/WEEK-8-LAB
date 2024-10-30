#8-5 PROGRAMMING EXERCISE
# ON A STANDARD TELEPHONE, THE ALPHABETIC LETTERS ARE MAPPED TO NUMBERS 
#IN THE FOLLOWING FASHION: A,B,C = 2; D,E AND F = 3; G,H,I =4; 
#J,K,L = 5, M,N, O
#WRITE A PROGRAM THAT ASKS THE USER TO ENTER A 10-CHARACTER TELEPHONE IN THE FORMAT
#XXX-XXX-XXX. THE APLICATION SHOULD DISPLAY THE TELEPHONE NUMBER WITH ANY
#ALPHABETIC CHARACTERS THAT APPEARED IN THE ORIGINAL TRANSLATED TO THEIR
#NUMERIC EQUIVALENT. FOR EXAMPLE, IF TH EUSER ENTERS 555-GET-FOOD, THE
#APPLICATION SHOULD DISPLAY 555-438-3663

def get_numeric_value(char):
    # CREATE LIST FOR EACH LETTER
    letters = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    
    #LOOP THROUGH LETTERSS LIST ASSOCIATED WITH CORRESPONDING NUMBER
    for i in range(2, 10):
        if char in letters[i]:
            return str(i)
    return char  # RETURN TO ORIGINAL CHAR IF NOT FOUND

def translate_to_number(phone):
    phone = phone.upper()
    translated_number = ""

    # Process each character in the phone number
    for char in phone:
        translated_number += get_numeric_value(char)
    
    return translated_number

# GET USER INPUT 
phone_number = input("ENTER A 10-CHARACTER TELEPHONE NUMBER (XXX-XXX-XXXX): ")
print("THE TRANSLATED NUMBER INPUTTED:", translate_to_number(phone_number))
