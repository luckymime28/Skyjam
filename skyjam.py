x = 0
def help():
    print("- So basically this is my first ever exploit I created")
    print("- My name is luckymime28 and this is my exploit skyjam.py")
    print("- skyjam.py is a password combination maker and password list creator")
    print("- Simply follow the instructions on screen and you should be fine")
    print("- Any questions? ask via instagram luckymime28, sorry if I take a while")
    print("Again, to begin, how old is the person? select a letter.")
print("- if you need more info or you're confused type 'help'")
print("To begin, how old is the person?")
while x == 0:
    ask = input("A.12-20 B.21-35 C.36-50 D.51+: ")
    ask = ask.lower()
    if ask == "a":
        print("I'll work on that in the future, too advanced :)")
    if ask == "b":
        print("I'll need to work on that one aswell, sorry :(")
    if ask == "c":
        print("Don't expect much")
    if ask == "d":
        x = x + 1
        import skyjam4
        quit()
    if ask == "help":
        help()
    else:
        print("Choose a letter dummy :)")