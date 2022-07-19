from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *

#Monster Name Funciton
def add_monster_name(monster_name_entry, monster_name_display):
    monster_name = monster_name_entry.get()
    monster_name_random = random.choice(monster_name_options_label)
    if monster_name == "":
        monster_name_display['text'] = monster_name_random
    else:
        monster_name_display['text'] = monster_name

