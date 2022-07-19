from tkinter import StringVar
from main import *
import customtkinter as ctk
import tkinter
import random
from data.combobox_options import *
from data.label_options import *

#Add Vuln Function
def add_vuln(vuln_combobox, vuln_display, vuln_list):
    vuln_choice = StringVar()
    vuln_choice = vuln_combobox.get()
    vuln_random = random.choice(vuln_options_label)
    if any(vuln_choice in s for s in vuln_list) or any(vuln_random in s for s in vuln_list):
        tkinter.messagebox.showinfo('Error', f'{vuln_choice} Vulnerability type already added.')
    else:
        if vuln_choice == "Random":
            vuln_list.append(vuln_random)
            vuln_display['text'] = ' | '.join(vuln_list)
        else:
            vuln_list.append(vuln_choice)
            vuln_display['text'] = ' | '.join(vuln_list)
    return vuln_list