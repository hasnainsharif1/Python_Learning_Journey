# Arithmetic Operators
a = 10
b = 5
sum_result = a + b  # Addition
diff_result = a - b  # Subtraction
prod_result = a * b  # Multiplication
div_result = a / b  # Division
mod_result = a % b  # Modulus

# Comparison Operators
is_greater = a > b  # True if a is greater than b
is_equal = a == b  # True if a and b are equal
is_not_equal = a != b  # True if a and b are not equal

# Logical Operators
x = True
y = False
and_result = x and y  # False (both should be True)
or_result = x or y  # True (at least one True)
not_result = not x  # False (negation of True)

# Assignment Operators
num = 10
num += 5  # Equivalent to num = num + 5
num -= 3  # Equivalent to num = num - 3
num *= 2  # Equivalent to num = num * 2
num /= 4  # Equivalent to num = num / 4

# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
identity_check = list1 is list2  # False, different objects in memory
identity_not_check = list1 is not list2  # True

# Membership Operators
fruits = ["apple", "banana", "cherry"]
is_in_list = "apple" in fruits  # True
is_not_in_list = "grape" not in fruits  # True

# Output results (Optional)
print(sum_result, diff_result, prod_result, div_result, mod_result)
print(is_greater, is_equal, is_not_equal)
print(and_result, or_result, not_result)
print(num)
print(identity_check, identity_not_check)
print(is_in_list, is_not_in_list)
