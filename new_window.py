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

master = Window()

class NewWindow(ctk.CTkToplevel):
    def __init__(self, master = None):
        super().__init__(master=master)

        self.title("Spells")
        self.geometry("750x750")
#Frames
        #Configure grid layout (1x2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        #Configure Top Frame
        self.frame_top = ctk.CTkFrame(master=self,width=180,corner_radius=0)
        self.frame_top.grid(row=0, column=0, sticky="nswe", padx=10,pady=10)
        #Configure Bottom Frame
        self.frame_bottom = ctk.CTkFrame(master=self,width=10,corner_radius=0)
        self.frame_bottom.grid(row=1, column=0, sticky="nswe", padx=10,pady=10)

#Labels
        #Top Frame
        spell_search_label = ctk.CTkLabel(master=self.frame_top, text="Search")
        spell_level_label = ctk.CTkLabel(master=self.frame_top, text="Level")
        spell_school_label = ctk.CTkLabel(master=self.frame_top, text="School")
        spell_class_label = ctk.CTkLabel(master=self.frame_top, text="Class")
        spell_highlighted_label = ctk.CTkLabel(master=self.frame_top, text="Selected:")
        spell_selected_label = tk.Label(master=self.frame_top, text="", bg='#2c2c2c', fg='#ffffff')
        #Bottom Frame
        spell_name_display = ctk.CTkLabel(master=self.frame_bottom, text="Name")
        spell_level_display = ctk.CTkLabel(master=self.frame_bottom, text="Level")
        spell_school_display = ctk.CTkLabel(master=self.frame_bottom, text="School")
        spell_details_display = ctk.CTkLabel(master=self.frame_bottom, text="Description")
#Listbox
        #Update Listbox with list
        def update_listbox(data):
            #Clear list box
            spell_listbox.delete(0, tk.END)
            #Loop through list
            for item in data:
                spell_listbox.insert(tk.END, item)

        #Update entry box with listbox clicked
        def selected_item(event): 
            #Delete what in the entry box
            # spell_selected_label.update(0, tk.END)
            #Add clicked item to entry 
            spell_selected_label['text'] = spell_listbox.get(tk.ACTIVE)

        #Check Listbox from typed word
        def check(event):
            typed = spell_search_entry.get()
            if typed == "":
                data = spell_name_options_label
            else:
                data = []
                for item in spell_name_options_label:
                    if typed.lower() in item.lower():
                        data.append(item)
            #Update list with what is typed
            update_listbox(data)

        #Create Listbox
        spell_listbox = tk.Listbox(master=self.frame_bottom, width=100, bg="#36454F", fg='#ffffff')
        spell_listbox.grid(row=1, column=0, columnspan=4)
        update_listbox(spell_name_options_label)

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
        spell_search_command = lambda: spell_search()
        

#Buttons
        spell_search_btn = ctk.CTkButton(master=self.frame_top, text="Search", command=spell_search_command, width=50)

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
        spell_search_btn.grid(row=1, column=4)
        #Row 2
        spell_highlighted_label.grid(row=2, column=1, sticky="e")
        spell_selected_label.grid(row=2, column=2, sticky="w")

        #Bottom Frame
        #Row 0 
        spell_name_display.grid(row=0,column=0)
        spell_level_display.grid(row=0, column=1)
        spell_school_display.grid(row=0, column=2)
        spell_details_display.grid(row=0, column=3)
        #Row 1
        
        
     
        
        



