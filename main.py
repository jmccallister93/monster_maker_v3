from libraries import *
import customtkinter as ctk


class Window(ctk.CTk):
    WIDTH = 700 
    HEIGHT = 600
    
    def __init__(self) -> None:
        super().__init__()
    
        self.geometry(f"{Window.WIDTH}x{Window.HEIGHT}")
        self.title("Monster Maker")

#Setup Frames-----#
        #Configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #Configure left frame
        self.frame_left = ctk.CTkFrame(master=self,width=180,corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=10,pady=10)
        #Configure right frame
        self.frame_right = ctk.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        #Far Left Frame
        self.frame_left.grid_rowconfigure(0, minsize=10)

#Labels-----#
        #Left Frame Labels
        size_label = ctk.CTkLabel(master=self.frame_left, text="Size Option:")
        monster_name_label = ctk.CTkLabel(master=self.frame_left, text="Monster Name:")
        #Right Frame Labels
        display_monster_name = ctk.CTkLabel(master=self.frame_right, text='')
        display_size = ctk.CTkLabel(master=self.frame_right, text='')

#Entries-----#
        #Monster Name
        monster_name_entry = ctk.CTkEntry(master=self.frame_left, placeholder_text='Enter Name')
        monster_name = monster_name_entry.get()
        
#Comboboxes-----#
        #Size
        size_combobox = ctk.CTkComboBox(master=self.frame_left, values=size_options_combobox)
        size_combobox.set("Random")

#Choice Vars-----#
        #Size
        size_choice = StringVar()
        size_choice = size_combobox.get()

#Functions-----#
        #Monster Name 
        create_monster_name(monster_name)
        #Size 
        size_command = add_size(size_combobox, display_size)

#Buttons-----#
        #Monster Name
        pass
        #Size
        add_size_btn = ctk.CTkButton(master=self.frame_left,command=size_command, text="+", width=30)
        
#Grid Layout-----#
#Left frame grid layout
        #Row 0
        monster_name_label.grid(row=0, column=0)
        monster_name_entry.grid(row=0, column=1)
        #Row 1 
        size_label.grid(row=1, column=0)
        size_combobox.grid(row=1, column=1)
        add_size_btn.grid(row=1, column=2, sticky = "W")

#Right frame grid layout
        #Column 0 Labels
        for index, row in enumerate(monster_stat_list): 
            monster_stats_label = ctk.CTkLabel(master=self.frame_right, text=row + ":")
            monster_stats_label.grid(row=index, column=0,padx=1,pady=1, sticky="w")
        #Row 0
        display_monster_name.grid(row=0,column=1)
        #Row 1
        display_size.grid(row=1,column=1)


        

if __name__ == "__main__":
    window = Window()
    window.mainloop()