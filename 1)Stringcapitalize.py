1)str.capitalize():

syntax: string.capitalize()
capitalize() Parameter
The capitalize() method doesn't take any parameter.

capitalize() Return Value
The capitalize() method returns:

a string with the first letter capitalized and all other characters in lowercase

The capitalize() method converts the first character of a string to an uppercase letter and all other alphabets to lowercase.

Example1:
program:
sentence = "i love PYTHON"
# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()
print(capitalized_string)
# Output: I love python







Example 1: Python capitalize():
program:

sentence = "python is AWesome."
# capitalize the first character
capitalized_string = sentence.capitalize()
print(capitalized_string)

Output:

 Python is awesome.
In the above example, we have used the capitalize() method to convert the first character of the sentence string to uppercase and the other characters to lowercase.

Here, sentence.capitalize() returns "Python is awesome" which is assigned to capitalized_string.




Example 2: capitalize() Doesn't Change the Original String:

The capitalize() method returns a new string and doesn't modify the original string. For example:
program:
sentence = "i am learning PYTHON."
# capitalize the first character
capitalized_string = sentence.capitalize()
# the sentence string is not modified
print('Before capitalize():', sentence)
print('After capitalize():', capitalized_string)

Output:

Before capitalize(): i am learning PYTHON.
After capitalize(): I am learning python.
Here, the capitalize() method doesn't modify the original sentence string.
                                                                                   
                                                           
