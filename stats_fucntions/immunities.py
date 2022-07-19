from tkinter import StringVar
from main import *
import customtkinter as ctk
import tkinter
import random
from data.combobox_options import *
from data.label_options import *

#Add Immune Function
def add_immune(immune_combobox, immune_display, immune_list):
    immune_choice = StringVar()
    immune_choice = immune_combobox.get()
    immune_random = random.choice(immune_options_label)
    if any(immune_choice in s for s in immune_list) or any(immune_random in s for s in immune_list):
        tkinter.messagebox.showinfo('Error', f'{immune_choice} Immunity type already added.')
    else:
        if immune_choice == "Random":
            immune_list.append(immune_random)
            immune_display['text'] = ' | '.join(immune_list)
        else:
            immune_list.append(immune_choice)
            immune_display['text'] = ' | '.join(immune_list)
    return immune_list