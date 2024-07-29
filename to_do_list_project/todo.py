import sys

# Print List
print("\nHere's your ToDo list:\n")
print("1. Walk the Dog")
print("2. Buy Cheese")

# Print Commands
print("\n*******************************\n")
print(f"To view ToDos:\n{sys.argv[0]}")
print(f"\nTo add a ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")

file_name = "todo.txt"

if sys.argv[1] == "add":
    try:
        file = open(file_name, "a")
        file.write(f"{sys.argv[2]} \n")
        file.close()
    except:
        pass
elif sys.argv[1] == "remove":
    try:
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()

        lines.pop(int(sys.argv[2]))
        print(lines)

        file = open(file_name, "w")
        file.writelines(lines)
        file.close()
    except:
        pass
else:
    print("Invalid input")

print(sys.argv[2])