from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *

keys = []
values = []

score = 0
for s in range(0, 31, 2): #Loop through every other value 0-30 for score
    keys.append(str(s))

modifier = -6
for m in range(16): #Loop through every value to get modifier 
    modifier = modifier + 1
    values.append(str(modifier))

modifier_dict = dict(zip(keys,values))

#Add Stats Function
def add_stats(stats_combobox, stats_display, modifier_dict):
    stats_choice = StringVar()
    stats_choice = stats_combobox.get()
    stats_random = random.choice(stats_options_label)
    mod = StringVar()

    if stats_choice == "Random":
        stats_display['text'] = stats_random

        if stats_display['text'] == "0" or stats_display['text'] == "1":
            mod = modifier_dict["0"]
            stats_display['text'] = stats_random + " (" + mod + ")"

        elif stats_display['text'] == "2" or stats_display['text'] == "3":
            mod = modifier_dict["2"]
            stats_display['text'] = stats_random + " (" + mod + ")"

        elif stats_display['text'] == "4" or stats_display['text'] == "5":
            mod = modifier_dict["4"]
            stats_display['text'] = stats_random + " (" + mod + ")"

        elif stats_display['text'] == "6" or stats_display['text'] == "7":
            mod = modifier_dict["6"]
            stats_display['text'] = stats_random + " (" + mod + ")"

        elif stats_display['text'] == "8" or stats_display['text'] == "9":
            mod = modifier_dict["8"]
            stats_display['text'] = stats_random + " (" + mod + ")"

        elif stats_display['text'] == "10" or stats_display['text'] == "11":
            mod = modifier_dict["10"]
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "12" or stats_display['text'] == "13":
            mod = modifier_dict["12"]
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "14" or stats_display['text'] == "15":
            mod = modifier_dict["14"]
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "16" or stats_display['text'] == "17":
            mod = modifier_dict["16"]
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "18" or stats_display['text'] == "19":
            mod = modifier_dict["18"]
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "20" or stats_display['text'] == "21":
            mod = modifier_dict["20"]
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "22" or stats_display['text'] == "23":
            mod = modifier_dict["22"]   
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "24" or stats_display['text'] == "25":
            mod = modifier_dict["24"] 
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "26" or stats_display['text'] == "27":
            mod = modifier_dict["26"]
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "28" or stats_display['text'] == "29":
            mod = modifier_dict["28"]
            stats_display['text'] = stats_random + " (+" + mod + ")"

        elif stats_display['text'] == "30":
            mod = modifier_dict["30"]
            stats_display['text'] = stats_random + " (+" + mod + ")"
            
    else:
        stats_display['text'] = stats_choice
        
        if stats_display['text'] == "0" or stats_display['text'] == "1":
            mod = modifier_dict["0"]
            stats_display['text'] = stats_choice + " (" + mod + ")"

        elif stats_display['text'] == "2" or stats_display['text'] == "3":
            mod = modifier_dict["2"]
            stats_display['text'] = stats_choice + " (" + mod + ")"

        elif stats_display['text'] == "4" or stats_display['text'] == "5":
            mod = modifier_dict["4"]
            stats_display['text'] = stats_choice + " (" + mod + ")"

        elif stats_display['text'] == "6" or stats_display['text'] == "7":
            mod = modifier_dict["6"]
            stats_display['text'] = stats_choice + " (" + mod + ")"

        elif stats_display['text'] == "8" or stats_display['text'] == "9":
            mod = modifier_dict["8"]
            stats_display['text'] = stats_choice + " (" + mod + ")"

        elif stats_display['text'] == "10" or stats_display['text'] == "11":
            mod = modifier_dict["10"]
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "12" or stats_display['text'] == "13":
            mod = modifier_dict["12"]
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "14" or stats_display['text'] == "15":
            mod = modifier_dict["14"]
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "16" or stats_display['text'] == "17":
            mod = modifier_dict["16"]
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "18" or stats_display['text'] == "19":
            mod = modifier_dict["18"]
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "20" or stats_display['text'] == "21":
            mod = modifier_dict["20"]
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "22" or stats_display['text'] == "23":
            mod = modifier_dict["22"]   
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "24" or stats_display['text'] == "25":
            mod = modifier_dict["24"] 
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "26" or stats_display['text'] == "27":
            mod = modifier_dict["26"]
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "28" or stats_display['text'] == "29":
            mod = modifier_dict["28"]
            stats_display['text'] = stats_choice + " (+" + mod + ")"

        elif stats_display['text'] == "30":
            mod = modifier_dict["30"]
            stats_display['text'] = stats_choice + " (+" + mod + ")"