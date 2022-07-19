from tkinter import StringVar
from main import *
import customtkinter as ctk
import tkinter
import random
from data.combobox_options import *
from data.label_options import *

#Add Language Function
def add_lang(lang_combobox, lang_display, lang_list):
    lang_choice = StringVar()
    lang_choice = lang_combobox.get()
    lang_random = random.choice(lang_options_label)
    if any(lang_choice in s for s in lang_list) or any(lang_random in s for s in lang_list):
        tkinter.messagebox.showinfo('Error', f'{lang_choice} Language already added.')
    else:
        if lang_choice == "Random":
            lang_list.append(lang_random)
            lang_display['text'] = ' | '.join(lang_list)
        else:
            lang_list.append(lang_choice)
            lang_display['text'] = ' | '.join(lang_list)
    return lang_list