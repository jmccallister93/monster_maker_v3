from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *

#Add Stats Function
def add_stats(stats_combobox, stats_display):
    stats_choice = StringVar()
    stats_choice = stats_combobox.get()
    stats_random = random.choice(stats_options_label)
    if stats_choice == "Random":
        stats_display['text'] = stats_random
    else:
        stats_display['text'] = stats_choice
    return stats_display