# Imports packages
from mcstatus import JavaServer
from mcstatus import BedrockServer
import colorama



# Defines Menu
def menu():
    colorama.Fore.RESET
    choice = input("Type Java for Java edition Servers or Bedrock for Bedrock edition server: ")

    return choice


# Defines Fnc1
def function1():

    try:

        # Gets IP
        user_input = input("Input valid server ip: ")
        server = JavaServer.lookup(user_input)
        status = server.status()
        

        # Prints the amount of Players online \ Prints MOTD
        print(colorama.Fore.CYAN, f"{user_input} has a max player count of {status.players.max}")
        print(colorama.Fore.LIGHTGREEN_EX, f"{user_input} has {status.players.online} player(s) online and replied in {status.latency} ms")


        # Gets player(s) name
        query = server.query()
        print(colorama.Fore.LIGHTGREEN_EX, f"{user_input} has the following players online: {query.players.names()}")


    # Handles errors
    except Exception as error:
        print(colorama.Fore.LIGHTRED_EX, f"An error has ocurred: {error}")
        if status.latency > 0:
            print(colorama.Fore.YELLOW, "The inputted Server is still up either query in server.properties is disabled or the server is under too much load to respond.")
            print(colorama.Fore.YELLOW, "Note: Most servers have query disabled", colorama.Fore.RESET)


# Defines Func2
def function2():

    try:
        
        # Gets bedrock IP
        bruser_input = input("Input valid server ip: ")
        brserver = BedrockServer.lookup(bruser_input)


        status = brserver.status()

        print(f"{bruser_input} has a max player count of {status.players.max}")
        print(colorama.Fore.LIGHTGREEN_EX, f"{bruser_input} has {status.players.online} player(s) online and replied in {status.latency} ms")
        print()

    except Exception as brerror:
        print(colorama.Fore.LIGHTRED_EX, f"An error has ocurred: {brerror}")


# Defines choices
while True:

    choice = menu()

    match choice:

        # Func1
        case "Java":
            function1()

        
        # Func2
        case "Bedrock":
                function2()

        
        # Invalid choice
        case _:
            print(colorama.Fore.RED, "Invalid choice", colorama.Fore.RESET)
            