import os
import socket
import tqdm
import tkinter as tk
from tkinter import ttk
import threading
import customtkinter as ctk
import time


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.global_log = ''
        self.start_time = None
        self.number_connection = 0
        self.all_connection = 0
        self.Start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.geometry("1080x720")
        self.title("CS File Server")
        self.iconbitmap('materials/Logo.ico')
        self.resizable(width=False, height=False)
        self.status_label1 = ctk.CTkLabel(self, text="< CS Server >", font=("times new roman", 50))
        self.status_label1.pack(pady=5)

        self.status_label = ctk.CTkLabel(self, text="Server is not Running", font=("times new roman", 20), text_color="#ffb600")
        self.status_label.place(relx=0.04, rely=0.07)

        self.log_text = ctk.CTkTextbox(self, wrap=tk.WORD, height=360, width=1060, corner_radius=32, border_width=3, border_spacing=1,
                                       border_color='#888888', scrollbar_button_color="#ffa500", activate_scrollbars=True,
                                       state='normal', font=("times new roman", 25))
        self.log_text.place(relx=0.008, rely=0.12)

        self.start_server_button = ctk.CTkButton(self, text="Start Server", command=self.start_server,
                                                 corner_radius=32, border_width=3, border_color="#ffa500", hover_color="#ffa500",
                                                 fg_color="transparent", font=("Ariel", 20), bg_color="#242424")
        self.start_server_button.place(relx=0.5, rely=0.68, anchor='center')

        self.log_button = ctk.CTkButton(self, text="Save Log File", command=self.log_file,
                                        corner_radius=0, border_width=3, border_color="#242424",
                                        hover_color="#242424",
                                        fg_color="#242424", font=("times new roman", 20), bg_color="#242424", text_color='#ffa500')
        self.log_button.place(relx=0.1, rely=0.65, anchor='center')

        self.time_label = ctk.CTkLabel(self, text="Elapsed Time: 00:00:00", font=("times new roman", 20),
                                       text_color="#ffb600")
        self.time_label.place(relx=0.8, rely=0.07)

        self.connection_label = ctk.CTkLabel(self, text=f"Number Connection: {self.number_connection}", font=("times new roman", 20),
                                             text_color="#ffb600")
        self.connection_label.place(relx=0.8, rely=0.63)

    def add_log(self, log):
        name = str(f"(CS/Server)-[~] ")
        self.log_text.insert(tk.END, name + str(log) + "\n")
        self.log_text.see(tk.END)
        self.global_log = self.global_log + name + str(log) + '\n'

    def update_log(self, log):
        self.after(0, self.add_log, log)

    def start_server(self):
        self.start_time = time.time()
        self.status_label.configure(text="Server is running...")
        self.update_elapsed_time()
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

    def run_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", 3333))
        server.listen()

        self.add_log("is listening")

        while True:
            client, addr = server.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client, addr))
            client_handler.start()

    def handle_client(self, client, addr):
        self.number_connection += 1
        self.all_connection += 1
        self.connection_label.configure(text=f"Number Connection: {self.number_connection}")
        self.update_log(f"Connection from {addr}")

        ip_number = str(client.recv(1024).decode('utf-8'))
        self.update_log(ip_number)

        type_request = client.recv(1024).decode('utf-8')
        self.update_log(f"Type request: {type_request}")

        print(f"before if type request:{type_request}")
        if int(type_request) == 0:
            print("after if")
            file_name = client.recv(1024).decode('utf-8')
            self.update_log(f"The Name of the file: {file_name}")
            file_size_bytes = client.recv(8)
            file_size = int.from_bytes(file_size_bytes, byteorder='big')
            self.update_log(f"The Size of the file: {file_size} bytes")

            file = open(file_name, "wb")
            file_bytz = b""

            done = False

            progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

            while not done:
                data = client.recv(1024)
                if file_bytz[-5:] == b"<END>":
                    done = True
                else:
                    file_bytz += data
                progress.update()

            file.write(file_bytz)
            file.close()
        elif int(type_request) == 1:
            self.update_log(addr)
            client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client1.connect(("localhost", 6666))

            file_name = client.recv(1024).decode('utf-8')
            self.update_log(f"The Name of the file: {file_name}")

            client1.send(f"{file_name}".encode('utf-8'))
            file = open(f"{file_name}", "rb")

            data = file.read()
            client1.sendall(data + b"<END>")

        client.close()
        self.number_connection -= 1
        self.connection_label.configure(text=f"Number Connection: {self.number_connection}")
        self.update_log("---------------------------------------")
        self.update_log("The operation is over bye. ")
        self.update_log(f"Connection from {addr} closed.")
        self.update_log("---------------------------------------")

    def get_elapsed_time(self):
        elapsed_time = time.time() - self.start_time
        return time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    def update_elapsed_time(self):
        elapsed_time = self.get_elapsed_time()
        self.time_label.configure(text=f"Elapsed Time: {elapsed_time}")
        self.after(1000, self.update_elapsed_time)

    def log_file(self):
        current_time = time.strftime("LOG File %Y-%m-%d %H;%M;%S")
        File = open(f'{current_time}.txt', 'w')
        self.global_log = self.global_log + f'Start Time:{self.Start_time}' + '\t' \
                         + f'Final Time:{time.strftime("%Y-%m-%d %H:%M:%S")}' + '\t' \
                         + f'Elapsed Time: {self.get_elapsed_time()}' + '\t' + f'Number Connections:{self.all_connection}'
        File.write(f'{self.global_log}')
        File.close()
        self.global_log = ''


if __name__ == "__main__":
    app = App()
    app.mainloop()
