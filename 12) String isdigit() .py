12)str.isdigit():
  
The syntax of isdigit() is: string.isdigit()
  
isdigit() Parameters:  The isdigit() doesn't take any parameters.

Return Value from isdigit():  The isdigit() returns:

True if all characters in the string are digits.
False if at least one character is not a digit.



str.isdigit():  the isdigit() method returns True if all characters in a string are digits. If not, it returns False.

Example:
str1 = '342'
print(str1.isdigit())
str2 = 'python'
print(str2.isdigit())

# Output: True
#    False





Example 1: Working of isdigit():
    
    
s = "28212"
print(s.isdigit())
# contains alphabets and spaces
s = "bAN4 NiE eill l22up"
print(s.isdigit())

O/P=
True
False





Example 2: String Containing digits and Numeric Characters:
    
PROGRAM:
s = '23455'
print(s.isdigit())
#s = '²3455'
# subscript is a digit
s = '\u00B23455'
print(s.isdigit())
# s = '½'
# fraction is not a digit
s = '\u00BD'
print(s.isdigit())

Output:

True
True
False
