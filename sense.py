from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *
import tkinter.messagebox

#Add Sense function
def add_sense(sense_type_combobox, sense_value_entry, sense_display, sense_list):
    
    #Type
    sense_type_choice = StringVar()
    sense_type_choice = sense_type_combobox.get()
    sense_type_random = random.choice(sense_type_options_label)
    #Value
    sense_value = sense_value_entry.get()
    sense_value_random = random.choice(sense_value_options_label)

    if sense_type_choice == "Random" and sense_value == "":
        sense_list.append(sense_type_random + ' ' + sense_value_random)
        sense_display['text'] = ' | '.join(sense_list)

    elif sense_type_choice == "Random" and sense_value != "":
        sense_list.append(sense_type_random + ' ' + sense_value + ' ft')
        sense_display['text'] = ' | '.join(sense_list)
    
    elif sense_type_choice != "Random" and sense_value == "":
        sense_list.append(sense_type_choice + ' ' + sense_value_random)
        sense_display['text'] = ' | '.join(sense_list)

    elif sense_type_choice != "Random" and sense_value != "":
        sense_list.append(sense_type_choice + ' ' + sense_value + ' ft')
        sense_display['text'] = ' | '.join(sense_list)

    return sense_list
    