with open("test.txt", "r") as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()
