17)str.partition():  this method splits the string at the first occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator.

The syntax of partition() is: string.partition(separator)
  
partition() Parameters():The partition() method takes a string parameter separator that separates the string at the first occurrence of it.

Return Value from partition(): The partition method returns a 3-tuple containing:

the part before the separator, separator parameter, and the part after the separator if the separator parameter is found in the string
the string itself and two empty strings if the separator parameter is not found

program:
  
string = "Python is fun"
# 'is' separator is found
print(string.partition('is '))
# 'not' separator is not found
print(string.partition('not '))
string = "Python is fun, isn't it"
# splits at first occurence of 'is'
print(string.partition('is'))

Output: 

('Python ', 'is ', 'fun')
('Python is fun', '', '')
('Python ', 'is', " fun, isn't it")


NOTE:  The partition() method search is case-sensitive.
It treats Fell' and 'fell' as two separate words, as shown below.

Example: partition() Copy

program:

mystr = 'Fell like is the best fell website.'
print(mystr.partition('fell'))
print(mystr.partition('Fell'))

Output:
('TutorialsTeacher is the best ', 'tutorials', ' website')
('', 'Tutorials', 'Teacher is the best tutorials website')




=>If the separator is an empty string, then the partition() method will throw ValueError.

Example: partition() Copy:

program:

mystr = 'Hello World'
print(mystr.partition('s'))

mystr = 'Hello World'
print(mystr.partition(''))

Output:
('Hello World', '', '')
ValueError: empty separator



=>The separator passed can be numbers as well as symbols.

Example: partition() Copy:

program:

mystr = '#1 Harbor Side'
print(mystr.partition('1'))
Output:
('#', '1', ' Harbor Side')


=>The partition() method will only split the string at the first occurrence of the separator.

Example: partition() Copy
mystr="TutorialsTeacher"
print(mystr.partition("T")

Output:
 ('', 'T', 'utorialsTeacher')
 

=>The partition() method performs case-sensitive search.

Example: partition() Copy
mystr="TutorialsTeacher"
print(mystr.partition("t")

Output:
 ('Tu', 't', 'orialsTeacher')
 



