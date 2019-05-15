import socket

size=1024
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('',8080))

data,addr=server_socket.recvfrom(size)
print("file recv start from : ",addr[0])
print(data)
print("File Name : ",data.decode())
total_size, _ = server_socket.recvfrom(size)
total_size = int(total_size)
print("File Size : %d"%total_size)

current_size=0
receive_byte=bytes()
receive_file = open('receive.jpg', 'wb')
data, addr = server_socket.recvfrom(size)

while data:
    current_size+=len(data)
    receive_byte+=data
    rate = (current_size / total_size)*100
    print("current_size / total_size = %d/%d  %f %%" % (current_size, total_size, rate))

    if rate>=100:
        break

    data, addr = server_socket.recvfrom(size)

receive_file.write(receive_byte)
receive_file.close()

