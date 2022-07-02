from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *

def add_size(size_combobox, size_display):
    size_choice = StringVar()
    size_choice = size_combobox.get()
    random_size = random.choice(size_options_label)
    if size_choice == "Random":
        size_display['text'] = random_size
    else:
        size_display['text'] = size_choice
    
    