def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

key = 13
#Input encrypted code into the "" below.
encrypted_code = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)
#The output quote is a Marilyn Monroe quote:
#IM SELFISH IMPATIENT AND A LITTLE INSECURE I MAKE MISTAKES I AM OUT OF CONTROL
# ANDAT TIMES HARD TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORST THEN YOU SURE AS HELLDONT DESERVE ME AT MY BEST MARILYN MONROE
#Cleaned up:
#I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle.
# But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.
# - Marlyn Monroe
