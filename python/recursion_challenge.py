def factorial(x):
    if x == 1:
        # print(f"{x}: is bottom of the recursion")
        return x
    else:
        print(f"{x}")
        # print(x * factorial(x-1))
        return x * factorial(x-1)

 
def palindrome(string): 
    
    new_string = str(string).lower()
    if len(new_string) <= 1:
        return True
    elif new_string[0] == new_string[-1]:
        return palindrome(new_string[1:-1])
    else:
        return False


def bottles(num):
    if num == 0:
        print(f"No bottles of beer on the wall, no more bottles of beer. ")
        print(f"Take one down and pass it around, 99 bottles of beer on the wall.")
        return
    elif num == 1:
        print(f"{num} bottles of beer on the wall, {num} bottles of beer. ")
        print(f"Take one down and pass it around, {num - 1} bottles of beer on the wall.")
        return bottles(num - 1)

    else:
        print(f"{num} bottles of beer on the wall, {num} bottles of beer. ")
        print(f"Take one down and pass it around, {num - 1} bottles of beer on the wall.")
        return bottles(num - 1)



def to_roman(num, roman_integer = ""):

    romanObj = {
        "M":  1000,
        "CM": 900,
        "D":  500,
        "CD": 400,
        "C":  100,
        "XC": 90,
        "L":  50,
        "XL": 40,
        "X":  10,
        "IX": 9,
        "V":  5,
        "IV": 4,
        "I":  1,
    }
    
    if num == 0:
        return roman_integer

    else: 
     for roman_number in romanObj:
        if (num / romanObj[roman_number]) >= 1:
            roman_integer += roman_number
            break
    return to_roman(num - romanObj[roman_number],roman_integer)

           
# print(to_roman(80))