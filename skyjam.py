print("- If you need more info or you're confused type 'help'")
def help():
    print("\n-So basically, this is my first exploit I ever created \n-My name is luckymime28, and this is my exploit skyjam.py \n-skyjam.py is a password combination maker and list creator \n-Simply follow the instructions on screen and you should be fine \n-Any questions? Ask via instagram luckymime28, sorry if I take a while.\nAlso I am in no way, shape, or form responsible if any damages occur from\nyou using my product.\n")
def more_info():
    print("- Level 1 is typically for those who have easy passwords\n You might want to save this one for the older people\n Typically just combines words together and generates a bunch of numbers\n")
    print("- Level 2 is more complex, it will include special symbols usually\n This might include weird letters in the end, beginning, special characters\n It will also generate or replace letters as numbers\n")
    print("- Level 3 is used for more specifics, for example,\n You know what the wording is, however not what might be the last character \n Try it out in case you forgot your password\n")
    print("NOTE: For more success, make sure to find more research on your target\nDon't just use this tool and input randoms as you'll be less successful!")

con = input("- Push Enter To continue to the Options\n> ")
if con.lower() == 'help':
    help()
while True:
    con2 = input("Which exploit would you like to navigate to?\n{a} Level 1\n{b} level 2\n{c} level 3\nIf you need more info for these types\ntype 'info'\n>> ")
    if con2.lower() == 'a':
        import skyjam4
    elif con2.lower() == 'b':
        import skyjam3
    elif con2.lower() == 'c':
        import skyjam2
    elif con2.lower() == "info":
        more_info()
    else:
        print("\n     INVALID TRY AGAIN     \n")
