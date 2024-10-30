#8-3 PROGRAMMING EXERCISE:
#WRITE A PROGRAM THAT READS A STRING FROM THE USER CONTAINING
#A DATE IN THE FORM OF MM/DD/YY. IT SHOULD PRINT THE DATE IN THE 
#FORMAT MARCH 12, 2018


def print_date():
    # GET A STRING FROM USER
    date_input = input("PLEASE ENTER DATE (MM/DD/YY): ")
    
    # SPLIT USER INPUT INTO THREE PARTS
    split_date = date_input.split("/")
    month_number = int(split_date[0]) #FIRST PART CONVERTS STRING TO INTEGER AND ASSIGN TO MONTH VARIABLE
    day = split_date[1] #SECOND PART OF STRING ASSIGNED TO DAY VARIABLE
    year = split_date[2] #THIRD PART OF STRING ASSIGNED TO YEAR VARIABLE

    # CREATE MONTH LIST
    month_names = [
        "January", "February", "March", "April", "May",
        "June", "July", "August", "September", "October",
        "November", "December"
    ]

    # CHECK MONTH NUMBERS/ IF MONTH NUMBER IS VALID IT EXECUTES NEXT LINES
    if 1 <= month_number <= 12:
        #FIND NAME OF THE MONTH BASED ON NUMBER.
        month_name = month_names[month_number - 1]#SUBTRACT 1
        #FROM MONTH NUMBER TO MATCH CORRECT INDEX
        print(f"{month_name} {day}, 20{year}")#DISPLAY DATE OUTPUT
    else:
        print("An error has occurred: Invalid month number.")

# RUN FUNCTION
print_date()
