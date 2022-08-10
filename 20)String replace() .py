20)str.replace():
  
It's syntax is: str.replace(old, new [, count]) 

replace() Parameters: The replace() method can take maximum of 3 parameters:

old - old substring you want to replace
new - new substring which will replace the old substring
count (optional) - the number of times you want to replace the old substring with the new substring
Note: If count is not specified, the replace() method replaces all occurrences of the old substring with the new substring.
  
  replace() Return Value:  The replace() method returns a copy of the string where the old substring is replaced with the new substring. The original string is unchanged.

If the old substring is not found, it returns the copy of the original string.

he replace() method replaces each matching occurrence of the old character/text in the string with the new character/text.

Example:
  
text = 'bal ball'
# replace b with c
replaced_text = text.replace('b', 'c')
print(replaced_text)

# Output: cat call

Example 1: Using replace():
    
    
song = 'cold, cold heart'
# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'
# replacing only two occurences of 'let'
print(song.replace('let', "don't let", 2))
 
Output:
hurt, hurt heart
Let it be, don't let it be, don't let it be, let it be

program:
  
s = 'Java is Nice'
# simple string replace example
str_new = s.replace('Java', 'Python')
print(str_new)


# replace character in string
s = 'dododo'
str_new = s.replace('d', 'c')
print(str_new)

Output:
Python is Nice
cococo

program:

Python string replace with count
s = 'dododo'
str_new = s.replace('d', 'c', 2)
print(str_new)

Output: cocodo




  
