from tkinter import *

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',

                   'C': '-.-.', 'D': '-..', 'E': '.',

                   'F': '..-.', 'G': '--.', 'H': '....',

                   'I': '..', 'J': '.---', 'K': '-.-',

                   'L': '.-..', 'M': '--', 'N': '-.',

                   'O': '---', 'P': '.--.', 'Q': '--.-',

                   'R': '.-.', 'S': '...', 'T': '-',

                   'U': '..-', 'V': '...-', 'W': '.--',

                   'X': '-..-', 'Y': '-.--', 'Z': '--..',

                   '1': '.----', '2': '..---', '3': '...--',

                   '4': '....-', '5': '.....', '6': '-....',

                   '7': '--...', '8': '---..', '9': '----.',

                   '0': '-----', ', ': '--..--', '.': '.-.-.-',

                   '?': '..--..', '/': '-..-.', '-': '-....-',

                   '(': '-.--.', ')': '-.--.-'}


class convertion():

    def __init__(self):

        self.MORSE_CODE_DICT = MORSE_CODE_DICT

        root = Tk()

        self.txxt = StringVar()

        root.geometry('1280x720')

        fram = Frame(root)

        fram.place(relx=.5, rely=.5, anchor='center')

        txt = Label(fram, text='Letters', font=('arial', 20, 'bold'))

        txt.grid(row=0, column=0, padx=10, pady=10)

        entry = Entry(fram, font=('arial', 15), textvariable=self.txxt)

        entry.grid(column=1, row=0, padx=10, pady=10)

        txt = Label(fram, text='Morsecode', font=('arial', 20, 'bold'))

        txt.grid(row=1, column=0, padx=10, pady=10)

        self.give = Text(fram, height=1, width=20, font=('arial', 15))

        self.give.grid(column=1, row=1, padx=10, pady=10)

        self.give.configure(state='disable')

        but = Button(fram, text='Convert', width=15, font=('arial', 15), bg='green', command=self.encrypt)

        but.grid(columnspan=2, row=2)

        root.mainloop()

    def encrypt(self):

        self.give.configure(state='normal')

        self.give.delete(1.0, END)

        message = self.txxt.get()

        cipher = ''

        for letter in message:

            if letter != ' ':
                cipher += self.MORSE_CODE_DICT[letter] + ' '

        else:

            cipher += ' '

        self.give.insert(0.0, cipher)

        self.give.configure(state='disable')


obj = convertion()
