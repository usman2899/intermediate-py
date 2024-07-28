# can do below or r+ but many edge cases which messes up -- so better to read, edit and write
# open("daemon.txt", "w+")

# Read
file = open("cheese.txt", "r")
lines = file.readlines()
file.close()

# Edit
# lines = ["Hello\n", "How r u"]
# lines.insert(0, "I like cheese\n")

#Get last lines add line break and add end of file
lines[-1] =lines[-1] + "\n"
lines.append("Goodbye")

# Write
file = open("cheese.txt", "w")
file.writelines(lines)
file.close()