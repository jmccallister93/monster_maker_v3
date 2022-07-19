from tkinter import StringVar
from main import *
import customtkinter as ctk
import tkinter
import random
from data.combobox_options import *
from data.label_options import *

#Add Cond Immune Function
def add_cond_immune(cond_immune_combobox, cond_immune_display, cond_immune_list):
    cond_immune_choice = StringVar()
    cond_immune_choice = cond_immune_combobox.get()
    cond_immune_random = random.choice(cond_immune_options_label)
    if any(cond_immune_choice in s for s in cond_immune_list) or any(cond_immune_random in s for s in cond_immune_list):
        tkinter.messagebox.showinfo('Error', f'{cond_immune_choice} Immunity type already added.')
    else:
        if cond_immune_choice == "Random":
            cond_immune_list.append(cond_immune_random)
            cond_immune_display['text'] = ' | '.join(cond_immune_list)
        else:
            cond_immune_list.append(cond_immune_choice)
            cond_immune_display['text'] = ' | '.join(cond_immune_list)
    return cond_immune_list