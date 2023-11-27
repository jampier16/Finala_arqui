import socket 

SOCK_BUFFER= 1024

if __name__=='__main__':
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address= ('localhost', 5000)
    sock.connect(server_address)

    while True:
        electromestico= input('Ingrese el nombre del electrodomestico: ')
        sock.sendall(electromestico.encode())
        respuesta= sock.recv(SOCK_BUFFER).decode()
        print(respuesta)
        if respuesta=='1':
            print('Producto en stock. Pedido procesando.')
        else:
            print('Producto agotado. Pedido no procesado.')

        