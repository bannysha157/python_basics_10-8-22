It's syntax is:  str.index(sub[, start[, end]] )

index() Parameters: The index() method takes three parameters:

sub -  substring to be searched in the string str.
start and end(optional) -   substring is searched within str[start:end]

If substring exists inside the string, it returns the lowest index in the string where substring is found.
If substring doesn't exist inside the string, it raises a ValueError exception.
The index() method is similar to the find() method for strings.

The only difference is that find() method returns -1 if the substring is not found, whereas index() throws an exception.

9)str.index():  
  The index() method returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.

Example:
 PROGRAM:
text = 'i will never give up'

# find the index of is
result = text.index('will')
print(result)

# Output: 2

Example 1:  index() With Substring argument Only():
    
program:
  
sentence = 'i will never give up'
result = sentence.index('up')
print("Substring 'is fun':", result)

result = sentence.index('horrer')
print("Substring 'Java':", result)

o/p=
Substring 'is fun': 18
Traceback (most recent call last):
File "<string>", line 5, in <module>
ValueError: substring not found
  
  
  
  
  
  Example 2: index() With start and end Arguments:
      
 PROGRAM:
sentence = 'Python programming is fun.'
# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))
# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))
# Substring is searched in 'programming'
print(sentence.index('fun', 7, 18))

Output:

15
17
Traceback (most recent call last):
  File "<string>", line 10, in 
    print(quote.index('fun', 7, 18))
ValueError: substring not found
  
  
  
  
  
