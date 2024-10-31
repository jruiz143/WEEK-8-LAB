#8-9 PROGRAMMING EXERCISE
#WRITE A PROGRAM WITH A FUNCTION THAT ACCEPTS A STRING AS AN ARGUMENT AND RETURNS THE NUMBER OF VOWELS
#THE STRING CONTAINS. THE APPLICATION SHOULD HAVE ANOTHER FUNCTION THAT ACCEPTS A STRING AS AN ARGUMENT AND RETURNS
#THE NUMBER OF CONSONANTS THAT THE STRING CONTAINS. DISPLAY OUTCOME

def main():
  user_string = input("ENTER A STRING OF CHARACTERS: ")
  print ("The string has", num_vowels(user_string), "vowels and", \
         num_consonants(user_string), "consonants.")
  
def num_vowels(s):
  vowels = ['a', 'e', 'i', 'o', 'u']#CREATE VOWEL LIST
  v_count = 0
  for ch in s:
    if ch.lower() in vowels:
      v_count +=1
  return v_count
  
#COUNT CONSONANTS 
def num_consonants(s):
  vowels = ['a', 'e', 'i', 'o', 'u']
  for ch in s:
    if ch.isaplha() and ch.lower() not in vowels:
      c_count +=1
  return c_count
#CALL MAIN FUNCTION
main()

