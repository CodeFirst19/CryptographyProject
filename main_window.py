import os
from tkinter import *
from tkinter import ttk as tk
import file_window
from file_window import encrypt_file, decrypt_file
from text_window import encrypt_text, decrypt_text


# ---Functions---
def construct_frame3(text=''):
    # ---Frame Three---
    frame3 = Frame(application)
    Label(frame3, text=text).grid(row=0, column=0, pady=10, sticky=W)
    global cmbx_type
    cmbx_type = StringVar()
    cmbx_text = tk.Combobox(frame3, textvariable=cmbx_type, width=60, state='readonly')
    cmbx_text['values'] = ('--File', '--Text')
    cmbx_text.grid(row=1, column=0, padx=5, sticky=W)
    frame3.grid(row=2, column=0, padx=15, sticky=W)

    # Function Scope Proceed Button
    btn_proceed = Button(application, text='Proceed', width=8, command=proceed)
    btn_proceed.grid(row=3, column=0, padx=15, pady=15, sticky=E)


def go_to_next():
    if cmbx_usage.get() == '--Encryption':
        text = 'Select What You Want To Encrypt:'
        construct_frame3(text)
        # btn_next['state'] = 'disabled'
    elif cmbx_usage.get() == '--Decryption':
        text = 'Select What You Want To Decrypt:'
        # btn_next['state'] = 'disabled'
        construct_frame3(text)
    else:
        return


def proceed():
    usage = cmbx_usage.get()
    if usage == '--Encryption':
        text = cmbx_type.get()
        if text == '--File':
            encrypt_file()
        elif text == '--Text':
            encrypt_text()
        else:
            return

    if usage == '--Decryption':
        text = cmbx_type.get()
        if text == '--File':
            decrypt_file()
        elif text == '--Text':
            decrypt_text()
        else:
            return


def restart():
    application_restart = sys.executable
    os.execl(application_restart, application_restart, *sys.argv)


# ---GUI Definition---
application = Tk()
application.title('Hashing Algorithms')
application.geometry('425x270')
application.resizable(False, False)

# ---File Menu---
menus = Menu(application)
application.config(menu=menus)
file_menus = Menu(menus)
menus.add_cascade(label='_File', menu=file_menus)
file_menus.add_command(label='Restart', command=restart)
file_menus.add_command(label='Exit', command=application.quit)

# ---Frame One---
frame1 = Frame(application)
Label(frame1, text='What Do You Want To Do?').grid(row=0, column=0, padx=15, pady=10, sticky=W)
cmbx_usage = StringVar()
cmbx_method = tk.Combobox(frame1, textvariable=cmbx_usage, width=60, state='readonly')
cmbx_method['values'] = ('--Select--', '--Encryption', '--Decryption')
cmbx_method.grid(row=1, column=0, padx=18, sticky=W)
cmbx_method.current(0)
frame1.grid(row=0, column=0, sticky=N)

# ---Frame Two---
# frame2 = LabelFrame(application, text='Choose An Algorithm Below:', padx=15, pady=15)
# radbxVar = IntVar()
# radbx1 = tk.Radiobutton(frame2, text='Vernam Cipher', variable=radbxVar, value=1)
# radbx1.grid(row=1, column=0, padx=0, sticky=W)
# radbx2 = tk.Radiobutton(frame2, text='Vigenère Cipher', variable=radbxVar, value=2)
# radbx2.grid(row=2, column=0, padx=0, sticky=W)
# radbx3 = tk.Radiobutton(frame2, text='Transposition', variable=radbxVar, value=3)
# radbx3.grid(row=3, column=0, padx=0, sticky=W)
# radbx4 = tk.Radiobutton(frame2, text='Caesar Cipher', variable=radbxVar, value=4)
# radbx4.grid(row=4, column=0, padx=0, sticky=W)
# frame2.grid(row=1, column=0, padx=15, pady=15, sticky=W)
# ---Button Next Outside Frame Two---
btn_next = Button(application, text='Next', width=8, command=go_to_next)
btn_next.grid(row=1, column=0, padx=15, pady=16, sticky=SE)

application.mainloop()
