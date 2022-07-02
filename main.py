from libraries import *
import customtkinter as ctk

#Main Class
class Window(ctk.CTk):
    WIDTH = 700 
    HEIGHT = 600
    
    def __init__(self) -> None:
        super().__init__()
    
        self.geometry(f"{Window.WIDTH}x{Window.HEIGHT}")
        self.title("Monster Maker")

#-----------------#
#Setup Frames-----#
#-----------------#
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

#------------#
#Entries-----#
#------------#
        #Monster Name
        monster_name_entry = ctk.CTkEntry(master=self.frame_left, placeholder_text='Enter Name')
        monster_name = monster_name_entry.get()

#-----------#
#Labels-----#
#-----------#
        #Left Frame Labels
        monster_name_label = ctk.CTkLabel(master=self.frame_left, text="Monster Name")
        size_label = ctk.CTkLabel(master=self.frame_left, text="Size Option")
        monster_type_label = ctk.CTkLabel(master=self.frame_left, text="Monster Type Option")
        ac_type_label = ctk.CTkLabel(master=self.frame_left, text="AC Type Option")
        ac_value_label = ctk.CTkLabel(master=self.frame_left, text="AC Value Option")
        hp_pool_label = ctk.CTkLabel(master=self.frame_left, text="HP Pool Option")
        hp_value_label = ctk.CTkLabel(master=self.frame_left, text="Hp Value Option")
        move_speed_label = ctk.CTkLabel(master=self.frame_left, text="Base Move Speed Option")
        extra_move_type_label = ctk.CTkLabel(master=self.frame_left, text="Extra Move Type Option")
        extra_move_speed_label = ctk.CTkLabel(master=self.frame_left, text="Extra Move Speed Option")
        str_label = ctk.CTkLabel(master=self.frame_left, text="STR Option")
        dex_label = ctk.CTkLabel(master=self.frame_left, text="DEX Option")
        con_label = ctk.CTkLabel(master=self.frame_left, text="CON Option")
        int_label = ctk.CTkLabel(master=self.frame_left, text="INT Option")
        wis_label = ctk.CTkLabel(master=self.frame_left, text="WIS Option")
        cha_label = ctk.CTkLabel(master=self.frame_left, text="CHA Option")
        skills_label = ctk.CTkLabel(master=self.frame_left, text="Skills Option")
        skills_value_label = ctk.CTkLabel(master=self.frame_left, text="Skills Value Option")
        vuln_label = ctk.CTkLabel(master=self.frame_left, text="Vulnerability Option")
        immune_label = ctk.CTkLabel(master=self.frame_left, text="Immunity Option")
        cond_immune_label = ctk.CTkLabel(master=self.frame_left, text="Condition Immunity Option")
        resist_label = ctk.CTkLabel(master=self.frame_left, text="Resistance Option")
        legendary_resist_label = ctk.CTkLabel(master=self.frame_left, text="Legendary Res. Option")
        senses_label = ctk.CTkLabel(master=self.frame_left, text="Senses Option")
        sense_value_label = ctk.CTkLabel(master=self.frame_left, text="Sense Value Option")
        lang_label = ctk.CTkLabel(master=self.frame_left, text="Languages Option")
        special_traits_label = ctk.CTkLabel(master=self.frame_left, text="Special Traits Option")
        action_label = ctk.CTkLabel(master=self.frame_left, text="Actions Option")
        legendary_action_label = ctk.CTkLabel(master=self.frame_left, text="Legendary Actions Option")
        lair_action_label = ctk.CTkLabel(master=self.frame_left, text="Lair Actions Option")
        spells_label = ctk.CTkLabel(master=self.frame_left, text="Spells Option")

        
        #Right Frame Labels
        monster_name_display = ctk.CTkLabel(master=self.frame_right, text='')
        size_display = ctk.CTkLabel(master=self.frame_right, text='')
        monster_type_display = ctk.CTkLabel(master=self.frame_right, text='')
        ac_type_display = ctk.CTkLabel(master=self.frame_right, text='')
        ac_value_display = ctk.CTkLabel(master=self.frame_right, text='')
        hp_pool_display = ctk.CTkLabel(master=self.frame_right, text='')
        hp_value_display = ctk.CTkLabel(master=self.frame_right, text='')
        move_speed_display = ctk.CTkLabel(master=self.frame_right, text='')
        extra_move_type_display = ctk.CTkLabel(master=self.frame_right, text='')
        extra_move_speed_display = ctk.CTkLabel(master=self.frame_right, text='')
        str_display = ctk.CTkLabel(master=self.frame_right, text='')
        dex_display = ctk.CTkLabel(master=self.frame_right, text='')
        con_display = ctk.CTkLabel(master=self.frame_right, text='')
        int_display = ctk.CTkLabel(master=self.frame_right, text='')
        wis_display = ctk.CTkLabel(master=self.frame_right, text='')
        cha_display = ctk.CTkLabel(master=self.frame_right, text='')
        skills_display = ctk.CTkLabel(master=self.frame_right, text='')
        skills_value_display = ctk.CTkLabel(master=self.frame_right, text='')
        vuln_display = ctk.CTkLabel(master=self.frame_right, text='')
        immune_display = ctk.CTkLabel(master=self.frame_right, text='')
        cond_immune_display = ctk.CTkLabel(master=self.frame_right, text='')
        resist_display = ctk.CTkLabel(master=self.frame_right, text='')
        legendary_resist_display = ctk.CTkLabel(master=self.frame_right, text='')
        senses_display = ctk.CTkLabel(master=self.frame_right, text='')
        sense_value_display = ctk.CTkLabel(master=self.frame_right, text='')
        lang_display = ctk.CTkLabel(master=self.frame_right, text='')
        special_traits_display = ctk.CTkLabel(master=self.frame_right, text='')
        action_display = ctk.CTkLabel(master=self.frame_right, text='')
        legendary_action_display = ctk.CTkLabel(master=self.frame_right, text='')
        lair_action_display = ctk.CTkLabel(master=self.frame_right, text='')
        spells_display = ctk.CTkLabel(master=self.frame_right, text='')

#---------------#        
#Comboboxes-----#
#---------------#
        #Size
        size_combobox = ctk.CTkComboBox(master=self.frame_left, values=size_options_combobox)
        size_combobox.set("Random")
        #Monster Type
        monster_type_combobox = ctk.CTkComboBox(master=self.frame_left, values=monster_type_options_combobox)
        monster_type_combobox.set("Random")
        #AC Type
        ac_type_combobox = ctk.CTkComboBox(master=self.frame_left, values=ac_type_options_combobox)
        ac_type_combobox.set("Random")
        #AC Value
        ac_value_combobox = ctk.CTkComboBox(master=self.frame_left, values=ac_value_options_combobox)
        ac_value_combobox.set("Random") 
        #TODO HP Pool
        hp_pool_combobox = ctk.CTkComboBox(master=self.frame_left, values='hp_pool_options_combobox')
        hp_pool_combobox.set("Random")
        #TODO HP Value
        hp_value_combobox = ctk.CTkComboBox(master=self.frame_left, values="hp_value_options_combobox")
        hp_value_combobox.set("Random")
        #Move Speed
        move_speed_combobox = ctk.CTkComboBox(master=self.frame_left, values=move_speed_options_combobox)
        move_speed_combobox.set("Random")
        #Extra Move Type
        extra_move_type_combobox = ctk.CTkComboBox(master=self.frame_left, values=extra_move_type_options_combobox)
        extra_move_type_combobox.set("Random")
        #Extra Move Speed
        extra_move_speed_combobox = ctk.CTkComboBox(master=self.frame_left, values=extra_move_speed_options_combobox)
        extra_move_speed_combobox.set("Random")
        #STR
        str_combobox = ctk.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        str_combobox.set("Random")
        #DEX
        dex_combobox = ctk.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        dex_combobox.set("Random")
        #CON
        con_combobox = ctk.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        con_combobox.set("Random")
        #INT
        int_combobox = ctk.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        int_combobox.set("Random")
        #WIS
        wis_combobox = ctk.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        wis_combobox.set("Random")
        #CHA
        cha_combobox = ctk.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        cha_combobox.set("Random")
        #Skills
        skill_combobox = ctk.CTkComboBox(master=self.frame_left, values=skill_options_combobox)
        skill_combobox.set("Random")
        #Skills Values
        skill_value_combobox = ctk.CTkComboBox(master=self.frame_left, values=skill_value_options_combobox)
        skill_value_combobox.set("Random")
        #Vulnerabilites
        vuln_combobox = ctk.CTkComboBox(master=self.frame_left, values=vuln_options_combobox)
        vuln_combobox.set("Random")
        #Immunities 
        immune_combobox = ctk.CTkComboBox(master=self.frame_left, values=immune_options_combobox)
        immune_combobox.set("Random")
        #Condition Immunities
        cond_immune_combobox = ctk.CTkComboBox(master=self.frame_left, values=cond_immune_options_combobox)
        cond_immune_combobox.set("Random")
        #Resistances
        resist_combobox = ctk.CTkComboBox(master=self.frame_left, values=resist_options_combobox)
        resist_combobox.set("Random")
        #Legendary Resistances 
        legendary_resist_combobox = ctk.CTkComboBox(master=self.frame_left, values=legendary_resist_options_combobox)
        legendary_resist_combobox.set("Random")
        #Sense
        sense_combobox = ctk.CTkComboBox(master=self.frame_left, values=sense_options_combobox)
        sense_combobox.set("Random")
        #Sense Value
        sense_value_combobox = ctk.CTkComboBox(master=self.frame_left, values=sense_value_options_combobox)
        sense_value_combobox.set("Random")
        #Languages
        lang_combobox = ctk.CTkComboBox(master=self.frame_left, values=lang_options_combobox)
        lang_combobox.set("Random")
        #Special Traits TODO
        special_trait_combobox = ctk.CTkComboBox(master=self.frame_left, values='special_trait_options_combobox')
        special_trait_combobox.set("Random")
        #Actions
        action_combobox = ctk.CTkComboBox(master=self.frame_left, values=action_options_combobox)
        action_combobox.set("Random")
        #Legendary Actions
        legendary_action_combobox = ctk.CTkComboBox(master=self.frame_left, values=legendary_action_options_combobox)
        legendary_action_combobox.set("Random")
        #Lair Actions
        lair_action_combobox = ctk.CTkComboBox(master=self.frame_left, values=lair_action_options_combobox)
        lair_action_combobox.set("Random")
        #Spells TODO
        spell_combobox = ctk.CTkComboBox(master=self.frame_left, values='spell_options_combobox')
        spell_combobox.set("Random")


#--------------#
#Functions-----#
#--------------#
        #Monster Name 
        create_monster_name(monster_name)
        #Size 
        size_command = lambda: add_size(size_combobox, size_display)
        #Monster Type
        monster_type_command = lambda: add_monster_type(monster_type_combobox, monster_type_display)

#------------#
#Buttons-----#
#------------#
        #Monster Name
        pass
        #Size
        add_size_btn = ctk.CTkButton(master=self.frame_left,command=size_command, text="+", width=30)
        #Monster Type
        add_monster_type_btn = ctk.CTkButton(master=self.frame_left, text="+", command=monster_type_command, width=30)

#----------------#        
#Grid Layout-----#
#----------------# 

#LEFT
        #Row 0
        monster_name_label.grid(row=0, column=0)
        monster_name_entry.grid(row=0, column=1)
        #Row 1 
        size_label.grid(row=1, column=0)
        size_combobox.grid(row=1, column=1)
        add_size_btn.grid(row=1, column=2, sticky = "W")
        #Row 2
        monster_type_label.grid(row=2,column=0)
        monster_type_combobox.grid(row=2, column=1)
        add_monster_type_btn.grid(row=2, column=2, sticky = "W")

#RIGHT
        #Column 0 Labels
        for index, row in enumerate(monster_stat_list): 
            monster_stats_label = ctk.CTkLabel(master=self.frame_right, text=row + ":")
            monster_stats_label.grid(row=index, column=0,padx=1,pady=1, sticky="w")
        #Row 0
        monster_name_display.grid(row=0,column=1)
        #Row 1
        size_display.grid(row=1,column=1)
        #Row 2 
        monster_type_display.grid(row=2,column=1)


        
#Main Loop
if __name__ == "__main__":
    window = Window()
    window.mainloop()