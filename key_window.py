from tkinter import *


# Window Key Display
def send_key(key):
    root = Tk()
    root.title('Your Key Is:')
    root.geometry('410x305')
    message = ''
    message += '\nPLEASE COPY AND KEEP THE KEY SAFE.\n\n'
    message += '----------------------------------------------\n\n'
    message += key
    message += '\n\n----------------------------------------------\n'
    frame = Frame(root)
    scrollBar = Scrollbar(frame)
    text = Text(frame, width=46, height=15)
    scrollBar.grid(row=0, column=1, sticky='NSE')
    text.grid(row=0, column=0)
    scrollBar.config(command=text.yview)
    text.config(yscrollcommand=scrollBar.set)
    frame.grid(row=0, column=0, padx=15, pady=15)
    text.insert(END, message)
    text['state'] = 'disable'
    root.mainloop()
