from tkinter import StringVar
from main import *
import customtkinter as ctk
import random
from data.combobox_options import *
from data.label_options import *

def remove_stat(my_list, stat):
    my_list.pop(stat)
    return my_list