import sys

prod = 1
for argument in sys.argv:
    try:
        num = int(argument)

        # For decimals
        # num = float(argument)
        prod *= num
    except:
        print (f"{argument}: is not a number")

print(prod)