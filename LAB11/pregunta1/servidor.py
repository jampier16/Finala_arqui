import socket
from threading import Thread

SOCK_BUFFER = 1024
num_clientes = 0
stock = {"lavadora": 5, "refrigerador": 3, "aspiradora": 2, "licuadora": 4}

#b) Función para manejar la conexión con un cliente

def client_handler(conn, client_address):
    global num_clientes, stock

    print(f"Conexion de {client_address[0]}:{client_address[1]}")
    num_clientes += 1
    print(f"Numero de clientes actualmente conectados: {num_clientes}")

    try:
        while True:
            electrodomestico = conn.recv(SOCK_BUFFER).decode()

            if electrodomestico in stock and stock[electrodomestico] > 0:
                conn.sendall('1'.encode())
                stock[electrodomestico] -= 1
            else:
                conn.sendall('0'.encode())
                break
    except (ConnectionResetError, ConnectionAbortedError):
        print("El cliente cerró la conexión de manera abrupta")
    finally:
        print("cerrando la conexion")
        conn.close()
        num_clientes -= 1

#c) Servidor.py

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5000)

    print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)  # Aumentar el número de conexiones en cola

    while True:
        print("Servidor en espera de conexiones...")
        connection, c_address = sock.accept()
        print(f"Cliente conectado desde {c_address}")

        t = Thread(target=client_handler, args=(connection, c_address))
        t.start()

#d) ¿Es necesario el uso de locks? ¿Por qué?
# Al  ejecutar el hilo de manera concurrente es posible que mas de un cliente acceda 
# a la cantidad de stock, lo que podría llevar a resultados inesperados o corruptos
# si no se gestionan adecuadamente porian darse casos como leer un stock no actualizado 
# o modificar el stock mientras que el anterior hilo esta ejecutando su rutina afectando su resultado.
# El uso de with stock_lock asegura que solo un hilo pueda acceder al diccionario 
# stock a la vez, evitando así que ocurran condiciones de carrera cuando se actualiza
# el stock.