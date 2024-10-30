#8-7 PROGRAMMING EXERCISE
#WRITE A PROGRAM THAT READS FILE TEXT.TXT CONTENTS AND DETERMINES THE FOLLOWING:
#1) THE NUMBER OF UPPERCASE LETTERS IN THE FILE, 2) THE NUMBER OF LOWERCASE LETTERS IN THE FILE,
#3)THE NUMBER OF DIGITS IN THE FILE, 4)THE NUMBER OF WHITESPACE CHARACTERS IN THE FILE

# INTITALIZE VARIABLES
uppercase = 0
lowercase = 0
digits = 0
whitespace = 0

# OPEN FILE AND READ CONTENTS
with open("text.txt", "r") as file:
    for line in file:
        for char in line:
            if char.isupper(): #SEARCH FOR CAPTIAL LETTERS
                uppercase += 1 #ADD UPPERCASE TO COUNT
            elif char.islower(): #SEARCH FOR LOWERCASE LETTERS
                lowercase += 1 #ADD LOWERCASE TO COUNT
            elif char.isdigit():#SEARCH FOR DIGITS
                digits += 1 #ADD DIGITS TO COUNT
            elif char.isspace():#SEARCH FOR WHITESPACES IN FILE
                whitespace += 1#ADD WHITESPACE TO COUNT

# DISPLAY RESULTS
print(f"THE NUMBER OF UPPERCASE LETTERS FOUND: {uppercase}")
print(f"THE NUMBER OF LOWERCASE LETTERS FOUND: {lowercase}")
print(f"THE NUMBER OF DIGITS FOUND: {digits}")
print(f"THE NUMBER OF WHITESPACE CHARACTERS FOUND: {whitespace}")

          
