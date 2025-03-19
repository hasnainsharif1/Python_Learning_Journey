def index_number(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1

    
    return max(result, key=result.get)
    # return max_character

    # for i in range(len(s)):
    #     if result[s[i]] == 1:
    #         return i
        
    # return -1

print(index_number('Hasnain'))