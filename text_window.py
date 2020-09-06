from tkinter import *
from tkinter import ttk as tk
from string import ascii_letters
from tkinter import messagebox
import random
from textwrap import wrap
from key_window import send_key
from tkinter import filedialog


# Command Function
# Send Own Text To Binary Generator Function For Encryption
def encrypt_own_text():
    try:
        value = comboBox_encrypt.get()
        if value == '--Vernam cipher':
            msgbx_results = messagebox.askyesno('Message Encryption', 'The Message Will Be Encrypted!\n'
                                                                      'Do You Want To Continue?')
            typed_text = own_text_encrypt.get('1.0', END)
            if msgbx_results == 1:
                # Convert File Content To Binary
                user_input = typed_text
                user_binary = [bin(ord(letter))[2:].ljust(15, '0') for letter in user_input]
                global random_key
                random_key = "".join(random.choice(ascii_letters) for letter in range(len(user_input)))
                global key_binary
                key_binary = [bin(ord(letter))[2:].ljust(15, '0') for letter in random_key]

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
                own_text_encrypt.delete('1.0', END)
                own_text_encrypt.insert(END, ciphertext)
                own_text_encrypt['state'] = 'disabled'
                btn_encrypt['state'] = 'disabled'
                messagebox.showinfo('Information', 'The Message Has Been Encrypted')
                send_key(random_key)
            else:
                return

        elif value == '--Vigenere cipher':
            msgbx_results = messagebox.askyesno('Message Encryption',
                                                'The Message Will Be Encrypted!\nDo You Want To Continue?')
            typed_text = own_text_encrypt.get('1.0', END)
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

                    for i in range(len(typed_text)):
                        letter += [alphabets.find(typed_text[i])]
                        while len(list_key) < len(alphabets):
                            list_key += [key[j] for j in range(len(key))]

                        letter[i] = (letter[i] + list_key[i]) % 26
                        cipher += alphabets[letter[i]]

                    own_text_encrypt['state'] = 'normal'
                    own_text_encrypt.delete('1.0', END)
                    own_text_encrypt.insert(END, cipher)
                    own_text_encrypt['state'] = 'disabled'
                    btn_encrypt['state'] = 'disabled'
                    messagebox.showinfo('Information', 'The Message has been Encrypted.')
                else:
                    messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')
            else:
                return

        elif value == '--Transposition cipher':
            msgbx_results = messagebox.askyesno('Message Encryption',
                                                'The Message Will Be Encrypted!\nDo You Want To Continue?')
            typed_text = own_text_encrypt.get('1.0', END)
            if msgbx_results == 1:
                user_key = entry_encrypt.get()
                if user_key != '':
                    user_key = int(entry_encrypt.get())
                    cipher = [''] * user_key
                    for table_col in range(user_key):
                        cursor = table_col
                        while cursor < len(typed_text):
                            cipher[table_col] += typed_text[cursor]
                            cursor += user_key

                    own_text_encrypt['state'] = 'normal'
                    own_text_encrypt.delete('1.0', END)
                    own_text_encrypt.insert(END, ''.join(cipher))
                    own_text_encrypt['state'] = 'disabled'
                    btn_encrypt['state'] = 'disabled'
                    messagebox.showinfo('Information', 'The Message has been Encrypted.')
                else:
                    messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')
            else:
                return

        elif value == '--Caesar cipher':
            msgbx_results = messagebox.askyesno('Message Encryption',
                                                'The Message Will Be Encrypted!\nDo You Want To Continue?')
            if msgbx_results == 1:
                typed_text = own_text_encrypt.get('1.0', END)
                alphabets = 'abcdefghijklmnopqrstuvwxyz'
                key = entry_encrypt.get()
                if key != '':
                    file_content = typed_text
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
                    own_text_encrypt.delete('1.0', END)
                    own_text_encrypt.insert(END, cipher)
                    own_text_encrypt['state'] = 'disabled'
                    btn_encrypt['state'] = 'disabled'
                    messagebox.showinfo('Information', 'The Message Has Been Encrypted')
                else:
                    messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')
            else:
                return
        else:
            messagebox.showerror('Error', 'Please Select The Encryption Method.')
    except:
        messagebox.showerror('Error',
                             'Unexpected Error occurred.\nPlease Make Sure You Use This Application Accordingly.')



def encrypt_text():
    # ---GUI Definition---
    text_win = Tk()
    text_win.title('Text Encryption')
    text_win.geometry('550x350')
    text_win.resizable(False, False)

    # Text Menu
    menus = Menu(text_win)
    text_win.config(menu=menus)
    text_menus = Menu(menus)
    menus.add_cascade(label='_File', menu=text_menus)
    text_menus.add_command(label='Exit', command=text_win.quit)

    # ---Text Window Frame One---
    global comboBox_encrypt
    comboBox_encrypt = tk.Combobox(text_win, width=82, state='readonly')
    comboBox_encrypt['values'] = (
        '--Select cipher method--', '--Vernam cipher', '--Vigenere cipher', '--Transposition cipher', '--Caesar '
                                                                                                      'cipher')
    comboBox_encrypt.current(0)
    comboBox_encrypt.grid(row=0, column=0, pady=10)
    # Key Entry With Label
    Label(text_win, text='Enter Encryption Key:').grid(row=1, column=0, sticky=W, padx=13)
    global entry_encrypt
    entry_encrypt = Entry(text_win, width=65)
    entry_encrypt.grid(row=1, column=0, padx=15, sticky=E)
    # ---Text Area---
    text_frame = Frame(text_win)
    scrollBar = Scrollbar(text_win)
    global own_text_encrypt
    own_text_encrypt = Text(text_win, width=64, height=14)
    scrollBar.grid(row=2, column=0, pady=15, sticky='NSE')
    own_text_encrypt.grid(row=2, column=0, padx=15, pady=10)
    scrollBar.config(command=own_text_encrypt.yview)
    own_text_encrypt.config(yscrollcommand=scrollBar.set)

    # ---Button Encrypt---
    global btn_encrypt
    btn_encrypt = Button(text_win, text='Encrypt Text', width=12, command=encrypt_own_text)
    btn_encrypt.grid(row=3, column=0, padx=15, sticky=E)
    text_frame.grid(row=0, column=0)
    text_win.mainloop()


# Text Decryption
def decrypt_own_text():
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

                    plaintext = ''
                    plaintext_plus = ''
                    for i in range(len(plaintext_binary_split)):
                        plaintext_binary_split_item = plaintext_binary_split[i]
                        plaintext += chr(int(plaintext_binary_split_item, 2))

                    # Inserting Plaintext
                    own_text_decrypt['state'] = 'normal'
                    own_text_decrypt.delete('1.0', END)
                    own_text_decrypt.insert(END, plaintext)
                    btn_decrypt['state'] = 'disabled'
                    messagebox.showinfo('Information', 'The Message has been Decrypted.')
                else:
                    messagebox.showerror('Incorrect Key', 'The Key Is Incorrect.\nPlease Enter The Correct Key.')
            else:
                messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')

        elif value == '--Vigenere cipher':
            typed_text = own_text_decrypt.get('1.0', END)
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

                for i in range(len(typed_text)):
                    letter += [alphabets.find(typed_text[i])]
                    while len(list_key) < len(alphabets):
                        list_key += [key[j] for j in range(len(key))]

                    letter[i] = (letter[i] - list_key[i]) % 26
                    cipher += alphabets[letter[i]]

                own_text_decrypt['state'] = 'normal'
                own_text_decrypt.delete('1.0', END)
                own_text_decrypt.insert(END, cipher)
                own_text_decrypt['state'] = 'disabled'
                btn_decrypt['state'] = 'disabled'
                messagebox.showinfo('Information', 'The Message has been Decrypted.')
            else:
                messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')

        elif value == '--Transposition cipher':
            from math import ceil
            typed_text = own_text_decrypt.get('1.0', END)
            key = entry_decrypt.get()
            if key != '':
                typed_text = typed_text.lower()
                user_key = int(entry_decrypt.get())

                text_length = len(typed_text)
                current_column = 0
                current_row = 0
                num_of_rows = ceil(text_length / user_key)
                table_content = (num_of_rows * user_key) - text_length
                plaintext = [''] * num_of_rows

                for table_col in typed_text:
                    plaintext[current_column] += table_col
                    current_column += 1
                    if (current_column == num_of_rows) \
                            or (current_column == num_of_rows - 1 and current_row >= user_key - table_content):
                        current_column = 0
                        current_row += 1

                own_text_decrypt['state'] = 'normal'
                own_text_decrypt.delete('1.0', END)
                own_text_decrypt.insert(END, plaintext)
                own_text_decrypt['state'] = 'disabled'
                btn_decrypt['state'] = 'disabled'
                messagebox.showinfo('Information', 'The Message Has Been Decrypted')
            else:
                messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')

        elif value == '--Caesar cipher':
            typed_text = own_text_decrypt.get('1.0', END)
            alphabets = 'abcdefghijklmnopqrstuvwxyz'
            key = entry_decrypt.get()
            if key != '':
                file_content = typed_text
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
                own_text_decrypt.delete('1.0', END)
                own_text_decrypt.insert(END, cipher)
                own_text_decrypt['state'] = 'disabled'
                btn_decrypt['state'] = 'disabled'
                messagebox.showinfo('Information', 'The Message Has Been Decrypted')
            else:
                messagebox.showerror('Null Entry', 'The Key Entry Cannot Be Null,\nPlease Enter Key.')
        else:
            messagebox.showerror('Error', 'Please Select The Decryption Method.')
    except:
        messagebox.showerror('Error',
                             'Unexpected Error occurred.\nPlease Make Sure You Use This Application Accordingly.')


def decrypt_text():
    # ---GUI Definition---
    text_win = Tk()
    text_win.title('Text Decryption')
    text_win.geometry('550x350')
    text_win.resizable(False, False)

    # Text Menu
    menus = Menu(text_win)
    text_win.config(menu=menus)
    text_menus = Menu(menus)
    menus.add_cascade(label='_File', menu=text_menus)
    text_menus.add_command(label='Exit', command=text_win.quit)

    # ---Text Window Frame One---
    global comboBox_decrypt
    comboBox_decrypt = tk.Combobox(text_win, width=82, state='readonly')
    comboBox_decrypt['values'] = (
        '--Select cipher method--', '--Vernam cipher', '--Vigenere cipher', '--Transposition cipher', '--Caesar '
                                                                                                      'cipher')
    comboBox_decrypt.current(0)
    comboBox_decrypt.grid(row=0, column=0, pady=15)
    # ---Text Area---
    Label(text_win, text='Enter Decryption Key:').grid(row=1, column=0, sticky=W, pady=8, padx=10)
    global entry_decrypt
    entry_decrypt = Entry(text_win, width=65)
    entry_decrypt.grid(row=1, column=0, pady=8, padx=15, sticky=E)
    # Frame
    text_frame = Frame(text_win)
    scrollBar = Scrollbar(text_win)
    global own_text_decrypt
    own_text_decrypt = Text(text_win, width=64, height=13)
    scrollBar.grid(row=2, column=0, sticky='NSE')
    own_text_decrypt.grid(row=2, column=0, padx=15, pady=8)
    scrollBar.config(command=own_text_decrypt.yview)
    own_text_decrypt.config(yscrollcommand=scrollBar.set)
    text_frame.grid(row=0, column=0)
    # ---Button Encrypt---
    global btn_decrypt
    btn_decrypt = Button(text_win, text='Decrypt Text', width=12, command=decrypt_own_text)
    btn_decrypt.grid(row=3, column=0, padx=15, sticky=E)
    text_win.mainloop()

# encrypt_text()
# decrypt_text()
