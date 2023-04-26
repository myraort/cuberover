import socket
import time
import picamera
import os

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()

ip = os.environ.get('IP')

connected = False
while not connected:
    try:
        client_socket.connect((ip, 8000))
        connected = True
    except:
        time.sleep(10)
        continue

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')
try:
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 24
    camera.start_preview()
    time.sleep(2)
    camera.start_recording(connection, format='rgb')
    while 1:
        continue
finally:
    camera.stop_recording()
    connection.close()
    client_socket.close()
