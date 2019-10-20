import socket
import select
import sys
import threading
from tkinter import messagebox
from Controlador import Bulk

import socket
import threading
import sys
import pickle

class Client:

    def __init__(self):
        self.jsonTxt = ""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        IP_address = "192.168.0.9"
        Port = 8080
        self.sock.connect((IP_address, Port))

        msg_recv = threading.Thread(target=self.msg_recv)

        msg_recv.daemon = True
        msg_recv.start()

    def msg_recv(self):
        while True:
            try:
                print("x")
                data = self.sock.recv(1024)
                data = data.decode('utf-8')
                if data:
                    messagebox.showinfo("Enviado:", str(data))
                    if str(data) == "true":
                        Bulk.saveJson(self.jsonTxt)
                    elif str(data) == "false":
                        print()
                    else:
                        self.jsonTxt = str(data)
                        boolean = str(Bulk.validateJson(self.jsonTxt))
                        self.sock.sendall(boolean.encode('utf-8'))
                    print(str(data))
            except:
                pass

    def send_msg(self, msg):
        self.sock.sendall(msg.encode('utf-8'))


