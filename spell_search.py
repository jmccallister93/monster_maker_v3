from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.spell_data import *
from string import *


#Spell search function
def spell_search(name=None, level=None, school=None, dndclass=None, spell_list=None):
    #covnert to lower 
    name.lower()
    #check if name matches list 
    if name == "a":
        pass