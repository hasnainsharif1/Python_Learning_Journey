# yield keyword for acessing one value

def counter(num):
    while num > 0:
        yield num
        num -= 1

for number in counter(10):
    print(number)