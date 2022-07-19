from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *


#Add AC Type function
def add_ac_type(ac_type_combobox, ac_type_display):
    ac_type_choice = StringVar()
    ac_type_choice = ac_type_combobox.get()
    ac_type_random = random.choice(ac_type_options_label)
    if ac_type_choice == "Random":
        ac_type_display['text'] = ac_type_random
    else:
        ac_type_display['text'] = ac_type_choice