import re
import math
def main():
    password = input("Please enter your password: ")
    combo = combinations(password)
    numbits = bits(combo)
    print(f"{password} has {combo} number of combinations and is {numbits} bits strong!")

def bits(pos):
    bits = math.log2(pos)
    return round(bits)

def combinations(pswd):
    combos = 0
    #Returns true if a lower case letter is in the pswd
    if bool(re.search(r'[a-z]', pswd)) == True:
        combos += 26
    #Returns true if an upper case letter is in the pswd
    if bool(re.search(r'[A-Z]', pswd)) == True:
        combos += 26
    #Returns true if a number is in the pswd
    if bool(re.search(r'[0-9]', pswd)) == True:
        combos += 10
    #Returns true if a special character is in the pswd
    if any(not c.isalnum() for c in pswd):
        combos += 32
    possibilities = combos ** len(pswd)
    return possibilities
    

if __name__ == "__main__":
    main()