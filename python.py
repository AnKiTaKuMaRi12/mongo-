from tkinter import *

MORSE_CODE_DICT={'A':'.-','B':'-...',
                 'C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'...',
                 'I':'..','J':'.---','K':'.-.','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.--',
                 'R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'..-','Y':'-.--','Z':'--..',
                 '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..',
                 '9':'----.','0':'-----',',':'--..--','.':'.-.-.-','?':'..--..','/':'-..-.','-':-'....-',
                 '(':'-.--.',')':'-.--.-'
                 }

class convertion():
    def __init__(self):
        self.MORSE_CODE_DICT=MORSE_CODE_DICT
        root=Tk()
        self.txxt=StringVar()
        root.geometry('1280*720')
        fram=Frame(root)
        fram.place(relx=.5,rely=.5,anchor='center')
        txt=Label(fram,text='Letters')
