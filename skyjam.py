x = 0
def help():
    print("-So basically, this is my first exploit I ever created \n-My name is luckymime28, and this is my exploit skyjam.py \n-skyjam.py is a password combination maker and list creator \n-Simply follow the instructions on screen and you should be fine \n-Any questions? Ask via instagram luckymime28, sorry if I take a while.\nAlso I am in no way, shape, or form responsible if any damages occur from\nyou using my product.")
print("- if you need more info or you're confused type 'help'")
while x == 0:
    con = input("Type 'a' To continue to the Exploit\n> ")
    if con.lower() == 'a':
        import skyjam4
        quit()
    elif con.lower() == 'help':
        help()
    else:
        print("That didn't work, type 'a' to continue\nor type 'help' for help.")
