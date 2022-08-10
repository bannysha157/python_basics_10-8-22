14)str.isslower(): The islower() method returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.

The syntax of islower() is: string.islower()
  
islower() parameters: The islower() method doesn't take any parameters.

Return Value from islower(): The islower() method returns:

True if all alphabets that exist in the string are lowercase alphabets.
False if the string contains at least one uppercase alphabet.


Example 1: Return Value from islower():
    
s = 'this is good'
print(s.islower())
s = 'th!s is a1so g00d'
print(s.islower())
s = 'this is Not good'
print(s.islower())

Output:
  
True
True
False


Example 2: How to use islower() in a program:
    
    
s = 'this is good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')
  
s = 'this is Good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')

Output:
Does not contain uppercase letter.
Contains uppercase letter.






program:
  
email = 'hello@example.com'
is_lowercase = email.islower()
print(is_lowercase)
 Output:
True
