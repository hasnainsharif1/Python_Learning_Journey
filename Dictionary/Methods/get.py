profile = {
    'name':'hasnain', 'age': 23
}

age = profile.get('age', 'not found') #passing default value, if age or any value not found
print(age)