from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *


#AC Value Function
def add_ac_value(ac_value_entry, ac_value_display):
    ac_value = ac_value_entry.get()
    ac_value_random = random.choice(ac_value_options_label)
    if ac_value == "":
        ac_value_display['text'] = ac_value_random
    else:
        ac_value_display['text'] = ac_value
