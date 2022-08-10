3)center():
The syntax of the center() method is: str.center(width, [fillchar])
Here, str is a string.

center() Parameters: The center() method takes two parameters:

width - length of the string with padded characters
fillchar (optional) - padding character
Note: If fillchar is not provided, whitespace is taken as the default argument.

center() Return Value:
The center() method returns: a string padded with specified fillchar

Note: The center() method doesn't modify the original string.



The center() method returns a new centered string after padding it with the specified character.

Example:
Program:
sentence = "Python is awesome"

# returns the centered padded string of length 24
new_string = sentence.center(24, '*')
print(new_string)

# Output: ***Python is awesome****


Example:

Program:

sentence = "fell like freedom"
# returns the centered padded string of length 20
new_string = sentence.center(20, '$')

print(new_string)

o/p= $fell like freedom$$




Example 2: center() with Default Argument:

progrm:

text = "fell like freedom"
# returns padded string by adding whitespace up to length 24
new_text = text.center(24)
print("Centered String: ", new_text)

Output:

Centered String:     fell like freedom

Here, we have not passed the fillchar parameter in the center() method. The method pads whitespace to text making the length of the centered string 24.

