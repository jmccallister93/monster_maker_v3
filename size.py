from tkinter import StringVar
from main import *
from data_lists import * 
import customtkinter as ctk
import random



class Size():
    def __init__(self, display_size, size_combobox) -> None:
        super().__init__()


def add_size(size_combobox, display_size):
    size_choice = StringVar()
    size_choice = size_combobox.get()
    random_size = random.choice(size_options_label)
    if size_choice == "Random":
        display_size['text'] = random_size
    else:
        display_size['text'] = size_choice
    
    