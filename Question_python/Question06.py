# input aaabbcc, output: a3b2c2
#using join method

def compressor(s):
    dict = {}

    for char in s:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    
    output = ''.join(f"{key}{value}" for key, value in dict.items())
    return output

print(compressor('aaabbccdddd'))