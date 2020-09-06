from tkinter import *
from tkinter import ttk as tk
from tkinter import filedialog
from tkinter import messagebox
import random
from string import ascii_letters
from textwrap import wrap
from key_window import send_key


#  GUI Definition Functions
def init_win():
    # ---GUI Definition---
    file_win = Tk()
    file_win.title('File Encryption')
    file_win.geometry('550x360')
    file_win.resizable(False, False)
    return file_win


# Open File Dialog
def encrypt_open_file():
    try:
        root = Tk()
        root.title('Directory Configuration')
        global filename
        filename = filedialog.askopenfilename(initialdir='/', title='Choose File', filetypes=(('Text Files', '*.txt'),))
        root.destroy()
        with open(filename, 'r') as file:
            for line in file:
                text_in_file_encrypt.insert(END, line)
        text_in_file_encrypt['state'] = 'disabled'
        btn_encrypt['state'] = 'normal'
    except:
        messagebox.showerror('Error',
                             'Unexpected Error occurred.\nPlease Make Sure You Use This Application Accordingly.')


# Function For Encryption
def encrypt_text_in_file():
    try:
        value = comboBox_encrypt.get()
        # Vernam Cipher Encryption
        if value == '--Vernam cipher':
            msgbx_results = messagebox.askyesno('File Encryption',
                                                'The File Will Be Encrypted!\nDo You Want To Continue?')
            file_text = text_in_file_encrypt.get('1.0', END)

            if msgbx_results == 1:
                # Convert File Content To Binary
                user_input = file_text
                user_binary = [bin(ord(letter))[2:].ljust(15, '0') for letter in user_input]
                global random_key
                random_key = ''.join(random.choice(ascii_letters) for letter in range(len(user_input)))
                global key_binary
                key_binary = [bin(ord(letter))[2:].ljust(15, '0') for letter in random_key]

                # Generating Cipher Binary From User File Content And The Random Key.
                cipher_binary = ''
                for i in range(len(user_binary)):
                    user_binary_item = user_binary[i]
                    global key_binary_item
                    key_binary_item = key_binary[i]
                    for j in range(len(user_binary_item)):
                        if user_binary_item[j:7] == key_binary_item[j:7]:
                            cipher_binary += '0'
                        else:
                            cipher_binary += '1'

                # Perform Encryption
                global cipher_binary_split
                cipher_binary_split = wrap(cipher_binary, 7)
                ciphertext = ''
                for i in range(len(cipher_binary_split)):
                    cipher_binary_split_item = cipher_binary_split[i]
                    ciphertext += chr(int(cipher_binary_split_item, 2))

                # Inserting Ciphertext In The Text Area
                text_in_file_encrypt['state'] = 'normal'
                text_in_file_encrypt.delete('1.0', END)
                text_in_file_encrypt.insert(END, ciphertext)
                text_in_file_encrypt['state'] = 'disabled'
                btn_encrypt['state'] = 'disabled'

                # Changing File Content With Vernam Cipher
                with open(filename, 'w', encoding='utf-8', errors='ignore') as file:
                    for line in text_in_file_encrypt.get('1.0', END):
                        file.write(line)

                messagebox.showinfo('Information', 'The File has been Encrypted.')
                send_key(random_key)
            else:
                return

        elif value == '--Vigenere cipher':
            msgbx_results = messagebox.askyesno('File Encryption',
                                                'The File Will Be Encrypted!\nDo You Want To Continue?')
            file_text = text_in_file_encrypt.get('1.0', END)
            if msgbx_results == 1:
                alphabets = 'abcdefghijklmnopqrstuvwxyz'
                key_to_int = entry_encrypt.get()
                if key_to_int != '':
                    key_to_int = entry_encrypt.get().split(',')
                    for i in range(len(key_to_int)):
                        key_to_int[i] = int(key_to_int[i])

                    key = key_to_int
                    cipher = ''

                    letter = []
                    list_key = []

                    for i in range(len(file_text)):
                        letter += [alphabets.find(file_text[i])]
                        while len(list_key) < len(alphabets):
                            list_key += [key[j] for j in range(len(key))]

                        letter[i] = (letter[i] + list_key[i]) % 26
                        cipher += alphabets[letter[i]]

                    text_in_file_encrypt['state'] = 'normal'
                    text_in_file_encrypt.delete('1.0', END)
                    text_in_file_encrypt.insert(END, cipher)
                    text_in_file_encrypt['state'] = 'disabled'
                    btn_encrypt['state'] = 'disabled'

                    with open(filename, 'w') as file:
                        for line in text_in_file_encrypt.get('1.0', END):
                            file.write(line)

                    messagebox.showinfo('Information', 'The File has been Encrypted.')
                else:
                    messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')

            else:
                return

        elif value == '--Transposition cipher':
            msgbx_results = messagebox.askyesno('File Encryption',
                                                'The File Will Be Encrypted!\nDo You Want To Continue?')
            file_text = text_in_file_encrypt.get('1.0', END)
            if msgbx_results == 1:
                user_key = entry_encrypt.get()
                if user_key != '':
                    user_key = int(entry_encrypt.get())
                    cipher = [''] * user_key

                    for table_col in range(user_key):
                        cursor = table_col

                        while cursor < len(file_text):
                            cipher[table_col] += file_text[cursor]
                            cursor += user_key

                    text_in_file_encrypt['state'] = 'normal'
                    text_in_file_encrypt.delete('1.0', END)
                    text_in_file_encrypt.insert(END, ''.join(cipher))
                    text_in_file_encrypt['state'] = 'disabled'
                    btn_encrypt['state'] = 'disabled'

                    with open(filename, 'w') as file:
                        for line in text_in_file_encrypt.get('1.0', END):
                            file.write(line)
                    messagebox.showinfo('Information', 'The File has been Encrypted.')
                else:
                    messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')
            else:
                return

        elif value == '--Caesar cipher':
            msgbx_results = messagebox.askyesno('File Encryption',
                                                'The File Will Be Encrypted!\nDo You Want To Continue?')
            if msgbx_results == 1:
                file_text = text_in_file_encrypt.get('1.0', END)
                alphabets = 'abcdefghijklmnopqrstuvwxyz'
                key = entry_encrypt.get()
                if key != '':
                    file_content = file_text
                    file_content = file_content.lower()
                    key = int(entry_encrypt.get())
                    cipher = ''

                    for i in range(len(file_content)):
                        letter = file_content[i]
                        if letter == ' ':
                            cipher += ' '
                        else:
                            letter_position = alphabets.find(letter)
                            new_letter_position = (letter_position + key) % 26
                            cipher += alphabets[new_letter_position]

                    # Changing File Content With Caesar Cipher
                    text_in_file_encrypt['state'] = 'normal'
                    text_in_file_encrypt.delete('1.0', END)
                    text_in_file_encrypt.insert(END, cipher)
                    text_in_file_encrypt['state'] = 'disabled'
                    btn_encrypt['state'] = 'disabled'

                    with open(filename, 'w') as file:
                        for line in text_in_file_encrypt.get('1.0', END):
                            file.write(line)

                    messagebox.showinfo('Information', 'The File has been Encrypted.')
                else:
                    messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')
            else:
                return
        else:
            messagebox.showerror('Error', 'Please Select The Encryption Method.')
    except:
        messagebox.showerror('Error',
                             'Unexpected Error occurred.\nPlease Make Sure You Use This Application Accordingly.')


# Encryption Window Function
def encrypt_file():
    file_win = init_win()
    # File Menu
    menus = Menu(file_win)
    file_win.config(menu=menus)
    file_menus = Menu(menus)
    menus.add_cascade(label='_File', menu=file_menus)
    file_menus.add_command(label='Open', command=encrypt_open_file)
    file_menus.add_command(label='Exit', command=file_win.quit)

    # ---File Window Frame One---
    global comboBox_encrypt
    comboBox_encrypt = tk.Combobox(file_win, width=82, state='readonly')
    comboBox_encrypt['values'] = (
        '--Select cipher method--', '--Vernam cipher', '--Vigenere cipher', '--Transposition cipher', '--Caesar '
                                                                                                      'cipher')
    comboBox_encrypt.current(0)
    comboBox_encrypt.grid(row=0, column=0, pady=10)
    # Key Entry With Label
    Label(file_win, text='Enter Encryption Key:').grid(row=1, column=0, sticky=W, padx=13)
    global entry_encrypt
    entry_encrypt = Entry(file_win, width=65)
    entry_encrypt.grid(row=1, column=0, pady=8, padx=15, sticky=E)
    # ---Text Area And Scrollbar---
    text_frame = Frame(file_win)
    scrollBar = Scrollbar(file_win)
    global text_in_file_encrypt
    text_in_file_encrypt = Text(file_win, width=64, height=14)
    scrollBar.grid(row=2, column=0, pady=15, sticky='NSE')
    text_in_file_encrypt.grid(row=2, column=0, padx=15, pady=10)
    scrollBar.config(command=text_in_file_encrypt.yview)
    text_in_file_encrypt.config(yscrollcommand=scrollBar.set)
    # ---Button Encrypt---
    global btn_encrypt
    btn_encrypt = Button(file_win, text='Encrypt File', width=12, state='disabled', command=encrypt_text_in_file)
    btn_encrypt.grid(row=3, column=0, padx=15, sticky=E)
    text_frame.grid(row=0, column=0)
    file_win.mainloop()


# Open File Dialog
def decrypt_open_file():
    try:
        root = Tk()
        root.title('Directory Configuration')
        global filename
        filename = filedialog.askopenfilename(initialdir='/', title='Choose File',
                                              filetypes=(('Text Files', '*.txt'),))
        root.destroy()
        with open(filename, 'r') as file:
            for line in file:
                text_in_file_decrypt.insert(END, line)
        text_in_file_decrypt['state'] = 'disabled'
        btn_decrypt['state'] = 'normal'
    except:
        messagebox.showerror('Error',
                             'Unexpected Error Occurred.\nPlease Make Sure You Use This Application Accordingly.')


# Function For Decryption
def decrypt_text_in_file():
    try:
        value = comboBox_decrypt.get()
        if value == '--Vernam cipher':
            user_key = entry_decrypt.get()
            auto_key = random_key
            if user_key != '':
                if auto_key == user_key:
                    plaintext_binary = ''
                    print("key", key_binary)
                    print('cipher', cipher_binary_split)
                    for i in range(len(key_binary)):
                        key_binary_item = key_binary[i]
                        cipher_binary_split_item = cipher_binary_split[i]
                        for j in range(len(key_binary_item)):
                            if key_binary_item[j:7] == cipher_binary_split_item[j:7]:
                                plaintext_binary += '0'
                            else:
                                plaintext_binary += '1'

                    plaintext_binary_split = wrap(plaintext_binary, 7)
                    print(plaintext_binary_split)

                    plaintext = ''
                    plaintext_plus = ''
                    for i in range(len(plaintext_binary_split)):
                        plaintext_binary_split_item = plaintext_binary_split[i]
                        plaintext += chr(int(plaintext_binary_split_item, 2))

                    # Inserting Plaintext
                    text_in_file_decrypt['state'] = 'normal'
                    text_in_file_decrypt.delete('1.0', END)
                    text_in_file_decrypt.insert(END, plaintext)
                    btn_decrypt['state'] = 'disabled'

                    with open(filename, 'w') as file:
                        for line in text_in_file_decrypt.get('1.0', END):
                            file.write(line)

                    messagebox.showinfo('Information', 'The File has been Decrypted.')
                else:
                    messagebox.showerror('Incorrect Key', 'The Key Is Incorrect.\nPlease Enter The Correct Key.')
            else:
                messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')

        elif value == '--Vigenere cipher':
            file_text = text_in_file_decrypt.get('1.0', END)
            alphabets = 'abcdefghijklmnopqrstuvwxyz'
            key_to_int = entry_decrypt.get()
            if key_to_int != '':
                key_to_int = entry_decrypt.get().split(',')
                for i in range(len(key_to_int)):
                    key_to_int[i] = int(key_to_int[i])

                key = key_to_int
                cipher = ''
                letter = []
                list_key = []

                for i in range(len(file_text)):
                    letter += [alphabets.find(file_text[i])]
                    while len(list_key) < len(alphabets):
                        list_key += [key[j] for j in range(len(key))]

                    letter[i] = (letter[i] - list_key[i]) % 26
                    cipher += alphabets[letter[i]]

                text_in_file_decrypt['state'] = 'normal'
                text_in_file_decrypt.delete('1.0', END)
                text_in_file_decrypt.insert(END, cipher)
                text_in_file_decrypt['state'] = 'disabled'
                btn_decrypt['state'] = 'disabled'

                with open(filename, 'w') as file:
                    for line in text_in_file_decrypt.get('1.0', END):
                        file.write(line)

                messagebox.showinfo('Information', 'The File has been Decrypted.')
            else:
                messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')

        elif value == '--Transposition cipher':
            from math import ceil
            file_text = text_in_file_decrypt.get('1.0', END)
            key = entry_decrypt.get()
            if key != '':
                file_content = file_text
                file_content = file_content.lower()
                user_key = int(entry_decrypt.get())

                text_length = len(file_content)
                current_column = 0
                current_row = 0
                num_of_rows = ceil(text_length / user_key)
                table_content = (num_of_rows * user_key) - text_length
                plaintext = [''] * num_of_rows

                for table_col in file_content:
                    plaintext[current_column] += table_col
                    current_column += 1
                    if (current_column == num_of_rows) \
                            or (current_column == num_of_rows - 1 and current_row >= user_key - table_content):
                        current_column = 0
                        current_row += 1

                text_in_file_decrypt['state'] = 'normal'
                text_in_file_decrypt.delete('1.0', END)
                text_in_file_decrypt.insert(END, plaintext)
                text_in_file_decrypt['state'] = 'disabled'
                btn_decrypt['state'] = 'disabled'

                with open(filename, 'w') as file:
                    for line in text_in_file_decrypt.get('1.0', END):
                        file.write(line)

                messagebox.showinfo('Information', 'The File has been Decrypted.')
            else:
                messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')

        elif value == '--Caesar cipher':
            file_text = text_in_file_decrypt.get('1.0', END)
            alphabets = 'abcdefghijklmnopqrstuvwxyz'
            key = entry_decrypt.get()
            if key != '':
                file_content = file_text
                file_content = file_content.lower()
                key = int(entry_decrypt.get())
                cipher = ''

                for i in range(len(file_content)):
                    letter = file_content[i]
                    if letter == ' ':
                        cipher += ' '
                    else:
                        letter_position = alphabets.find(letter)
                        new_letter_position = (letter_position - key) % 26
                        cipher += alphabets[new_letter_position]

                # Changing File Content With Caesar Cipher
                text_in_file_decrypt['state'] = 'normal'
                text_in_file_decrypt.delete('1.0', END)
                text_in_file_decrypt.insert(END, cipher)
                text_in_file_decrypt['state'] = 'disabled'
                btn_decrypt['state'] = 'disabled'

                with open(filename, 'w') as file:
                    for line in text_in_file_decrypt.get('1.0', END):
                        file.write(line)
                messagebox.showinfo('Information', 'The File has been Decrypted.')
            else:
                messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')
        else:
            messagebox.showerror('Error', 'Please Select The Decryption Method.')
    except:
        messagebox.showerror('Error',
                             'Unexpected Error occurred.\nPlease Make Sure You Use This Application Accordingly.')


# Decryption Window Function
def decrypt_file():
    file_win = init_win()
    # File Menu
    menus = Menu(file_win)
    file_win.config(menu=menus)
    file_menus = Menu(menus)
    menus.add_cascade(label='File', menu=file_menus)
    file_menus.add_command(label='Open', command=decrypt_open_file)
    file_menus.add_command(label='Exit', command=file_win.quit)

    # ---File Window Frame One---
    # ---Text Area And Scrollbar---
    global comboBox_decrypt
    comboBox_decrypt = tk.Combobox(file_win, width=82, state='readonly')
    comboBox_decrypt['values'] = (
        '--Select cipher method--', '--Vernam cipher', '--Vigenere cipher', '--Transposition cipher', '--Caesar '
                                                                                                      'cipher')
    comboBox_decrypt.current(0)
    comboBox_decrypt.grid(row=0, column=0, pady=15)
    Label(file_win, text='Enter Decryption Key:').grid(row=1, column=0, sticky=W, pady=8, padx=10)
    global entry_decrypt
    entry_decrypt = Entry(file_win, width=65)
    entry_decrypt.grid(row=1, column=0, pady=8, padx=15, sticky=E)
    # Frame
    text_frame = Frame(file_win)
    scrollBar = Scrollbar(file_win)
    global text_in_file_decrypt
    text_in_file_decrypt = Text(file_win, width=64, height=13)
    scrollBar.grid(row=2, column=0, sticky='NSE')
    text_in_file_decrypt.grid(row=2, column=0, padx=15, pady=8)
    scrollBar.config(command=text_in_file_decrypt.yview)
    text_in_file_decrypt.config(yscrollcommand=scrollBar.set)
    text_frame.grid(row=0, column=0)

    # ---Button Encrypt---
    global btn_decrypt
    btn_decrypt = Button(file_win, text='Decrypt File', width=12, state='disabled', command=decrypt_text_in_file)
    btn_decrypt.grid(row=3, column=0, padx=15, sticky=E)
    file_win.mainloop()

# encrypt_file()
# decrypt_file()
