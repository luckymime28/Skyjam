print("\nLEVEL 2\n")
n = "\n"
import getpass
user = getpass.getuser()
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "\n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
def feedback():
    return "[SUCCESS] Check your Desktop/Directory to see your list!"
def Every_Other(p):
    p2 = ""
    capitalize = True
    for letter in p:
        if capitalize is True:
            p2 += letter.upper()
        elif capitalize is not True:
            p2 += letter.lower()
        if capitalize != " ":
            capitalize = not capitalize
    jam.write(p2 + n)
    Every_Other2(p)
def Every_Other2(p):
    p2 = ""
    capitalize = True
    for letter in p:
        if capitalize is not True:
            p2 += letter.upper()
        elif capitalize is True:
            p2 += letter.lower()
        if capitalize != " ":
            capitalize = not capitalize
    jam.write(p2 + n)
    Numbered_Words(p)
def Numbered_Words(p):
    p2 = p
    if p.count('o') or p.count('O'):
        p2 = p.replace('o', '0')
        p2 = p2.replace('O', '0')
        jam.write(p2 + n)
    if p.count('l') or p.count('L'):
        p2 = p2.replace('l', '1')
        p2 = p2.replace('L', '1')
        jam.write(p2 + n)
    if p.count('e') or p.count('E'):
        p2 = p2.replace('e', '3')
        p2 = p2.replace('E', '3')
        jam.write(p2 + n)
    if p.count('a') or p.count('A'):
        p2 = p2.replace("a", '4')
        p2 = p2.replace('A', '4')
        jam.write(p2 + n)
    if p.count('g') or p.count("G"):
        p2 = p2.replace("g", '9')
        p2 = p2.replace("G", '9')
        jam.write(p2 + n)
    if p.count('o') or p.count('O'):
        p = p.replace('o', '()')
        p = p.replace('O', '()')
        jam.write(p + n)
    if p.count('l') or p.count('L') or p.count("i") or p.count("I"):
        p = p.replace('l', '!')
        p = p.replace('L', '!')
        p = p.replace("i", "!")
        p = p.replace('I', "!")
        jam.write(p + n)
    if p.count('e') or p.count('E'):
        p = p.replace('e', '3')
        p = p.replace('E', '3')
        jam.write(p + n)
    if p.count('a') or p.count('A'):
        p = p.replace("a", '@')
        p = p.replace('A', '@')
        jam.write(p + n)
    if p.count('g') or p.count("G"):
        p = p.replace("g", '9')
        p = p.replace("G", '9')
        jam.write(p + n)
    if p.count('s') or p.count("S"):
        p = p.replace("s", "$")
        p = p.replace("S", "$")
        jam.write(p + n)
    jam.close()
    print(feedback())
    quit()
def help():
    print("\n- Follow the directions to create your own password list\n- If you want or need to add an alternate directory,\n- Type 'change' once it asks what OS you're using!\n")
try:
    print("Follow the directions, or type 'help' for other\ntypes of options if there are issues.")
    ask = input("Otherwise push Enter to continue: ")
    if ask.lower() == 'help':
        help()
    p = input("First Word > ")
    #p2 = input("Second Word > ")
    #p3 = input("Third Word > ")
    Sys = input("Are you currently using Windows or Linux?[K/W] > ")
    if Sys.lower() != 'change' and Sys.lower() == 'k':
        name = input("What is the name of your System > ")
    name2 = input("What would you like to name your .txt? > ")
    if Sys.lower() == 'change':
        change = input("\nTYPE IN YOUR ALTERNATE DIRECTORY HERE\nREMEMBER TO INCLUDE THE NAME OF YOUR FILE AND ITS EXTENSION\nDO NOT INCLUDE ANY QUOTATION MARKS!!!\n>> ")
        jam = open(f"{change}", "w")
    elif Sys.lower() == 'w':
        try:
            jam = open(f"C:/Users/{user}/Onedrive/Desktop/{name2}.txt", 'w')
        except FileNotFoundError:
            jam = open("C:/users/{}/desktop/{}.txt".format(user, name2), 'w')
    elif Sys.lower() == 'k':
        jam = open(f"/home/{name}/Desktop/{name2}.txt", 'w')
    Every_Other(p)
except FileNotFoundError or UnboundLocalError:
    print("Your Directory Wasn't Found...\nDid you input the correct System/Directory?")
    quit()
