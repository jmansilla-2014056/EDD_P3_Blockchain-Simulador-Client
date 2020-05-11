import socket
import select
import sys
import threading
from tkinter import messagebox
from Controlador import Bulk

import socket
import threading
import sys
import msvcrt
import pickle


class Client:

    def __init__(self):
        self.josnTxt = ""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        IP_address = "192.168.0.8"
        Port = 8080
        self.sock.connect((IP_address, Port))

        msg_recv = threading.Thread(target=self.msg_recv)
        msg_recv.daemon = True
        msg_recv.start()

    def msg_recv(self):
            while True:
                try:
                    messagebox.showinfo("Nuevo mensaje:", "x")
                    if self.sock is not None:
                        data = self.sock.recv(2048)
                        data = data.decode('utf-8')
                        if data:
                            messagebox.showinfo("Recivido:", str(data))
                            if str(data) == "true":
                                Bulk.saveJson(str(self.jsonTxt))
                            elif str(data) == "false":
                                print()
                            else:
                                if data == "Welcome to [EDD]Blockchain Project!":
                                    print()
                                else:
                                    self.jsonTxt = str(data)
                                    boolean = Bulk.validateJson(str(self.jsonTxt))
                                    self.sock.sendall(boolean.encode('utf-8'))


                except:
                    pass

    def send_msg(self, msg):
        self.sock.sendall(msg.encode('utf-8'))
    