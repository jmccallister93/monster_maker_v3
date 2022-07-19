from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *


#HP Value Function
def add_hp_value(hp_value_entry, hp_value_display):
    hp_value = hp_value_entry.get()
    hp_value_random = random.randrange(10, 500, 2)
    if hp_value == "":
        hp_value_display['text'] = hp_value_random
    else:
        hp_value_display['text'] = hp_value