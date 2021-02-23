x = 1
def Male():
    ask2 = input("First interest: ")
    ask3 = input("Second interest: ")
    ask4 = input("Third interest: ")
    name = input("What is the name on your system?: ")
    name2 = input("What would you like to name your .txt?: ")
    #DO NOT ADD '.TXT' AT THE END OF THE NAME, IT'S ALREADY AUTOMATICALLY ADDED!
    jam = open(f"/home/{name}/Desktop/{name2}.txt", "w")
    jam.write(ask2 + ask3 + ask4)
    jam.write(ask2.lower() + ask3.lower() + ask4.lower())
    jam.write(ask4 + ask3 + ask2)
    jam.write(ask2.upper() + ask3.upper() + ask4.upper())
    jam.write(ask3.upper() + ask4.upper() + ask2.upper())
    for x in range(10000):
        x = str(x)
        jam.write(x + ask2 + ask3 + ask4 + x)
        jam.write(x + ask2.upper() + ask3.upper() + ask4.upper() + x)
        jam.write(x + ask2.lower() + ask3.lower() + ask4.lower() + x)
        jam.close()
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
        print("Completed Successfully!")
        quit()
