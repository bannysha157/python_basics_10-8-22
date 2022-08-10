4)str.count()

The syntax of count() method is: string.count(substring, start=..., end=...)

count() Parameters: count() method only requires a single parameter for execution. 
However, it also has two optional parameters:

     substring -   string whose count is to be found.
start (Optional) -  starting index within the string where search starts.
end (Optional) -   ending index within the string where search ends.

Note: Index in Python starts from 0, not 1.

count() Return Value
count() method returns the number of occurrences of the substring in the given string.






The count() method returns the number of occurrences of a substring in the given string.

Example:

PROGRAM:

message = 'fell like freedom'
# number of occurrence of 'p'
print('Number of occurrence of p:', message.count('l'))

# Output: Number of occurrence of l: 3



Example 1: Count number of occurrences of a given substring:

Program:

# define string
string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)

# print count
print("The count is:", count)


Output:
The count is: 2


Example 2: Count number of occurrences of a given substring using start and end:

PROGRAM:

# define string
string = "fell like freedom"
substring = "l"
# count after first 'l' and before the last 'l'
count = string.count(substring, 3, 16 )
# print count
print("The count is:", count)

o/p= The count is: 2

Here, the counting starts after the first l has been encountered, i.e. 3th index position.

And, it ends before the last i, i.e. 16th index position.


