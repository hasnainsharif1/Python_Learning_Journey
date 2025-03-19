def index_number(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    for i in range(len(s)):
        if result[s[i]] == 1:
            return i
        
    return -1

print(index_number('aasnain'))