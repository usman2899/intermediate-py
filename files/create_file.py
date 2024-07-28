import sys

# Creates only if the file doesn't exist
file = open("cheese.txt", "x")
file.write("X marks the spot")
#If not closed below doesnt overwrite proper instead goes: For the W!e spot
file.close()

# Overwrite
file = open("cheese.txt", "w")
file.write("For the W!")
file.close()

# Append
file = open("cheese.txt", "a")
file.write("A+ work")
file.close()


try:
    name = (f"{sys.argv[1]}.txt")
    file = open(name, "x")
    file.write(sys.argv[2])
    file.close()
except:
    print ("Incorrect format")
