# Write your unit tests here
from recursion_challenge import factorial, palindrome, bottles, roman_num

print(factorial(5) == 120)
print(factorial(8) == 40320)
print(factorial(45) == 119622220865480194561963161495657715064383733760000000000)

print(palindrome('racecar') == True)
print(palindrome('Noon') == True)
print(palindrome('ciVic') == True)
print(palindrome('nice') == False)
print(palindrome(434) == True)
print(palindrome(123) == False)
print(palindrome('bomb') == False)


print(roman_num(1) == 'I')
print(roman_num(3) == 'III')
print(roman_num(4) == 'IV')