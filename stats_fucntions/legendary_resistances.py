from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *

#Add legendary_resist Function
def add_legendary_resist(legendary_resist_combobox, legendary_resist_display):
    legendary_resist_choice = StringVar()
    legendary_resist_choice = legendary_resist_combobox.get()
    legendary_resist_random = random.choice(legendary_resist_options_label)
    if legendary_resist_choice == "Random":
        legendary_resist_display['text'] = legendary_resist_random
    else:
        legendary_resist_display['text'] = legendary_resist_choice