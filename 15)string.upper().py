15)str.isuuper():The string isupper() method returns whether or not all characters in a string are uppercased or not.

The syntax of isupper() method is:  string.isupper()
  
String isupper() Parameters: The isupper() method doesn't take any parameters.

Return value from String isupper(): The isupper() method returns:

True if all characters in a string are uppercase characters
False if any characters in a string are lowercase characters

Program:
  eample 1: Return value of isupper():

# example string
string = "THIS IS GOOD!"
print(string.isupper());
# numbers in place of alphabets
string = "THIS IS ALSO G00D!"
print(st
# lowercase string
string = "THIS IS not GOOD!"
print(string.isupper());

Output:
 
True
True
False

      
      
      
Example 2: How to use isupper() in a program:
      
      
PROGRAM:
string = 'THIS IS GOOD'
if string.isupper() == True:
  print('Does not contain lowercase letter.')
else:
  print('Contains lowercase letter.')
  
string = 'THIS IS gOOD'
if string.isupper() == True:
  print('Does not contain lowercase letter.')
else:
  print('Contains lowercase letter.')

Output:

Does not contain lowercase letter.
Contains lowercase letter.
      
      
      
