file = open("nums.txt", "r")
lines = file.readlines()
file.close()

# Edit
for x in range(len(lines)):
    try:
        number = int(lines[x]) * 2
        lines[x] = f"{number}\n"
    except Exception as e:
        pass

# Write
file = open("nums.txt", "w")
file.writelines(lines)
file.close()