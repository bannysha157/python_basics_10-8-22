11)str.isalpha():

The isalpha() method returns True if all characters in the string are alphabets. 
If not, it returns False.

The syntax of isalpha() is:  string.isalpha()

isalpha() Parameters:  isalpha() doesn't take any parameters.

Return Value from isalpha():  The isalpha() returns:

True if all characters in the string are alphabets (can be both lowercase and uppercase).
False if at least one character is not alphabet.

=>program: Working of isalpha():

name = "Bannysha"
print(name.isalpha())
# contains whitespace
name = "never  kill you"
print(name.isalpha())
tains number
name = "Banny123shayou"
print(name.isalpha())

o/p=True
False
False

Example2:  Working of isalpha()

name = "banny$ha"
if name.isalpha() == True:
   print("All characters are alphabets")
else:
    print("All characters are not alphabets.")
    
    
    o/p=All characters are not alphabets
    
    
    





