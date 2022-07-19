from tkinter import StringVar
from main import *
import customtkinter as ctk
import tkinter
import random
from data.combobox_options import *
from data.label_options import *

#Add Spell Function
def add_spell(spell_combobox, spell_display, spell_list):
    spell_choice = StringVar()
    spell_choice = spell_combobox.get()
    spell_random = random.choice(spell_options_label)
    if any(spell_choice in s for s in spell_list) or any(spell_random in s for s in spell_list):
        tkinter.messagebox.showinfo('Error', f'{spell_choice} Spell already added.')
    else:
        if spell_choice == "Random":
            spell_list.append(spell_random)
            spell_display['text'] = ' | '.join(spell_list)
        else:
            spell_list.append(spell_choice)
            spell_display['text'] = ' | '.join(spell_list)

    return spell_list