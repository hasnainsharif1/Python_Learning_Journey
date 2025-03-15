# Conditional Statements (if, elif, else)
x = 10
if x > 15:
    result = "Greater than 15"
elif x == 10:
    result = "Equal to 10"
else:
    result = "Less than 15"

# Loop with else suite
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop completed without break")

# Nested loops
for i in range(2):
    for j in range(2):
        print(f"Nested Loop i={i}, j={j}")

# Infinite loop (commented to prevent execution)
# while True:
#     print("This is an infinite loop")

# Pass statement (used as a placeholder)
def my_function():
    pass  # Placeholder for future code

# Continue statement (skipping an iteration)
for num in range(5):
    if num == 2:
        continue  # Skip number 2
    print(num)

# Break statement (exit loop prematurely)
for num in range(5):
    if num == 3:
        break  # Stop loop at 3
    print(num)

# Assert statement (check conditions)
assert x == 10, "x is not 10"  # Will not raise an error since x == 10

# Return statement inside a function
def add(a, b):
    return a + b

sum_result = add(5, 7)

# Output results (optional)
print(result)
print("Sum:", sum_result)
