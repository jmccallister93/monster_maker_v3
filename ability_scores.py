from tkinter import StringVar
from main import *
import customtkinter as ctk
import tkinter
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

#Create Score Mod Calc Function
def calculate_score_modifier(ability_score, ability_scores_display, modifier_dict, ability_score_list):
    mod = StringVar()
    ability_score = ability_score["text"]
    
    if ability_score == "0" or ability_score == "1":
        mod = modifier_dict["0"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "2" or ability_score == "3":
        mod = modifier_dict["2"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "4" or ability_score == "5":
        mod = modifier_dict["4"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "6" or ability_score == "7":
        mod = modifier_dict["6"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "8" or ability_score == "9":
        mod = modifier_dict["8"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "10" or ability_score == "11":
        mod = modifier_dict["10"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "12" or ability_score == "13":
        mod = modifier_dict["12"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "14" or ability_score == "15":
        mod = modifier_dict["14"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "16" or ability_score == "17":
        mod = modifier_dict["16"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "18" or ability_score == "19":
        mod = modifier_dict["18"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "20" or ability_score == "21":
        mod = modifier_dict["20"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "22" or ability_score == "23":
        mod = modifier_dict["22"]   
        ability_score_list.append(mod)
    elif ability_score == "24" or ability_score == "25":
        mod = modifier_dict["24"] 
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "26" or ability_score == "27":
        mod = modifier_dict["26"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "28" or ability_score == "29":
        mod = modifier_dict["28"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    elif ability_score == "30":
        mod = modifier_dict["30"]
        ability_score_list.append(mod)
        ability_scores_display['text'] = ' | '.join(ability_score_list)

    ability_scores_display['text'] = ability_score_list

    return ability_score_list