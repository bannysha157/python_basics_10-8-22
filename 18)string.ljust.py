18)str.ljust():  the string ljust() method returns a left-justified string of a given minimum width.

The syntax of ljust() method is:  string.ljust(width[, fillchar])
  
Here, fillchar is an optional parameter.


Example 1: Left justify string of minimum width:
    
    program:
      
# example string
string = 'cat'
width = 5
# print left justified string
print(string.ljust(width))

o/p:
cat  
Here, the minimum width defined is 5. So, the resultant string is of minimum length 5.

And, the string cat is aligned to the left which makes leaves two spaces on the right of the word.


Example 2: Left justify string and fill the remaining spaces:
    
# example string
string = 'cat'
width = 5
fillchar = '*'
# print left justified string
print(string.ljust(width, fillchar))

Output:
cat**
Here, the string cat is aligned to the left, and the remaining two spaces on the right is filled with the character *.

