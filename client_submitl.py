import socket
FLAGS=None
import os

class ClientSocket():

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


    def socket_send(self):

        ip_addr='10.3.225.244'
        port=8080

        self.socket.connect((ip_addr, int(port)))

        filename=input('Input your file name: ')
        print("File Transmit Start...")

        total_size=os.path.getsize(filename)

        self.socket.sendto(filename.encode(), (ip_addr, int(port)))
        self.socket.sendto(str(total_size).encode(), (ip_addr, int(port)))

        file = open(filename,'rb')

        sending_data = file.read(1024)
        current_size=0
        while sending_data:

            self.socket.sendto(sending_data, (ip_addr, int(port)))
            current_size +=len( sending_data)
            rate = (current_size / total_size)*100
            print("current_size / total_size = %d/%d %f%%" % (current_size, total_size, rate))
            if rate>=100:
                break

            sending_data = file.read(1024)

        print("ok")
        print("file_send_end")

        file.close()


    def main(self):
        self.socket_send()

if __name__ == '__main__':
    import argparse

    parser=argparse.ArgumentParser()
    parser.add_argument('-i','--ip',type=str,default='localhost')
    parser.add_argument('-p', '--port', type=int, default=8080)

    FLAGS,_=parser.parse_known_args()

    client_socket=ClientSocket()
    client_socket.main()