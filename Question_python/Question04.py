#Check if string is a palindrome

def str_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True
    
print(str_palindrome('madam'))