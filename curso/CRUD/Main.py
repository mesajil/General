


clients = "Luis,Cristian,Angel,Betsabe,Piero,"

def _add_coma ():
    global clients
    clients += ","

def _print_welcome ():
    print ("WELCOME TO LM VENTAS")
    print ("*" * 20)


def _print_menu ():
    print ("What would you like to do today ?")
    print ("[C]reate client")
    print ("[R]ead client's list")
    print ("[U]pdate client")
    print ("[D]elete client")

def list_clients ():
    global clients
    for c in clients.split(","):
        print(c)


def update_client (client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print ("'{}' is not in the client's list".format(client_name))

def create_client (client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print ("'{}' already is in the Client's list".format(client_name))

def delete_client (client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ",", "")
    else:
        print ("'{}' is not in the client's list".format(client_name))
    
    
def _get_client_name ():
    return input ("What is the client name?: ")

def _get_updated_client_name ():
    return input ("What is the updated client name?: ")

if __name__ == "__main__":
    _print_welcome()

    while (1):
        _print_menu()
        cmd = input ("").upper()
        if (cmd == "C"):
            client_name = _get_client_name()
            create_client (client_name)
        elif cmd == "R":
            list_clients()
        elif (cmd == "U"):
            client_name = _get_client_name()
            updated_client_name = _get_updated_client_name()
            update_client (client_name, updated_client_name)
        elif (cmd == "D"):
            client_name = _get_client_name()
            delete_client (client_name)
        else:
            print ("Invalid command")