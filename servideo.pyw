import socket
import pyautogui
import cv2
import struct
import pickle
import numpy as np
    



socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = socket.gethostbyname(socket.gethostname())
print('host ip:', host_ip)
port = 9999
direction_socket = (host_ip, port)

def iniciar_escucha():
    socket_servidor.bind(direction_socket)
    socket_servidor.listen(5)
    print("listening at:",direction_socket)

while True:
    try:
        iniciar_escucha()
        socket_cliente,addr = socket_servidor.accept()
        print("got conection from:", addr)

        while True:
            if socket_cliente:
                captura = pyautogui.screenshot()

                arreglo_captura = np.array(captura)
                frame = cv2.cvtColor(arreglo_captura , cv2.COLOR_BGR2RGB)
                
                captura_codificada = pickle.dumps(frame)
                mensaje =struct.pack("Q", len(captura_codificada))+captura_codificada
                socket_cliente.sendall(mensaje) 
    except OSError:
        pass 