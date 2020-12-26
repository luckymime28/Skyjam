x = 1
def Male():
    ask2 = input("First interest: ")
    ask3 = input("Second interest: ")
    ask4 = input("Third interest: ")
    print(" ")
    print(ask2 + ask3 + ask4)
    print(ask2.lower() + ask3.lower() + ask4.lower())
    print(ask4 + ask3 + ask2)
    print(ask2.upper() + ask3.upper() + ask4.upper())
    print(ask3.upper() + ask4.upper() + ask2.upper())
    for x in range(10000):
        x = str(x)
        print(x + ask2 + ask3 + ask4 + x)
        print(x + ask2.upper() + ask3.upper() + ask4.upper() + x)
        print(x + ask2.lower() + ask3.lower() + ask4.lower() + x)
def Female():
    print("Also worked")

print("The person you're targetting is 51+")
print("Type 'back' to go back to the main screen.")
while x == 1:
    askk = input("Are they Male or Female?: ")
    if askk == "m" or "male":
        x = x + 1
        Male()
    if askk == 'help':
        x = x + 1
    else:
        print("Invalid, are they MALE or FEMALE?")
