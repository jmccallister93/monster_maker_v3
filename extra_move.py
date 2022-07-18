from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *
import tkinter.messagebox

#Add Extra Move function
def add_extra_move(extra_move_type_combobox, extra_move_speed_entry, extra_move_display, extra_move_list):
    
    #Type
    extra_move_type_choice = StringVar()
    extra_move_type_choice = extra_move_type_combobox.get()
    extra_move_type_random = random.choice(extra_move_type_options_label)
    #Speed
    extra_move_speed = extra_move_speed_entry.get()
    extra_move_speed_random = random.choice(extra_move_speed_options_label)

    # if any(extra_move_type_choice in s for s in extra_move_list) or any(extra_move_type_random in s for s in extra_move_list):
    #     tkinter.messagebox.showinfo('Error', f'{extra_move_type_options_label} Movement type already added.')
    # else:
    if extra_move_type_choice == "Random" and extra_move_speed == "":
        extra_move_list.append(extra_move_type_random + ' ' + extra_move_speed_random)
        extra_move_display['text'] = ' | '.join(extra_move_list)

    elif extra_move_type_choice == "Random" and extra_move_speed != "":
        extra_move_list.append(extra_move_type_random + ' ' + extra_move_speed + ' ft')
        extra_move_display['text'] = ' | '.join(extra_move_list)
    
    elif extra_move_type_choice != "Random" and extra_move_speed == "":
        extra_move_list.append(extra_move_type_choice + ' ' + extra_move_speed_random)
        extra_move_display['text'] = ' | '.join(extra_move_list)

    elif extra_move_type_choice != "Random" and extra_move_speed != "":
        extra_move_list.append(extra_move_type_choice + ' ' + extra_move_speed + ' ft')
        extra_move_display['text'] = ' | '.join(extra_move_list)

    return extra_move_list