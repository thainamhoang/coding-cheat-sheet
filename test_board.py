def replacing (string):
    if "?" not in string:
        print(string)
    else:
        replacing(string.replace("?", "0", 1))
        replacing(string.replace("?", "1", 1))

print(replacing("1???10?011"))