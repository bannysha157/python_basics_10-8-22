6)str.encode():

The syntax of encode() method is: string.encode(encoding='UTF-8',errors='strict')


note: use this link  https://mothereff.in/utf- 8
errors -  response when encoding fails. There are six types of error response
strict -  default response which raises a UnicodeDecodeError exception on failure
ignore -  ignores the unencodable unicode from the result
replace -  replaces the unencodable unicode to a question mark ?
xmlcharrefreplace -  inserts XML character reference instead of unencodable unicode
backslashreplace - inserts a \uNNNN escape sequence instead of unencodable unicode
namereplace -    inserts a \N{...} escape sequence instead of unencodable unicode



Example 1: Encode to Default Utf-8 Encoding:

progrm:
# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)

Output:

The string is: pythön!
The encoded version is: b'pyth\xc3\xb6n!'


Example 2: Encoding with error parameter:
 program:

# unicode string
string = 'pythön!'
# print string
print('The string is:', string)
# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))
# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))

Output

The string is: pythön!
The encoded version (with ignore) is: b'pythn!'
The encoded version (with replace) is: b'pyth?n!'






