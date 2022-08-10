10)isalnum():

The syntax of the isalnum() method is:  string.isalnum()
  
Here, the isalnum() method checks if all the characters of string are alphanumeric or not.

isalnum() Parameters:  The isalnum() method doesn't take any parameters.

isalnum() Return Value:   The isalnum() method returns:

True - if all characters in the string are alphanumeric
False - if at least one character is not alphanumeric


=>isalnum():   The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.

Example:
 program:
  
# string contains either alphabet or number 
name1 = "Python3"
print(name1.isalnum()) #True
# string contains whitespace
name2 = "Python 3"
print(name2.isalnum()) #False

o/p =true
flase



Example 1: Python isalnum():
    
    program:
      # contains either numeric or alphabet
string1 = "M234bOannysha"
print(string1.isalnum()) # True 
# contains whitespace
string2 = "M3onica give up"
print(string2.isalnum()) # False
# contains non-alphanumeric character 
string3 = "#bannysha!"
print(string3.isalnum()) # False 

o/p=true
false
false

In the above example, we have used the isalnum() method with different strings to check if every character in the string is alphanumeric.

Here, string1 contains either alphabet or numerical values so the method returns True.

The method returns False for string2 and string3 because they contain non-alphanumeric characters i.e. whitespace, @, !.


Example 2: isalnum() in if..else Statement():
    
program:
  
text = "Python#Programming123"
# checks if all the characters are alphanumeric 
if text.isalnum() == True:
   print("All characters of string are alphanumeric.")
else:
    print("All characters are not alphanumeric.")

o/p= All characters are not alphanumeric








