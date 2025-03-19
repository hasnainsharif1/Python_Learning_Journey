try:
    file = open('C:/Users/hasna/OneDrive/Documents/GitHub/Python_Learning_Journey/Exception_Handling/notes.txt')
    content = file.read()
    print(content)

except:
    print(f"File no found!")

finally:
    file.close()
    print(f"File operation completed.")