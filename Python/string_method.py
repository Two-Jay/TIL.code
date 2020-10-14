
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


***

#  string.startswith(<string>) - 대상 string이 <string>으로 시작된다면 True를, 그렇지 않다면 False를 반환한다.


txt = "superman"
print(txt.startswith("s")) # True
print(txt.startswith("a")) # False
print(txt.startswith("super")) # True


# my implement of this method

def my_startsWith(string1, string2):
    target = string1[0:len(string2)-1]
    for i in range(len(target)-1):
        if string1[i] != string2[i]:
            return False
    return True


***


#  string.split(<string>) - 매개변수로 주어진 문자열을 기준으로 문자열을 분리하여 리스트로 반환합니다.
#           매개변수로 입력하지 않을 시에는 ""(공백)을 기준으로 분리한다.

langs = "Korean, English, Arabic, Javascript, Python"
langs_list = langs.split(",")
print(langs_list) # ['Korean', ' English', ' Arabic', ' Javascript', ' Python']

intro = "Hi, this is Aiden."
print(intro.split()) # ['Hi,', 'this', 'is', 'Aiden.']


def my_split(string, delimiter):

    result_list = []

    if not delimiter:
        raise ValueError("Empty Separator")
    if not string:
        return [string]

    start = 0
    for index, char in enumerate(string):
        if char == delimiter:
            result_list.append(string[start:index])
            start = index + 1
    if start == 0:
        return [string]
    result_list.append(string[start:index + 1])
    
    return result_list


***

#  string.upper() - 대상 문자열의 소문자를 모두 대문자로 치환하여 반환한다.
#  string.lower() - 대상 문자열의 대문자를 모두 소문자로 치환하여 반환한다.
#           위의 메소드는 Immutable하다! 즉, 대상 문자열을 직접 바꾸지 아니한다.


intro = "Hello, this is Aiden"
print(intro.upper()) # HELLO, THIS IS AIDEN
print(intro.lower()) # hello, this is aiden
print(intro) # Hello, this is Aiden


def my_upper(string):
    splited_list = list(string)
    for i in range(len(splited_list)):
        if ord(splited_list[i]) >= 97 and ord(splited_list[i]) <= 122:
            splited_list[i] = chr((ord(splited_list[i])-32))
    return "".join(splited_list)

def my_lower(string):
    splited_list = list(string)
    for i in range(len(splited_list)):
        if ord(splited_list[i]) >= 65 and ord(splited_list[i]) <= 90:
            splited_list[i] = chr((ord(splited_list[i])+32))
    return "".join(splited_list)


***

#  string.replace(<string1>, <string2>) - 대상 문자열에서 대상 문자 <string1>을 찾아서 <string2>로 대체한다.
#           2번째 매개변수를 주지 않았다면, ""(공백)을 기본값으로 한다.
#           위의 메소드는 Immutable하다! 즉, 대상 문자열을 직접 바꾸지 아니한다.
    

intro = "제 이름은 Aiden입니다."
print(intro.replace("Aiden", "김정준")) # 제 이름은 김정준입니다.
# 두번째 파라미터를 ""로 주면 대상 문자열을 삭제할 수도 있다.

intro = "제 이름은 Aiden입니다."
print(intro.replace("Aiden", "")) # 제 이름은 입니다.
print(intro.replace(" ", "")) # 제이름은Aiden입니다. | 띄어쓰기 삭제!
print(intro) # 제 이름은 Aiden입니다.

# 리스트에 있는 요소들의 느낌표, 작은따옴표, 쉼표를 제거하는 함수
def remove_special_characters(text):
    processed_text = []
    for i in text:
        target = i.replace(",","").replace("!","").replace("'","")
        processed_text.append(target)
    return processed_text


***

#  strip() -  문자열 내에서 불필요한 공백문자를 없애어 준다.
#         - /n 