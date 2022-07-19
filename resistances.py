from tkinter import StringVar
from main import *
import customtkinter as ctk
import tkinter
import random
from data.combobox_options import *
from data.label_options import *

#Add resist Function
def add_resist(resist_combobox, resist_display, resist_list):
    resist_choice = StringVar()
    resist_choice = resist_combobox.get()
    resist_random = random.choice(resist_options_label)
    if any(resist_choice in s for s in resist_list) or any(resist_random in s for s in resist_list):
        tkinter.messagebox.showinfo('Error', f'{resist_choice} Immunity type already added.')
    else:
        if resist_choice == "Random":
            resist_list.append(resist_random)
            resist_display['text'] = ' | '.join(resist_list)
        else:
            resist_list.append(resist_choice)
            resist_display['text'] = ' | '.join(resist_list)
    return resist_list