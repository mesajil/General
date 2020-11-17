import csv

CLIEN_SCHEMA = ["name", "gmail"]
clients = [
    {
        "name":"Luis",
        "gmail":"luis@gmail.com"
    },
    {
        "name":"Cristian",
        "gmail":"cristian@gmail.com"
    }
]


def _print_welcome ():
    print ("WELCOME TO LM VENTAS")
    print ("*" * 20)


def _print_menu ():
    print ("What would you like to do today?")
    print ("[C]reate client")
    print ("[R]ead client's list")
    print ("[U]pdate client")
    print ("[D]elete client")

def list_clients ():
    for i,client in enumerate(clients):
        print (i)
        for field in client:
            print (client[field])


def update_client (client_id, updated_client):
    global clients
    try:
        clients[client_id] = updated_client
    except:
        print ("Didn't find the client's id")


def create_client (client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print ("Client already is in the Client's list")

def delete_client (client_id):
    global clients
    try:
        del clients[client_id]
    except:
        print ("Didn't find the client's id")

    
def _get_client_field (field_name):
    field = None
    while not field:
        field = input ("What is the client {}?: ".format(field_name))
    return field


def ingress_client_data ():
    client = {}
    for field in CLIEN_SCHEMA:
        client[field] = _get_client_field(field)
    return client

if __name__ == "__main__":
    _print_welcome()

    while (1):
        _print_menu()
        cmd = input ("").upper()
        if (cmd == "C"):
            client = ingress_client_data()
            create_client (client)
        elif cmd == "R":
            list_clients()
        elif (cmd == "U"):
            updated_client = ingress_client_data()
            id_client = int(_get_client_field("id"))
            update_client (id_client, updated_client)
        elif (cmd == "D"):
            id_client = int(_get_client_field("id"))
            delete_client (id_client)
        else:
            print ("Invalid command")