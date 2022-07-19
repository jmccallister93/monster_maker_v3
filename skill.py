from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *
import tkinter.messagebox

#Add Skill function
def add_skill(skill_type_combobox, skill_value_entry, skill_display, skill_list):
    
    #Type
    skill_type_choice = StringVar()
    skill_type_choice = skill_type_combobox.get()
    skill_type_random = random.choice(skill_type_options_label)
    #Value
    skill_value = skill_value_entry.get()
    skill_value_random = random.choice(skill_value_options_label)

    if skill_type_choice == "Random" and skill_value == "":
        skill_list.append(skill_type_random + ' ' + skill_value_random)
        skill_display['text'] = ' | '.join(skill_list)

    elif skill_type_choice == "Random" and skill_value != "":
        skill_list.append(skill_type_random + ' +' + skill_value + ' ft')
        skill_display['text'] = ' | '.join(skill_list)
    
    elif skill_type_choice != "Random" and skill_value == "":
        skill_list.append(skill_type_choice + ' ' + skill_value_random)
        skill_display['text'] = ' | '.join(skill_list)

    elif skill_type_choice != "Random" and skill_value != "":
        skill_list.append(skill_type_choice + ' +' + skill_value + ' ft')
        skill_display['text'] = ' | '.join(skill_list)

    return skill_list
    