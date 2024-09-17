#String
s = "56eAww1904kst7235270aYm1145ss785fSq310D"

#Seperating even digits and alphabets
even_digits = ''.join([character for character in s if character.isdigit()and int(character) % 2 == 0])
alphabet_string = ''.join([character for character in s if character.isalpha()])

#Modifying even digits to ASCII
ascii_even_digits = [ord(digit) for digit in even_digits]

#Changing Uppercase characters to ASCII
ascii_uppercase_chars = [ord(char) for char in alphabet_string if char.isupper()]

#Result
print( even_digits)
print( alphabet_string)
print(ascii_even_digits)
print(ascii_uppercase_chars)

