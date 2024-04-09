# Imports packages
from mcstatus import *
import colorama


# Initializes colorama
class Colours:

    RESET = colorama.Fore.RESET
    GREEN = colorama.Fore.GREEN
    RED = colorama.Fore.RED
    CYAN = colorama.Fore.CYAN
    YELLOW = colorama.Fore.YELLOW
    MAGENTA = colorama.Fore.MAGENTA
    ORANGE = '\033[38;5;214m'

    L_GREEN = colorama.Fore.LIGHTGREEN_EX
    L_RED = colorama.Fore.LIGHTRED_EX
    L_CYAN = colorama.Fore.LIGHTCYAN_EX
    L_YELLOW = colorama.Fore.LIGHTYELLOW_EX
    L_MAGENTA = colorama.Fore.LIGHTMAGENTA_EX


# Defines Menu
def menu():
    
    print(Colours.CYAN, "1. Java")
    print(Colours.CYAN, "2. Bedrock")
    print(Colours.CYAN, "3. Exit", colorama.Fore.RESET)

    choice = input("Choose a server type: ")

    try:
        choice = int(choice)
        return choice
    except ValueError:
        pass
    
    if type(choice) == str:
        choice = choice.lower()

    return choice


# Defines Fnc1
def javaServer():

    # Gets IP
    user_input = input("Input valid server ip: ")
    port = input("Input valid server port: ")
    
    try: 
        
        server = JavaServer.lookup(f"{user_input}:{port}")

    except Exception as error:
        print(Colours.L_RED, f"An error has ocurred: {error}")
        return
    
    status = server.status()

    
    # Prints the amount of Players online 
    print(Colours.CYAN, f"{user_input} has a max player count of {status.players.max}")
    print(Colours.CYAN, f"{user_input} has {status.players.online} player(s) online and replied in {status.latency} ms")
    

    try:
        # Gets player(s) name
        query = server.query()
        print(Colours.L_GREEN, "Players online: ", query.players.names)

    except Exception as error:
        print(Colours.L_RED, f"An error has ocurred: {error}")
        print(Colours.ORANGE, "This server does not query enabled in server.properties")


# Defines Func2
def bedrockServer():

    try:
        
        # Gets bedrock IP
        BRuser_input = input("Input valid server ip: ")
        BRserver = BedrockServer.lookup(BRuser_input)
        status = BRserver.status()


        print(f"{BRuser_input} has a max player count of {status.players.max}")
        print(Colours.CYAN, f"{BRuser_input} has {status.players.online} player(s) online and replied in {status.latency} ms")
        

    except Exception as BRerror:
        print(Colours.L_RED, f"An error has ocurred: {BRerror}")


# Defines choices
while True:

    choice = menu()

    match choice:

        # Func1
        case 1 | "java":
            javaServer()

        # Func2
        case 2 | "bedrock":
            bedrockServer()

        case 3 | "exit":
            exit()

        # Invalid choice
        case _:
            print(Colours.L_RED, "Invalid choice", Colours.RESET)