


clients = "Pablo,Ricardo,"

def __add_coma ():
    global clients
    clients += ","

def __print_welcome ():
    print ("WELCOME TO LM VENTAS")
    print ("*" * 20)


def __print_menu ():
    print ("What would you like to do today ?")
    print ("[C]reate client")
    print ("[D]elete client")

def list_clients ():
    global clients
    for c in clients.split(","):
        print(c)


def create_client (client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        __add_coma()
    else:
        print ("Client already is in the Client's list")

if __name__ == "__main__":
    __print_welcome()

    while (1):
        __print_menu()
        cmd = input ("")
        if (cmd == "C"):
            client_name = input ("What is the client name?: ")
            create_client (client_name)
            list_clients()
        elif (cmd == "D"):
            pass
        else:
            print ("Invalid command")