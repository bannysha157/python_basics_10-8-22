8)str.find():
  
The syntax of the find() method is:  str.find(sub[, start[, end]] )
  
find() Parameters:  The find() method takes maximum of three parameters:

sub -  It is the substring to be searched in the str string.
start and end (optional) -  The range str[start:end] within which substring is searched.
find() Return Value:  The find() method returns an integer value:

If the substring exists inside the string, it returns the index of the first occurence of the substring.

If a substring doesn't exist inside the string, it returns -1.





find() :   The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
  
 program:
message = 'never give up'

# check the index of 'up'
print(message.find('up'))

# Output: 11



Example 1: find() With No start and end Argument:
    
    program:
      s = 'fell like Freedom.fell Like freedom'

# first occurance of 'like '(case sensitive)
result = s.find('like')
print("Substring 'like':", result)

# find returns -1 if substring not found
result = s.find('give  up')
print("Substring 'give up ':", result)

# How to use find()
if (s.find('fell') != -1):
    print("Contains substring 'fell,'")
else:
    print("Doesn't contain substring")
    
 o/p=   
    
 Substring 'like': 5
Substring 'give up ': -1
Contains substring 'fell,'



Example 2: find() With start and end Arguments:
    
    
 PROGRAM:
    
 quote = 'Do small things with great love'
# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))
# Substring is searched in ' small things with great love' 
print(quote.find('small things', 2))
# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))
# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))

Output:

-1
3
-1
9





