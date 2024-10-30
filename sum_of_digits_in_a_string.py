#8-2 SUM OF DIGITS IN A STRING
#WRITE A PROGRAM THAT ASKS THE USER TO ENTER A SERIES OF
#SINGLE-DIGIT NUMBERS W/ NOTHING SEPARATING THEM.
#PROGRAM SHOULD DISPLAY THE SUM OF ALL SINGLE DIGIT NUMBERS IN THE STRING.
#FOR EXAMPLE, IF USER ENTERS 2514, THE METHOD SHOULD RETURN 12, WHICH IS SUM OF 2,5,1, AND 4

def sum_of_digits():
    # GET USER INPUT
    digits = input("Please Enter a series of Numbers: ")
    
    # SPLIT USER INPUT INTO A LIST OF NUMBER STRING
    digit_list = digits.split()

    total = 0
    # LOOP THROUGH EACH NUMBER IN THE STRING LIST
    for digit in digit_list:
        total += int(digit)  # CONVERT TO INTEGER AND ADD
    
    # DISPLAY TOTAL
    print("THE SUM OF DIGITS ENTERED:", total)

#RUN FUNCTION
sum_of_digits()


      
