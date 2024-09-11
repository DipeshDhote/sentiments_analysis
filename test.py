with open("requirements.txt") as file:
    content = file.readlines()
    content = [con.count('\n',) for con in content]
    print(content)