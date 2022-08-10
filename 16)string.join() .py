16)str.join():
  
 =>The syntax of the join() method is:  string.join(iterable)
    
joint() Parameters: The join() method takes an iterable (objects capable of returning its members one at a time) as its parameter.

Some of the example of iterables are:

Native data types - List, Tuple, String, Dictionary and Set.

File objects and objects you define with an __iter__() or __getitem()__ method.

Note: The join() method provides a flexible way to create strings from iterable objects. 
  It joins each element of an iterable (such as list, string, and tuple) by a string separator (the string on which the join() method is called) and returns the concatenated string.
  
  return Value from join() method:
The join() method returns a string created by joining the elements of an iterable by string separator.

If the iterable contains any non-string values, it raises a TypeError exception.

Example:
text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
# join elements of text with space
print(' '.join(text))

# Output: Python is a fun programming language

PROGRAM:
# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))
# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))
s1 = 'abc'
s2 = '123'
# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))
# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))


Output:
1, 2, 3, 4
1, 2, 3, 4
s1.join(s2): 1abc2abc3
s2.join(s1): a123b123c
  
  
  
  
  
  
  
Example 2: The join() method with sets:
    
# .join() with sets
test = {'2', '1', '3'}
s = ', '
print(s.join(test))
test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

Output:
2, 3, 1
Python->->Ruby->->Java

Note: A set is an unordered collection of items, so you may get different output (order is random).
  
  
 => join() vs Concatenation operator + 

Concatenation operator + is perfectly fine solution to join two strings. But if you need to join more strings, it is convenient to use join() method.

PROGRAM:
  
# concatenation operator
x = 'aaa' + 'bbb'
print(x)
# Prints aaabbb

# join() method
x = ''.join(['aaa','bbb'])
print(x)
# Prints aaabbb
      
 
  
  




