from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *


#Add Monster Type function
def add_monster_type(monster_type_combobox, monster_type_display):
    monster_type_choice = StringVar()
    monster_type_choice = monster_type_combobox.get()
    monster_random_type = random.choice(monster_type_options_label)
    if monster_type_choice == "Random":
        monster_type_display['text'] = monster_random_type
    else:
        monster_type_display['text'] = monster_type_choice