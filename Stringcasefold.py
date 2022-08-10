2)str.caseflod()
The syntax of the casefold() method is: str.casefold()
Here, str is a string.

casefold() Parameters
The casefold() method doesn't take any parameters.

casefold() Return Value
The casefold() method returns:   a lowercased string


The casefold() method converts all characters of the string into lowercase letters and returns a new string.

Example:
program:

text = "pYtHon"
# convert all characters to lowercase
lowercased_string = text.casefold()
print(lowercased_string)

# Output: python

Example 1: Python casefold():
program:

text = "PYTHON IS FUN"
# converts text to lowercase
print(text.casefold())

Output:

python is fun
In the above example, we have used the casefold() method to convert all the characters of text to lowercase.

Here, text.casefold() modifies the value of string1 and returns 'python is fun'.









xample 2: casefold() as an Aggressive lower() Method:

    
The casefold() method is similar to the lower() method but it is more aggressive. This means the casefold() method converts more characters into lower case compared to lower() .

For example, the German letter ß is already lowercase so, the lower() method doesn't make the conversion.

But the casefold() method will convert ß to its equivalent character ss.

ptogram:

text = 'groß'
# convert text to lowercase using casefold()
print('Using casefold():', text.casefold())
# convert text to lowercase using lower()
print('Using lower():', text.lower())

Output:

Using casefold(): gross
Using lower(): groß

In the above example, we have used the casefold() and lower() methods to convert 'groß'.

The casefold() method also converts 'ß' to lowercase whereas lower() doesn't.
