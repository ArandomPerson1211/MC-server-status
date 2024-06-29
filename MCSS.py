# Imports packages
from mcstatus import *
import colorama
import time


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
    
    print(Colours.L_MAGENTA, "1. Java")
    print(Colours.L_MAGENTA, "2. Bedrock")
    print(Colours.L_MAGENTA, "3. Exit", colorama.Fore.RESET)

    choice = input("Choose a server type: ")

    try:
        choice = int(choice)
        return choice
    except ValueError:
        pass
    
    if type(choice) == str:
        choice = choice.lower()

    return choice


# Defines javaServer
def javaServer():

    # Gets IP
    user_input = input("Input valid server ip: ")

    # Define Valid IP Check / Valid IP Check Raw / The Raw Means a IP with only numbers
    user_inputVIPCR = user_input.count(".")
    user_inputVIPC = not any(char.isalpha() for char in user_input)

    if user_inputVIPCR > 3:
        pass
    else: 
        if user_inputVIPC:
            print(Colours.L_RED, "Invalid input")
            Colours.RESET
            return javaServer()
        else:
            pass
            

    if ":" in user_input:
        user_input = user_input.split(":")[0]

    port = input("Input valid server port (Optinal press enter for defualt port): ")
    
    try: 
        server = JavaServer.lookup(f"{user_input}:{port}")
    except Exception as error:
        print(Colours.L_RED, f"An error has occurred: {error}")
        return

    status = server.status()

    # Prints the amount of Players online 
    print(Colours.CYAN, f"{user_input} has {status.players.online} player(s) online and replied in {status.latency} ms")

    # attempts to Gets player(s) name 
    try:
        
        query = server.query()
        print(Colours.L_GREEN, "Players online: ", query.players.names)
        # Activates query if it gets a response when trying to query
        query_output = True
    # If it does not get a response when trying to query it will print an error and warn the user that it does not have query/rcon enabled
    except Exception as error:
        print(Colours.L_RED, f"An error has occurred: {error}")
        print(Colours.ORANGE, "This server does not have query/rcon enabled in server.properties")
        # Deactivates query if it does not get a response when trying to query
        query_output = False

    repeat = input(Colours.CYAN + "Would you like to keep a live stream of the server? (y/n): ")


    # Checks if user wants to keep a live stream
    if repeat == "y":
        length = input("How many seconds would you like to wait between each check?: ")

        try:
            length = int(length)
        except ValueError:
            print(Colours.L_RED, "Invalid input")
            return
        
        while True:
            time.sleep(length)
            try:
                status = server.status()
                print(Colours.CYAN, f"{user_input} has {status.players.online} player(s) online and replied in {status.latency} ms")
            except Exception as error:
                print(Colours.L_RED, f"An error has occurred: {error}")
                print(Colours.ORANGE, "This server may be offline or the address is incorrect")

            # if query is True it tries to query if query is False it does not try to query
            if query_output:
                try:
                    query = server.query()
                    print(Colours.L_GREEN, "Players online: ", query.players.names)
                except Exception as error:
                    print(Colours.L_RED, f"An error has occurred: {error}")
                    print(Colours.ORANGE, "This server does not have query enabled in server.properties")
            else:
                print(Colours.ORANGE, "This server does not have query enabled in server.properties")



# Defines bedrockServer
def bedrockServer():

    try:
        
        # Gets bedrock IP
        BRuser_input = input("Input valid server ip: ")
        BRserver = BedrockServer.lookup(BRuser_input)
        status = BRserver.status()


        print(Colours.CYAN, f"{BRuser_input} has a max player count of {status.players.max}")
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


    # End of code
    while exit:
        Colours.RESET