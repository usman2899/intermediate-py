direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "east":
        print("Left")
    case "west":
        print("Right")
    case _:
        print("not valid bro")
    