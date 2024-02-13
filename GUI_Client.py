import socket
import os
import threading
import tkinter
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import customtkinter
from PIL import Image, ImageTk, ImageFilter
from customtkinter import *
import webbrowser
from itertools import count

app = CTk()
app.geometry("1080x720")
app.title("CS File")
app.iconbitmap('materials/Logo.ico')
app.resizable(width=False, height=False)
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

mode = 'dark'
path = 'materials/giphy.gif'
images_list = []
gif_duration = ''
images_counting = -1
cs = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.100.123", 3334))

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

facebook = customtkinter.CTkImage(light_image=Image.open("materials/icons8-facebook-50.png"),
                                             dark_image=Image.open("materials/icons8-facebook-50.png"),
                                             size=(20, 20))

instagram = customtkinter.CTkImage(light_image=Image.open("materials/icons8-instagram-50.png"),
                                              dark_image=Image.open("materials/icons8-instagram-50.png"),
                                              size=(20, 20))
githup = customtkinter.CTkImage(light_image=Image.open("materials/icons8-github-50.png"),
                                dark_image=Image.open("materials/icons8-github-50.png"),
                                size=(20, 20))

sun_moon = customtkinter.CTkImage(light_image=Image.open("materials/icons8-moon-64.png"),
                                  dark_image=Image.open("materials/icons8-sun-64.png"),
                                  size=(20, 20))


def change():
    global mode
    if mode == 'dark':
        customtkinter.set_appearance_mode('light')
        mode = 'light'
    elif mode == 'light':
        customtkinter.set_appearance_mode('dark')
        mode = 'dark'


def main0page():
    main_page = customtkinter.CTkFrame(master=app, width=1080, height=720, fg_color=("#D9D9D9", "#242424"))
    main_page.pack()

    label = CTkLabel(master=main_page, text="Chose your Service", font=("Elephant", 60))
    label.place(relx=0.5, rely=0.2, anchor="center")

    # entry = CTkEntry(master=main_page, placeholder_text="What is your IP...", placeholder_text_color="#ffa500", bg_color=("#E5E5E5", "#202020"))
    # entry.place(relx=0.5, rely=0.35, anchor='center')

    image_path = os.path.join(os.path.dirname(__file__), 'materials/Logo.png')
    image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(100, 100))
    image_label = customtkinter.CTkLabel(master=main_page, image=image, text='', fg_color=("#D9D9D9", "#242424"))
    image_label.place(relx=0.5, rely=0.1, anchor='center')

    Download_image = customtkinter.CTkImage(light_image=Image.open("materials/Download Icon.png"),
                                             dark_image=Image.open("materials/Download Icon.png"),
                                             size=(250, 250))

    btn2 = CTkButton(master=main_page, text="Download", corner_radius=0, border_width=3,
                     border_color=("#D9D9D9", "#242424"), hover_color=("#C5C5C5", "#282828"), text_color=("#242424", "#D9D9D9"), fg_color=("#D9D9D9", "#242424"), font=("Elephant", 40),
                     command=lambda: (entry1(), download()), bg_color=("#D9D9D9", "#242424"), image=Download_image, compound="top", height=80, width=80)
    btn2.place(relx=0.7, rely=0.5, anchor="center")

    Upload_image = customtkinter.CTkImage(light_image=Image.open("materials/Upload Icon.png"),
                                            dark_image=Image.open("materials/Upload Icon.png"),
                                            size=(250, 250))

    btn3 = CTkButton(master=main_page, text="Upload", corner_radius=0, border_width=3,
                     border_color=("#D9D9D9", "#242424"), hover_color=("#C5C5C5", "#282828"), text_color=("#242424", "#D9D9D9"), fg_color=("#D9D9D9", "#242424"), font=("Elephant", 40),
                     command=lambda: (entry1(), upload()), bg_color=("#D9D9D9", "#242424"), image=Upload_image, compound="top")
    btn3.place(relx=0.3, rely=0.5, anchor="center")

    btn14 = CTkButton(master=app, text="Instagram", corner_radius=1, border_width=3,
                      border_color=("#D9D9D9", "#242424"), hover_color=("#D9D9D9", "#242424"),
                      text_color=("#242424", "#E5E5E5"), font=("Elephant", 8), image=instagram,
                      command=lambda: (webbrowser.open_new_tab('https://www.instagram.com/ieee_bau_cs/')),
                      fg_color=("#D9D9D9", "#242424"), bg_color=("#D9D9D9", "#242424"))
    btn14.place(relx=0.76, rely=0.9777, anchor="center")

    btn12 = CTkButton(master=app, text="Facebook", corner_radius=1, border_width=3,
                      border_color=("#D9D9D9", "#242424"), hover_color=("#D9D9D9", "#242424"),
                      text_color=("#242424", "#D9D9D9"), font=("Elephant", 8), image=facebook,
                      command=lambda: (webbrowser.open_new_tab('https://www.facebook.com/IEEEBAUCS')),
                      fg_color=("#D9D9D9", "#242424"), bg_color=("#D9D9D9", "#242424"))
    btn12.place(relx=0.86, rely=0.9777, anchor="center")

    btn13 = CTkButton(master=app, text="Contact us", corner_radius=1, border_width=3,
                      border_color=("#D9D9D9", "#242424"), hover_color=("#D9D9D9", "#242424"),
                      text_color=("#242424", "#D9D9D9"), font=("Elephant", 8), image=githup,
                      command=lambda: (webbrowser.open_new_tab('https://github.com/AyhamAsfoor')),
                      fg_color=("#D9D9D9", "#242424"), bg_color=("#D9D9D9", "#242424"))
    btn13.place(relx=0.9555, rely=0.9777, anchor="center")

    def entry1():
        ip_number = str(ip)
        client.send(f"{ip_number}".encode('utf-8'))

    def upload():
        type_request = int(0)
        client.send(f"{type_request}".encode('utf-8'))

        image_path = os.path.join(os.path.dirname(__file__), 'materials/Logo.png')
        image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(100, 100))
        image_label = customtkinter.CTkLabel(master=app, image=image, text='', fg_color=("#E5E5E5", "#212121"))
        image_label.place(relx=0.5, rely=0.1, anchor='center')

        download_page = customtkinter.CTkFrame(master=main_page, width=1080, height=720)
        download_page.pack()

        label2 = CTkLabel(master=main_page, text="Upload File", font=("Elephant", 60), bg_color=("#E5E5E5", "#212121"))
        label2.place(relx=0.5, rely=0.2, anchor="center")

        entry2 = CTkEntry(master=main_page, placeholder_text="Name", placeholder_text_color="#ffa500", bg_color=("#E5E5E5", "#212121"), width=180, height=40, font=("Elephant", 20))
        entry2.place(relx=0.4, rely=0.68, anchor='center')

        label3 = CTkLabel(master=main_page, text=".", font=("Elephant", 50), bg_color=("#E5E5E5", "#212121"))
        label3.place(relx=0.5, rely=0.68, anchor='center')

        entry3 = CTkEntry(master=main_page, placeholder_text="Extension", placeholder_text_color="#ffa500", bg_color=("#E5E5E5", "#212121"), width=180, height=40, font=("Elephant", 20))
        entry3.place(relx=0.6, rely=0.68, anchor='center')

        # entry4 = CTkEntry(master=main_page, placeholder_text="", placeholder_text_color="#ffa500", bg_color=("#D9D9D9", "#292929"))
        # entry4.place(relx=0.48, rely=0.5)

        Upload_image = customtkinter.CTkImage(light_image=Image.open("materials/File Upload Icon.png"),
                                              dark_image=Image.open("materials/File Upload Icon.png"),
                                              size=(250, 250))

        image_label = customtkinter.CTkLabel(master=app, image=Upload_image, text='', fg_color=("#E5E5E5", "#212121"))
        image_label.place(relx=0.5, rely=0.45, anchor='center')

        btn3 = CTkButton(master=main_page, text="Upload", corner_radius=32, border_width=3, fg_color="#ffa500",
                         border_color="#ffa500", hover_color=("#E5E5E5", "#212121"), text_color=("#212121", "#E5E5E5"), font=("Elephant", 30),
                         command=lambda: (entry_upload(), initiate_gif(), app.after(1000, play_image_for_upload())), bg_color=("#E5E5E5", "#212121"), width=60, height=40)
        btn3.place(relx=0.5, rely=0.78,  anchor='center')

        print("upload")

        Browse_image = customtkinter.CTkImage(light_image=Image.open("materials/Browse Icon.png"),
                                              dark_image=Image.open("materials/Browse Icon.png"),
                                              size=(50, 50))

        btn7 = CTkButton(master=app, image=Browse_image, text="", fg_color=("#E5E5E5", "#212121"), corner_radius=0, border_width=3,
                         border_color=("#E5E5E5", "#212121"), hover_color=("#D5D5D5", "#272727"), text_color=("#212121", "#E5E5E5"),
                         font=("Elephant", 20), command=lambda: (filedialog1(), initiate_gif(), app.after(1000, play_image_for_upload())), bg_color=("#E5E5E5", "#212121"), width=40, height=40)
        btn7.place(relx=0.72, rely=0.68, anchor="center")

        btn9 = CTkButton(master=app, text="Instagram", corner_radius=1, border_width=3,
                         border_color=("#E5E5E5", "#212121"), hover_color=("#E5E5E5", "#212121"),
                         text_color=("#202020", "#E5E5E5"), font=("Elephant", 8), image=instagram, command=lambda: (webbrowser.open_new_tab('https://www.instagram.com/ieee_bau_cs/')),
                         fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#212121"))
        btn9.place(relx=0.76, rely=0.9777, anchor="center")

        btn10 = CTkButton(master=app, text="Facebook", corner_radius=1, border_width=3,
                          border_color=("#E5E5E5", "#212121"), hover_color=("#E5E5E5", "#212121"),
                          text_color=("#202020", "#E5E5E5"), font=("Elephant", 8), image=facebook, command=lambda: (webbrowser.open_new_tab('https://www.facebook.com/IEEEBAUCS')),
                          fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#212121"))
        btn10.place(relx=0.86, rely=0.9777, anchor="center")

        btn11 = CTkButton(master=app, text="Contact us", corner_radius=1, border_width=3,
                          border_color=("#E5E5E5", "#212121"), hover_color=("#E5E5E5", "#212121"),
                          text_color=("#212121", "#D9D9D9"), font=("Elephant", 8), image=githup, command=lambda: (webbrowser.open_new_tab('https://github.com/AyhamAsfoor')),
                          fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#212121"))
        btn11.place(relx=0.9555, rely=0.9777, anchor="center")

        def filedialog1():
            filepath = filedialog.askopenfilename(title='Select file', filetypes=(
             ('Image', '*.png'), ('Text Files', '*.txt'), ('All Files', '*.*')))

            file_name = os.path.basename(filepath)

            file_extension = os.path.splitext(file_name)[1]

            file_extension_without_dot = file_extension[1:]

            file_fill = ''
            for a in file_name:
                if a == '.':
                    break
                file_fill += a

            entry2.configure(placeholder_text=f"{file_fill}")
            entry3.configure(placeholder_text=f"{file_extension_without_dot}")

            # file_name1_with_out_ex = os.path.basename(filepath)

            print("Name File:", file_fill)
            print("Extension:", file_extension_without_dot)

            Name = str(file_fill)
            Extension = str(file_extension_without_dot)
            Name_after = f'{file_fill}_after'

            file = open(f"{Name}.{Extension}", "rb")
            file_size = int(os.path.getsize(f"{Name}.{Extension}"))

            client.send(f"{Name_after}.{Extension}".encode('utf-8'))
            client.send(file_size.to_bytes(8, byteorder='big'))

            data = file.read()
            client.sendall(data + b"<END>")

        def entry_upload():
            Name = str(entry2.get())
            Extension = str(entry3.get())
            Name_after = f'{entry2.get()}_after'

            file = open(f"{Name}.{Extension}", "rb")
            file_size = int(os.path.getsize(f"{Name}.{Extension}"))

            client.send(f"{Name_after}.{Extension}".encode('utf-8'))
            client.send(file_size.to_bytes(8, byteorder='big'))

            data = file.read()
            client.sendall(data + b"<END>")

    def download():
        type_request = int(1)
        client.send(f"{type_request}".encode('utf-8'))
        server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_client.bind(("localhost", 6666))
        server_client.listen()

        client1, addr = server_client.accept()

        upload_page = customtkinter.CTkFrame(master=main_page, width=1080, height=720)
        upload_page.pack()

        image_path = os.path.join(os.path.dirname(__file__), 'materials/Logo.png')
        image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(100, 100))
        image_label = customtkinter.CTkLabel(master=app, image=image, text='', fg_color=("#E5E5E5", "#212121"))
        image_label.place(relx=0.5, rely=0.1, anchor='center')

        download_page = customtkinter.CTkFrame(master=main_page, width=1080, height=720)
        download_page.pack()

        Server_image = customtkinter.CTkImage(light_image=Image.open("materials/File Server Icon.png"),
                                              dark_image=Image.open("materials/File Server Icon.png"),
                                              size=(250, 250))

        image_label = customtkinter.CTkLabel(master=app, image=Server_image, text='', fg_color=("#E5E5E5", "#212121"))
        image_label.place(relx=0.25, rely=0.45, anchor='center')

        Arrows_image = customtkinter.CTkImage(light_image=Image.open("materials/Arrows .png"),
                                              dark_image=Image.open("materials/Arrows .png"),
                                              size=(250, 250))

        image_label = customtkinter.CTkLabel(master=app, image=Arrows_image, text='', fg_color=("#E5E5E5", "#212121"), width=100, height=100)
        image_label.place(relx=0.5, rely=0.45, anchor='center')

        Folder_image = customtkinter.CTkImage(light_image=Image.open("materials/Browse Icon.png"),
                                              dark_image=Image.open("materials/Browse Icon.png"),
                                              size=(250, 250))

        image_label = customtkinter.CTkLabel(master=app, image=Folder_image, text='', fg_color=("#E5E5E5", "#212121"), width=100, height=100)
        image_label.place(relx=0.75, rely=0.45, anchor='center')

        label2 = CTkLabel(master=main_page, text="Download File", font=("Elephant", 60), bg_color=("#E5E5E5", "#212121"), width=100, height=100)
        label2.place(relx=0.5, rely=0.2, anchor="center")

        entry4 = CTkEntry(master=main_page, placeholder_text="File Name", placeholder_text_color="#ffa500", bg_color=("#E5E5E5", "#212121"), font=("Elephant", 20))
        entry4.place(relx=0.15, rely=0.7, anchor="center")

        entry5 = CTkEntry(master=main_page, placeholder_text="Extension", placeholder_text_color="#ffa500", bg_color=("#E5E5E5", "#212121"), font=("Elephant", 20))
        entry5.place(relx=0.3, rely=0.7, anchor="center")

        entry6 = CTkEntry(master=main_page, placeholder_text="New File Name", placeholder_text_color="#ffa500", bg_color=("#E5E5E5", "#212121"), font=("Elephant", 20), width=180)
        entry6.place(relx=0.75, rely=0.7, anchor="center")

        btn3 = CTkButton(master=main_page, text="Download", corner_radius=32, border_width=3, fg_color="#ffa500",
                         border_color="#ffa500", hover_color=("#E5E5E5", "#212121"), text_color=("#212121", "#E5E5E5"), font=("Elephant", 30),
                         command=lambda: (entry_download(), initiate_gif(), app.after(1000, play_image_for_download())), bg_color=("#E5E5E5", "#212121"), width=60, height=40)
        btn3.place(relx=0.5, rely=0.8, anchor="center")

#        btn8 = CTkButton(master=app, text="Browse", fg_color="#ffa500", corner_radius=32, border_width=3,
#                         border_color="#ffa500", hover_color=("#E5E5E5", "#292929"), text_color=("#242424", "#E5E5E5"),
#                         font=("Ariel", 20), command=lambda: (filedialog1()), bg_color=("#E5E5E5", "#292929"))
#        btn8.place(relx=0.45, rely=0.65)

        btn15 = CTkButton(master=app, text="Instagram", corner_radius=1, border_width=3,
                          border_color=("#E5E5E5", "#212121"), hover_color=("#E5E5E5", "#212121"),
                          text_color=("#212121", "#E5E5E5"), font=("Elephant", 8), image=instagram,
                          command=lambda: (webbrowser.open_new_tab('https://www.instagram.com/ieee_bau_cs/')),
                          fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#212121"))
        btn15.place(relx=0.76, rely=0.9777, anchor="center")

        btn16 = CTkButton(master=app, text="Facebook", corner_radius=1, border_width=3,
                          border_color=("#E5E5E5", "#212121"), hover_color=("#E5E5E5", "#212121"),
                          text_color=("#212121", "#E5E5E5"), font=("Elephant", 8), image=facebook,
                          command=lambda: (webbrowser.open_new_tab('https://www.facebook.com/IEEEBAUCS')),
                          fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#292929"))
        btn16.place(relx=0.86, rely=0.9777, anchor="center")

        btn17 = CTkButton(master=app, text="Contact us", corner_radius=1, border_width=3,
                          border_color=("#E5E5E5", "#212121"), hover_color=("#E5E5E5", "#212121"),
                          text_color=("#212121", "#E5E5E5"), font=("Elephant", 8), image=githup,
                          command=lambda: (webbrowser.open_new_tab('https://github.com/AyhamAsfoor')),
                          fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#212121"))
        btn17.place(relx=0.9555, rely=0.9777, anchor="center")

        print("download")

        def entry_download():
            Name = str(entry4.get())
            Extension = str(entry5.get())
            Name_after = str(entry6.get())
            client.send(f"{Name}.{Extension}".encode('utf-8'))
            f_name = client1.recv(1024)
            print(f"The File name: {f_name.decode('utf-8')}")

            file1 = open(Name_after + '.' + Extension, "wb")
            file_bytz = b""

            done = False

            while not done:
                data = client1.recv(1024)
                if file_bytz[-5:] == b"<END>":
                    done = True
                else:
                    file_bytz += data

            file1.write(file_bytz)
            file1.close()

    def initiate_gif():
        global gif_duration, path
        if mode == 'dark':
            path = "materials/giphy.gif"

        try:
            image = Image.open(path)

            for i in range(1, 75):

                if i == 73:
                    i = 0
                try:
                    images_list.append(ImageTk.PhotoImage(image.copy()))
                    image.seek(i)

                except Exception as error:
                    print(f"Error extracting frame {i}: {error}")
                    break
            gif_duration = int(image.info['duration'])

        except Exception as error:
            print(f"Error opening GIF file: {error}")

    def play_image_for_upload():
        global images_counting, cs
        images_counting += 1

        if images_counting < len(images_list):
            label5 = CTkLabel(master=main_page, text="")
            label5.configure(image=images_list[images_counting], fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#212121"))
            label5.place(relx=0.5, rely=0.8, anchor="center")
            qq = customtkinter.CTkLabel(master=app, text='              ',
                                        font=("Elephant", 20), fg_color=("#E5E5E5", "#212121"),
                                        bg_color=("#E5E5E5", "#212121"), height=80)
            qq.place(relx=0.72, rely=0.68, anchor='center')
            app.after(gif_duration, play_image_for_upload)
        else:
            cs += 1
            print(cs)
            if cs != 2:
                images_counting = 0
                app.after(gif_duration, play_image_for_upload)
            else:
                final_label = customtkinter.CTkLabel(master=main_page, text='We\'re done. You can close the window.',
                                                     font=("Elephant", 20), fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#212121"))
                final_label.place(relx=0.5, rely=0.8, anchor='center')

    def play_image_for_download():
        global images_counting, cs
        images_counting += 1

        if images_counting < len(images_list):
            label5 = CTkLabel(master=main_page, text="")
            label5.configure(image=images_list[images_counting], fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#212121"))
            label5.place(relx=0.5, rely=0.8, anchor="center")
            qq = customtkinter.CTkLabel(master=app, text='                                   ',
                                        font=("Elephant", 20), fg_color=("#E5E5E5", "#212121"),
                                        bg_color=("#E5E5E5", "#212121"), width=80, height=60)
            qq.place(relx=0.78, rely=0.69, anchor='center')
            qq1 = customtkinter.CTkLabel(master=app, text='                                   ',
                                         font=("Elephant", 20), fg_color=("#E5E5E5", "#212121"),
                                         bg_color=("#E5E5E5", "#212121"), width=280, height=60)
            qq1.place(relx=0.2, rely=0.69, anchor='center')
            app.after(gif_duration, play_image_for_download)
        else:
            cs += 1
            print(cs)
            if cs != 2:
                images_counting = 0
                app.after(gif_duration, play_image_for_download())
            else:
                final_label = customtkinter.CTkLabel(master=main_page, text='We\'re done. You can close the window.',
                                                     font=("Elephant", 20), fg_color=("#E5E5E5", "#212121"), bg_color=("#E5E5E5", "#212121"))
                final_label.place(relx=0.5, rely=0.8, anchor='center')


# image_path_bg = PhotoImage(file='background.png')
# image_bg = tkinter.Label(app, image=image_path_bg)
# image_bg.place(relx=0.5, rely=0.5, anchor='center')

# image_path = os.path.join(os.path.dirname(__file__), 'Background.png')
# image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(1080, 720))
# image_label = customtkinter.CTkLabel(app, image=image, text='')
# image_label.place(relx=0.5, rely=0.5, anchor='center')

my_image = customtkinter.CTkImage(light_image=Image.open("materials/Background1.png"),
                                  dark_image=Image.open("materials/Background.png"),
                                  size=(1080, 720))
image_label = customtkinter.CTkLabel(app, image=my_image, text="", fg_color=("#D9D9D9", "#242424"))
image_label.place(relx=0.5, rely=0.5, anchor='center')

image_path = os.path.join(os.path.dirname(__file__), 'materials/Logo With Name.png')
image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(400, 400))
image_label = customtkinter.CTkLabel(master=app, image=image, text='', fg_color=("#D9D9D9", "#242424"))
image_label.place(relx=0.5, rely=0.3, anchor='center')

label = CTkLabel(master=app, text="Welcome TO CS File", font=("Elephant", 40), fg_color=("#D9D9D9", "#242424"))
label.place(relx=0.5, rely=0.55, anchor="center")

btn1 = CTkButton(master=app, text="NEXT", width=200, height=60, fg_color="transparent", corner_radius=32, border_width=3, border_color="#ffa500", hover_color="#ffa500", text_color=("#242424", "#D9D9D9"), font=("Elephant", 40), command=lambda: (main0page()), bg_color=("#D9D9D9", "#242424"))
btn1.place(relx=0.5, rely=0.7, anchor="center")

btn6 = CTkButton(master=app, image=sun_moon, text="Change Mode", corner_radius=1, border_width=3, border_color=("#D9D9D9", "#242424"), hover_color=("#D9D9D9", "#242424"), text_color=("#242424", "#D9D9D9"), font=("Elephant", 10), command=lambda: (change()), fg_color=("#D9D9D9", "#242424"), bg_color=("#D9D9D9", "#242424"), compound="left")
btn6.place(relx=0.9255, rely=0.9777, anchor="center")


app.mainloop()
