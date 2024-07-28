file = open("daemon.txt", "r")

# content = file.read()
# print(content)

# If above not commented it starts from bottom and returns null array, either close the above file before reopening again
# lines = file.readlines() 
# print(lines)

for line in file:
    print(line)

file.close