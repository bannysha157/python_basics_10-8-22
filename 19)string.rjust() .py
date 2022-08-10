19)str.rjust(): The string rjust() method returns a right-justified string of a given minimum width.

The syntax of rjust() method is:  string.rjust(width[, fillchar])
Here, fillchar is an optional parameter.

String rjust() Parameters: The rjust() method takes two parameters:

width -  width of the given string. If width is less than or equal to the length of the string, original string is returned.
fillchar (Optional) - character to fill the remaining space of the width
Return value from String rjust()


The rjust() method returns the right-justified string within the given minimum width.

If fillchar is defined, it fills the remaining space with the defined character.


Example 1: Right justify string of minimum width:
    
# example string
string = 'cat'
width = 5
# print right justified string
print(string.rjust(width))
 
Output:
  cat
Here, the minimum width defined is 5. So, the resultant string is at least of length 5.

Now, rjust() aligns the string cat to the right leaving two spaces to the left of the word.


Example 2: Right justify string and fill the remaining spaces:
    
# example string
string = 'cat'
width = 5
fillchar = '*'
# print right justified string
print(string)

Output:
**cat
Here, the string cat is aligned to the right and the remaining two spaces on its left are filled with the fillchar *.





