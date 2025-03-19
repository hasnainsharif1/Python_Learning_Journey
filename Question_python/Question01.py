#For lower to upper case 
def upper_Case(s):
    result = ""
    for char in s:
        if 'a' <= char >= 'z' :
            result += chr(ord(char)-32)
        else:
            result += char
    return result
print(upper_Case('helo'))

#For upper to lower case
def lower_case(s):
    result = ""
    for char in s:
        if 'A' <= char >= 'Z':
            result = chr(ord(char)+32)
        else:
            result += char
    return result

print(lower_case('HASNAIN'))

