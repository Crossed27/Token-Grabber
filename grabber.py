print("""\

                           ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
                          ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                          ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
                          ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
                          ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
                           ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                   Type A Number To Choose An Option
                                                                                                         
""")

shitList = [
    "[1] Grab Token From Link",
    "[2] Coming Soon",
    "[3] Coming Soon"
]

for i in shitList:
    print(i)

strInput = input()

# define a function
def shitFunction():
    print("W.I.P")
    input()

if strInput == "1":
    shitFunction()

input()