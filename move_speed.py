from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *

#Move Speed Function
def add_move_speed(move_speed_entry, move_speed_display):
    move_speed = move_speed_entry.get()
    move_speed_random = random.choice(move_speed_options_label)
    if move_speed == "":
        move_speed_display['text'] = move_speed_random
    else:
        move_speed_display['text'] = move_speed + " ft"