
   # 아래는 파이썬에서 문자열을 다루는 built-in 메소드들이다.
    
###
#  capitalize() - Converts the first character to upper case
#  casefold() - Converts string into lower case
#  center() - Returns a centered string
#  count() -  Returns the number of times a specified value occurs in a string
#  encode() - Returns an encoded version of the string
#  endswith() - Returns true if the string ends with the specified value
#  expandtabs() - Sets the tab size of the string
#  find() - Searches the string for a specified value and returns the position of where it was found
#  format() - Formats specified values in a string
#  format_map() - Formats specified values in a string
#  index() -  Searches the string for a specified value and returns the position of where it was found
#  isalnum() -  Returns True if all characters in the string are alphanumeric
#  isalpha() -  Returns True if all characters in the string are in the alphabet
#  isdecimal() -  Returns True if all characters in the string are decimals
#  isdigit() -  Returns True if all characters in the string are digits
#  isidentifier() - Returns True if the string is an identifier
#  islower() -  Returns True if all characters in the string are lower case
#  isnumeric() -  Returns True if all characters in the string are numeric
#  isprintable() -  Returns True if all characters in the string are printable
#  isspace() -  Returns True if all characters in the string are whitespaces
#  istitle() -  Returns True if the string follows the rules of a title
#  isupper() -  Returns True if all characters in the string are upper case
#  join() - Joins the elements of an iterable to the end of the string
#  ljust() -  Returns a left justified version of the string
#  lower() -  Converts a string into lower case
#  lstrip() - Returns a left trim version of the string
#  maketrans() -  Returns a translation table to be used in translations
#  partition() -  Returns a tuple where the string is parted into three parts
#  replace() -  Returns a string where a specified value is replaced with a specified value
#  rfind() -  Searches the string for a specified value and returns the last position of where it was found
#  rindex() - Searches the string for a specified value and returns the last position of where it was found
#  rjust() -  Returns a right justified version of the string
#  rpartition() - Returns a tuple where the string is parted into three parts
#  rsplit() - Splits the string at the specified separator, and returns a list
#  rstrip() - Returns a right trim version of the string
#  split() -  Splits the string at the specified separator, and returns a list
#  splitlines() - Splits the string at line breaks and returns a list
#  startswith() - Returns true if the string starts with the specified value
#  strip() -  Returns a trimmed version of the string
#  swapcase() - Swaps cases, lower case becomes upper case and vice versa
#  title() -  Converts the first character of each word to upper case
#  translate() -  Returns a translated string
#  upper() -  Converts a string into upper case
#  zfill() -  Fills the string with a specified number of 0 values at the beginning
###

***

# capitalize() - 문자열의 첫 번째 문자를 대문자로 바꾼다.

text = "hi, this is kim."
result = text.capitalize()
print (result) # "Hi, this is kim"

# my implement of this method
def my_capitalize(string):
    zeroth_char = string[0]
    if ord(zeroth_char) >= 97 and ord(zeroth_char) <= 122:
        zeroth_char = chr(ord(zeroth_char) - 32)
    return zeroth_char + string[1:]

***

#  casefold() - 존재하는 모든 영문 대문자를 소문자로 만든다.

txt = "HeLLo, And WelCOME To My WORld!"
x = txt.casefold()
print(x) # hello, and welcome to my world!

# my implement of this method

# def my_casefold(string)
#     splited = "".split(string)
    

# def my_lowercase(string)
#     result = ''
#     for i in range(len(string)-1):
#         if ord(string[i]) >= 65 and ord(string[i]) >= 90:
#             result.join(char(ord(string[i])+32))\
#     return result