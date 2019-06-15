import socket

host = '192.168.43.158'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    message= input()
    s.send(str.encode(message))
    reply = s.recv(1024)
    print("We have received a reply")
    print("Send closing message.")
    s.send(str.encode("EXIT"))
    s.close()
    print(reply.decode('utf-8'))
    break

s.close()

'''
def transmit(message):
    s = setupSocket()
    response = sendReceive(s, message)
    return response
    '''