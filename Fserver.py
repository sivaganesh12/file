import socket                   # Import socket module
import time
port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = '192.168.43.77'    # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='siva1.jpg'
    conn.send(filename.encode("ascii"))
    time.sleep(2)         
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       #print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting'.encode("ascii"))
    
    conn.close()
