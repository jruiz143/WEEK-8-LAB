#8-10 PROGRAMMING EXERCISE
#WRITE A PROGRAM THAT ALLOWS A USER TO ENTER A STRING AND DISPLAYS
#THE CHARACTER THAT APPEARS MOST FREQUENTLY IN THE STRING

def main():
    user_string = input("PLEASE ENTER A STRING OF CHARACTERS: ")
    user_string = user_string.upper()  # CONVERT STRING TO UPPERCASE LETTERS
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # CREATE ALPHABET STRING
    char_count = [0] * 26  # LIST TO STORE COUNTS FOR EACH LETTER

    # COUNT FREQUENCY OF EACH LETTER
    for ch in user_string:
        if ch.isalpha(): 
            index = alphabet.index(ch)
            char_count[index] += 1

    # FIND CHARACTER THAT APPEARS MOST FREQUENTLY IN STRING
    max_count = -1
    most_frequent_char = ''
    for i in range(26):
        if char_count[i] > max_count:
            max_count = char_count[i]
            most_frequent_char = alphabet[i]

    print("THE MOST FREQUENT CHARACTER IS:", most_frequent_char)

if __name__ == "__main__":
    main()

