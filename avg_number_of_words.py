#8-6 PROGRAMMING EXERCISE  
#WRITE A PROGRAM THAT READS THE A FILE NAMED TEXT.TXT CONTENTS AND CALCULATES THE AVG 
#NUMBER OF WORDS PER SENTENCE.

#OPEN AND RENAME AS FILE
with open("text.txt", "r") as file:
    lines = file.readlines() #READ THROUGH ALL LINES IN FILE

sentences = len(lines)#COUNT LINES(SENTENCES) IN FILE
total_words = 0 #INTIALIZE WORD COUNT

#LOOP THROUGH EACH LINE
for line in lines:
    words = line.split() #SPLIT LINE INTO WORDS
    total_words += len(words) #ADD NUMBER OF WORDS IN CURRENT LINE TO TOTAL WORD COUNT

average_words = total_words / sentences #CALC AVERAGE

print(f"THE AVERAGE NUMBER OF WORDS PER SENTENCE: {average_words:.2f}")
