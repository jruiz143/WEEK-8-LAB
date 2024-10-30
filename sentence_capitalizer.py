#8-8 PROGRAMMING CAPITALIZER
#WRITE A PROGRAM WITH A FUNCTION THAT ACCEPTS A STRING AS AN ARGUMENT AND RETURNS
#A COPY OF THE STRING WITH THE FIRST CHARACTER OF EACH SENTENCE CAPITALIZED
#THE PROGRAM SHOULD LET THE USER ENTER A STRING AND THEN PASS IT TO THE FUNCTION
#THE MODIFIED STRING SHOULD BE DISPLAYED

def capitalize_words(sentence):
    words = sentence.split()  # SPLIT SENTENCE INTO WORDS
    capitalized_words = []  # INTIALIZE CAPTIALIZED WORD LIST TO STORE STRINGS

    for word in words:
        if len(word) > 0:
            capitalized_word = word[0].upper() + word[1:]  # CAPITALIZE LETTER OF FIRST WORD.INCLUDE THE REST OF THE WORD 
            capitalized_words.append(capitalized_word)
        else:
            capitalized_words.append(word)  # HANDLE EXCEPTIONS
    #RETURN A COPY OF THE STRING 
    return ' '.join(capitalized_words)  # JOIN WORDS BACK INTO SENTENCE

# ASK FOR USER INPUT
sentence = input("Enter a sentence: ")

# DISPLAY RESULT
capitalized_sentence = capitalize_words(sentence)
print("Capitalized Sentence:", capitalized_sentence)
