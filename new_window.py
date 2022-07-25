from numpy import size
from pygame import ACTIVEEVENT
from libraries import * 
from data.combobox_options import *
from data.label_options import * 
from data.url_links import *
from data.spell_data import *
import customtkinter as ctk
import tkinter as tk 
from main import Window
from spell_search import *
from tkinter import StringVar

master = Window()

class NewWindow(ctk.CTkToplevel):
    def __init__(self, master = None):
        super().__init__(master=master)

        self.title("Spells")
        self.geometry("750x750")
#Frames
        #Configure grid layout (1x2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        #Configure Top Frame
        self.frame_top = ctk.CTkFrame(master=self,width=180,corner_radius=0)
        self.frame_top.grid(row=0, column=0, sticky="nswe", padx=10,pady=10)
        #Configure Middle Frame
        self.frame_middle = ctk.CTkFrame(master=self,width=180, height=30, corner_radius=0)
        self.frame_middle.grid(row=1, column=0, sticky="nswe", padx=10,pady=10)
        #Configure Bottom Frame
        self.frame_bottom = ctk.CTkFrame(master=self,width=10,corner_radius=0)
        self.frame_bottom.grid(row=2, column=0, sticky="nswe", padx=10,pady=10)

#Labels
        #Top Frame
        spell_search_label = ctk.CTkLabel(master=self.frame_top, text="Search")
        spell_level_label = ctk.CTkLabel(master=self.frame_top, text="Level")
        spell_school_label = ctk.CTkLabel(master=self.frame_top, text="School")
        spell_class_label = ctk.CTkLabel(master=self.frame_top, text="Class")

        #Middle Frame
        spell_highlighted_label = tk.Label(master=self.frame_middle, bg='#2c2c2c', fg='#ffffff', 
                                            text="Selected:", font=("Havetica",16))
        spell_selected_label = tk.Label(master=self.frame_middle, bg='#2c2c2c', fg='#ffffff',  
                                        text=" ", font=("Havetica",16))
        #Bottom Frame
        spell_name_display = ctk.CTkLabel(master=self.frame_bottom, text="Name")
        spell_level_display = ctk.CTkLabel(master=self.frame_bottom, text="Level")
        spell_school_display = ctk.CTkLabel(master=self.frame_bottom, text="School")
        spell_details_display = ctk.CTkLabel(master=self.frame_bottom, text="Description")
#Listbox
        # #Update Listbox with list
        def update_listbox(data):
            #Clear list box
            spell_listbox.delete(0, tk.END)
            #Loop through list
            for item in data:
                spell_listbox.insert(tk.END, item)

        #Update entry box with listbox clicked
        def selected_item(event): 
            #Add clicked item to entry 
            spell_selected_label['text'] = spell_listbox.get(tk.ACTIVE)

        #Update listbox based on level selected 
        def update_listbox_data(spell_level_combobox):
            #Get selected level
            level_selected = StringVar()
            level_selected = spell_level_combobox.get()
            if level_selected == "All":
                data = spell_all_options_listbox
            elif level_selected == "Cantrip":
                data = spell_lvl_0_options_listbox
            elif level_selected == "Level 1":
                data = spell_lvl_1_options_listbox
            elif level_selected == "Level 2":
                data = spell_lvl_2_options_listbox
            elif level_selected == "Level 3":
                data = spell_lvl_3_options_listbox
            elif level_selected == "Level 4":
                data = spell_lvl_4_options_listbox
            elif level_selected == "Level 5":
                data = spell_lvl_5_options_listbox
            elif level_selected == "Level 6":
                data = spell_lvl_6_options_listbox
            elif level_selected == "Level 7":
                data = spell_lvl_7_options_listbox
            elif level_selected == "Level 8":
                data = spell_lvl_8_options_listbox
            elif level_selected == "Level 9":
                data = spell_lvl_9_options_listbox

            update_listbox(data)

        #Check Listbox from typed word
        def check(event):
            typed = spell_search_entry.get()
            if typed == "":
                data = spell_all_options_listbox
            else:
                data = []
                for item in spell_all_options_listbox:
                    if typed.lower() in item.lower():
                        data.append(item)
            #Update list with what is typed
            update_listbox(data)

        #Create Listbox
        spell_listbox = tk.Listbox(master=self.frame_bottom, width=100, bg="#36454F", fg='#ffffff')
        spell_listbox.grid(row=1, column=0, columnspan=4)

        #Bind selected item from listbox
        spell_listbox.bind("<<ListboxSelect>>", selected_item)

        #Binding for entry box
        spell_search_entry = tk.Entry(master=self.frame_top, text="Search by Name", bg="#36454F", fg='#ffffff')
        spell_search_entry.bind("<KeyRelease>", check)

#Comboboxes
        
        spell_level_combobox = ctk.CTkComboBox(master=self.frame_top, values=spell_level_options_combobox)
        spell_school_combobox = ctk.CTkComboBox(master=self.frame_top, values=spell_school_options_combobox)
        spell_class_combobox = ctk.CTkComboBox(master=self.frame_top, values=spell_class_options_combobox)

        spell_level_combobox.set("All")
        spell_school_combobox.set("All")
        spell_class_combobox.set("All")

#Functions
        
        #Set listbox options
        
        update_listbox_data(spell_level_combobox) #TODO 
        search_command = lambda: update_listbox_data(spell_level_combobox)

#Buttons
        spell_add_btn = ctk.CTkButton(master=self.frame_middle, text="+", width=50)
        spell_search_btn = ctk.CTkButton(master=self.frame_top, text="Search", command=search_command, width=50)

#Grid Layout
        #Top Frame
        #Row 0
        spell_search_label.grid(row=0, column=0)
        spell_level_label.grid(row=0, column=1)
        spell_school_label.grid(row=0, column=2)
        spell_class_label.grid(row=0, column=3)
        #Row 1 
        spell_search_entry.grid(row=1, column=0)
        spell_level_combobox.grid(row=1, column=1)
        spell_school_combobox.grid(row=1, column=2)
        spell_class_combobox.grid(row=1, column=3)
        spell_search_btn.grid(row=1,column=4)

        #Middle Frame
        #Row 1
        spell_highlighted_label.grid(row=0, column=0, sticky="e")
        spell_selected_label.grid(row=0, column=1, sticky="w")
        spell_add_btn.grid(row=0, column=2)

        #Bottom Frame
        #Row 0 
        spell_name_display.grid(row=0,column=0)
        spell_level_display.grid(row=0, column=1)
        spell_school_display.grid(row=0, column=2)
        spell_details_display.grid(row=0, column=3)
        #Row 1
        
        
     
        
        



