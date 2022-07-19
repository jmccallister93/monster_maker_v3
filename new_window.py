from libraries import * 
from data.combobox_options import *
from data.label_options import * 
from data.url_links import *
from data.spell_data import *
import customtkinter as ctk
import tkinter as tk 
from main import Window

master = Window()

class NewWindow(ctk.CTkToplevel):
    def __init__(self, master = None):
        super().__init__(master=master)

        self.title("Spells")
        self.geometry("750x750")

        spell_search_label = ctk.CTkLabel(master=self, text="Search")
        spell_level_label = ctk.CTkLabel(master=self, text="Level")
        spell_school_label = ctk.CTkLabel(master=self, text="School")
        spell_class_label = ctk.CTkLabel(master=self, text="Class")

        spell_search_entry = ctk.CTkEntry(master=self, placeholder_text="Search by Name")
        spell_level_combobox = ctk.CTkComboBox(master=self, values="spell level combo")
        spell_school_combobox = ctk.CTkComboBox(master=self, values="spell school combo")
        spell_class_combobox = ctk.CTkComboBox(master=self, values="spell class combo")

        spell_level_combobox.set("Random")
        spell_school_combobox.set("Random")
        spell_class_combobox.set("Random")

        spell_search_label.grid(row=0, column=0)
        spell_level_label.grid(row=0, column=1)
        spell_school_label.grid(row=0, column=2)
        spell_class_label.grid(row=0, column=3)

        spell_search_entry.grid(row=1, column=0)
        spell_level_combobox.grid(row=1, column=1)
        spell_school_combobox.grid(row=1, column=2)
        spell_class_combobox.grid(row=1, column=3)

        
        
        
        



