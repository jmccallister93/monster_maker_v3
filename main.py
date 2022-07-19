from libraries import *
import customtkinter as ctk
import tkinter as tk

#Main Class
class Window(ctk.CTk):
    WIDTH = 700 
    HEIGHT = 900
    
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

#-----------#
#Labels-----#
#-----------#
        #Left Frame Labels
        monster_name_label = ctk.CTkLabel(master=self.frame_left, text="Monster Name")
        size_label = ctk.CTkLabel(master=self.frame_left, text="Size Option")
        monster_type_label = ctk.CTkLabel(master=self.frame_left, text="Monster Type Option")
        ac_type_label = ctk.CTkLabel(master=self.frame_left, text="AC Type Option")
        ac_value_label = ctk.CTkLabel(master=self.frame_left, text="AC Value Option")
        hp_value_label = ctk.CTkLabel(master=self.frame_left, text="HP Value Option")
        move_speed_label = ctk.CTkLabel(master=self.frame_left, text="Base Move Speed Option")
        extra_move_type_label = ctk.CTkLabel(master=self.frame_left, text="Extra Move Type Option")
        extra_move_speed_label = ctk.CTkLabel(master=self.frame_left, text="Extra Move Speed Option")
        str_label = ctk.CTkLabel(master=self.frame_left, text="STR Option")
        dex_label = ctk.CTkLabel(master=self.frame_left, text="DEX Option")
        con_label = ctk.CTkLabel(master=self.frame_left, text="CON Option")
        int_label = ctk.CTkLabel(master=self.frame_left, text="INT Option")
        wis_label = ctk.CTkLabel(master=self.frame_left, text="WIS Option")
        cha_label = ctk.CTkLabel(master=self.frame_left, text="CHA Option")
        skill_type_label = ctk.CTkLabel(master=self.frame_left, text="Skills Option")
        skill_value_label = ctk.CTkLabel(master=self.frame_left, text="Skills Value Option")
        vuln_label = ctk.CTkLabel(master=self.frame_left, text="Vulnerability Option")
        immune_label = ctk.CTkLabel(master=self.frame_left, text="Immunity Option")
        cond_immune_label = ctk.CTkLabel(master=self.frame_left, text="Condition Immunity Option")
        resist_label = ctk.CTkLabel(master=self.frame_left, text="Resistance Option")
        legendary_resist_label = ctk.CTkLabel(master=self.frame_left, text="Legendary Res. Option")
        sense_type_label = ctk.CTkLabel(master=self.frame_left, text="Senses Option")
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
        hp_value_display = ctk.CTkLabel(master=self.frame_right, text='')
        move_speed_display = ctk.CTkLabel(master=self.frame_right, text='')
        extra_move_display = ctk.CTkLabel(master=self.frame_right, text='')
        str_display = tk.Label(master=self.frame_right, text='', bg='#2c2c2c', fg='#ffffff')
        dex_display = tk.Label(master=self.frame_right, text='', bg='#2c2c2c', fg='#ffffff')
        con_display = tk.Label(master=self.frame_right, text='', bg='#2c2c2c', fg='#ffffff')
        int_display = tk.Label(master=self.frame_right, text='', bg='#2c2c2c', fg='#ffffff')
        wis_display = tk.Label(master=self.frame_right, text='', bg='#2c2c2c', fg='#ffffff')
        cha_display = tk.Label(master=self.frame_right, text='', bg='#2c2c2c', fg='#ffffff')
        skill_display = ctk.CTkLabel(master=self.frame_right, text='')
        vuln_display = ctk.CTkLabel(master=self.frame_right, text='')
        immune_display = ctk.CTkLabel(master=self.frame_right, text='')
        cond_immune_display = ctk.CTkLabel(master=self.frame_right, text='')
        resist_display = ctk.CTkLabel(master=self.frame_right, text='')
        legendary_resist_display = ctk.CTkLabel(master=self.frame_right, text='')
        sense_display = ctk.CTkLabel(master=self.frame_right, text='')
        lang_display = ctk.CTkLabel(master=self.frame_right, text='')
        special_traits_display = ctk.CTkLabel(master=self.frame_right, text='')
        action_display = ctk.CTkLabel(master=self.frame_right, text='')
        legendary_action_display = ctk.CTkLabel(master=self.frame_right, text='')
        lair_action_display = ctk.CTkLabel(master=self.frame_right, text='')
        spells_display = ctk.CTkLabel(master=self.frame_right, text='')
#------------#
#Entries-----#
#------------#
        #Monster Name
        monster_name_entry = ctk.CTkEntry(master=self.frame_left, placeholder_text='Enter Name')
        #AC Value
        ac_value_entry = ctk.CTkEntry(master=self.frame_left, placeholder_text='Enter AC Value')
        #HP Value
        hp_value_entry = ctk.CTkEntry(master=self.frame_left, placeholder_text='Enter HP Value')
        #Move Speed
        move_speed_entry = ctk.CTkEntry(master=self.frame_left, placeholder_text='Enter Move Speed')
        #Extra Move Speed
        extra_move_speed_entry = ctk.CTkEntry(master=self.frame_left, placeholder_text='Enter Extra Move Speed')
        #Skill Value
        skill_value_entry = ctk.CTkEntry(master=self.frame_left, placeholder_text='Enter Skill Value')
        #Sense Value
        sense_value_entry = ctk.CTkEntry(master=self.frame_left, placeholder_text='Enter Sense Value')

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
        #Extra Move Type
        extra_move_type_combobox = ctk.CTkComboBox(master=self.frame_left, values=extra_move_type_options_combobox)
        extra_move_type_combobox.set("Random")
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
        skill_type_combobox = ctk.CTkComboBox(master=self.frame_left, values=skill_type_options_combobox)
        skill_type_combobox.set("Random")
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
        sense_type_combobox = ctk.CTkComboBox(master=self.frame_left, values=sense_type_options_combobox)
        sense_type_combobox.set("Random")
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
        monster_name_command = lambda: add_monster_name(monster_name_entry, monster_name_display)
        #Size 
        size_command = lambda: add_size(size_combobox, size_display)
        #Monster Type
        monster_type_command = lambda: add_monster_type(monster_type_combobox, monster_type_display)
        #AC Type
        ac_type_command = lambda: add_ac_type(ac_type_combobox, ac_type_display)
        #AC Value
        ac_value_command = lambda: add_ac_value(ac_value_entry, ac_value_display)
        #HP Value
        hp_value_command = lambda: add_hp_value(hp_value_entry, hp_value_display)
        #Move Speed
        move_speed_command = lambda: add_move_speed(move_speed_entry, move_speed_display)
        #Extra Move
        extra_move_list = []
        extra_move_command = lambda: add_extra_move(extra_move_type_combobox, extra_move_speed_entry, extra_move_display, extra_move_list)
        #STR
        str_command = lambda: add_stats(str_combobox, str_display, modifier_dict)
        #DEX
        dex_command = lambda: add_stats(dex_combobox, dex_display, modifier_dict)
        #CON
        con_command = lambda: add_stats(con_combobox, con_display, modifier_dict)
        #INT
        int_command = lambda: add_stats(int_combobox, int_display, modifier_dict)
        #WIS
        wis_command = lambda: add_stats(wis_combobox, wis_display, modifier_dict)
        #CHA
        cha_command = lambda: add_stats(cha_combobox, cha_display, modifier_dict)
        #Skills
        skill_list = []
        skill_command = lambda: add_skill(skill_type_combobox, skill_value_entry, skill_display, skill_list)
        #Vulnerabilites
        vuln_list = []
        vuln_command = lambda: add_vuln(vuln_combobox, vuln_display, vuln_list)
        #Immunities
        immune_list = []
        immune_command = lambda: add_immune(immune_combobox, immune_display, immune_list)
        #Condition Immunities
        cond_immune_list = []
        cond_immune_command = lambda: add_cond_immune(cond_immune_combobox, cond_immune_display, cond_immune_list)
        #Resistances 
        resist_list = []
        resist_command = lambda: add_resist(resist_combobox, resist_display, resist_list)
        #Legendary Resistances
        legendary_resist_command = lambda: add_legendary_resist(legendary_resist_combobox, legendary_resist_display)
        #Senses
        sense_list = []
        sense_command = lambda: add_sense(sense_type_combobox, sense_value_entry, sense_display, sense_list)
        #Languages
        lang_list = []
        lang_command =  lambda: add_lang(lang_combobox, lang_display, lang_list)

        #Remove Stat
        remove_stat_command = lambda: remove_stat(extra_move_list, 0)
        

#------------#
#Buttons-----#
#------------#
        #Monster Name
        add_monster_name_btn =ctk.CTkButton(master=self.frame_left,text="+", command=monster_name_command, width=30)
        #Size
        add_size_btn = ctk.CTkButton(master=self.frame_left,command=size_command, text="+", width=30)
        #Monster Type
        add_monster_type_btn = ctk.CTkButton(master=self.frame_left, text="+", command=monster_type_command, width=30)
        #AC Type
        add_ac_type_btn = ctk.CTkButton(master=self.frame_left, text="+", command=ac_type_command, width=30)
        #AC Value
        add_ac_value_btn = ctk.CTkButton(master=self.frame_left, text="+", command=ac_value_command, width=30)
        #HP 
        add_hp_value_btn = ctk.CTkButton(master=self.frame_left, text="+", command=hp_value_command, width=30)
        #Move Speed
        add_move_speed_btn = ctk.CTkButton(master=self.frame_left, text="+", command=move_speed_command, width=30)
        #Extra Move
        add_extra_move_btn = ctk.CTkButton(master=self.frame_left, text="+", command=extra_move_command, width=30)
        #STR
        add_str_btn = ctk.CTkButton(master=self.frame_left, text="+", command=str_command, width=30)
        #DEX
        add_dex_btn = ctk.CTkButton(master=self.frame_left, text="+", command=dex_command, width=30)
        #CON
        add_con_btn = ctk.CTkButton(master=self.frame_left, text="+", command=con_command, width=30)
        #INT
        add_int_btn = ctk.CTkButton(master=self.frame_left, text="+", command=int_command, width=30)
        #WIS
        add_wis_btn = ctk.CTkButton(master=self.frame_left, text="+", command=wis_command, width=30)
        #CHA
        add_cha_btn = ctk.CTkButton(master=self.frame_left, text="+", command=cha_command, width=30)
        #Skill
        add_skill_btn = ctk.CTkButton(master=self.frame_left, text="+", command=skill_command, width=30)
        #Vulnerabilites
        add_vuln_btn = ctk.CTkButton(master=self.frame_left, text="+", command=vuln_command, width=30)
        #Immunities
        add_immune_btn = ctk.CTkButton(master=self.frame_left, text="+", command=immune_command, width=30)
        #Condition Immunities
        add_cond_immune_btn = ctk.CTkButton(master=self.frame_left, text="+", command=cond_immune_command, width=30)
        #Resistances
        add_resist_btn = ctk.CTkButton(master=self.frame_left, text="+", command=resist_command, width=30)
        #Legendary Resistances
        add_legendary_resist_btn = ctk.CTkButton(master=self.frame_left, text="+", command=legendary_resist_command, width=30)
        #Senses
        add_sense_btn = ctk.CTkButton(master=self.frame_left, text="+", command=sense_command, width=30)
        #Language 
        add_lang_btn = ctk.CTkButton(master=self.frame_left, text="+", command=lang_command, width=30)

        #Remove Stat
        remove_stat_btn = ctk.CTkButton(master=self.frame_left, text="Remove Stat?", command=remove_stat_command, width=30)

#----------------#        
#Grid Layout-----#
#----------------# 

#LEFT
        #Row 0
        monster_name_label.grid(row=0, column=0)
        monster_name_entry.grid(row=0, column=1)
        add_monster_name_btn.grid(row=0, column=2)
        #Row 1 
        size_label.grid(row=1, column=0)
        size_combobox.grid(row=1, column=1)
        add_size_btn.grid(row=1, column=2, sticky = "W")
        #Row 2
        monster_type_label.grid(row=2, column=0)
        monster_type_combobox.grid(row=2, column=1)
        add_monster_type_btn.grid(row=2, column=2, sticky = "W")
        #Row 3 
        ac_type_label.grid(row=3, column=0)
        ac_type_combobox.grid(row=3, column=1)
        add_ac_type_btn.grid(row=3, column=2)
        #Row 4 
        ac_value_label.grid(row=4, column=0)
        ac_value_entry.grid(row=4, column=1)
        add_ac_value_btn.grid(row=4, column=2)
        #Row 5 
        hp_value_label.grid(row=5, column=0)
        hp_value_entry.grid(row=5, column=1)
        add_hp_value_btn.grid(row=5, column=2)
        #Row 6
        move_speed_label.grid(row=6, column=0)
        move_speed_entry.grid(row=6, column=1)
        add_move_speed_btn.grid(row=6, column=2)
        #Row 7
        extra_move_type_label.grid(row=7, column=0)
        extra_move_type_combobox.grid(row=7, column=1)
        #Row 8
        extra_move_speed_label.grid(row=8, column=0)
        extra_move_speed_entry.grid(row=8, column=1)
        add_extra_move_btn.grid(row=8, column=2)
        #Row 9 
        str_label.grid(row=9, column=0)
        str_combobox.grid(row=9, column=1)
        add_str_btn.grid(row=9, column=2)
        #Row 10
        dex_label.grid(row=10,column=0)
        dex_combobox.grid(row=10, column=1)
        add_dex_btn.grid(row=10, column=2)
        #Row 11
        con_label.grid(row=11,column=0)
        con_combobox.grid(row=11, column=1)
        add_con_btn.grid(row=11, column=2)
        #Row 12
        int_label.grid(row=12,column=0)
        int_combobox.grid(row=12, column=1)
        add_int_btn.grid(row=12, column=2)
        #Row 13
        wis_label.grid(row=13,column=0)
        wis_combobox.grid(row=13, column=1)
        add_wis_btn.grid(row=13, column=2)
        #Row 14
        cha_label.grid(row=14,column=0)
        cha_combobox.grid(row=14, column=1)
        add_cha_btn.grid(row=14, column=2)
        #Row 15
        skill_type_label.grid(row=15,column=0)
        skill_type_combobox.grid(row=15, column=1)
        #Row 16
        skill_value_label.grid(row=16,column=0)
        skill_value_entry.grid(row=16, column=1)
        add_skill_btn.grid(row=16, column=2)
        #Row 17
        vuln_label.grid(row=17,column=0)
        vuln_combobox.grid(row=17, column=1)
        add_vuln_btn.grid(row=17, column=2)
        #Row 18
        immune_label.grid(row=18, column=0)
        immune_combobox.grid(row=18, column=1)
        add_immune_btn.grid(row=18, column=2)
        #Row 19 
        cond_immune_label.grid(row=19, column=0)
        cond_immune_combobox.grid(row=19, column=1)
        add_cond_immune_btn.grid(row=19, column=2)
        #Row 20 
        resist_label.grid(row=20, column=0)
        resist_combobox.grid(row=20, column=1)
        add_resist_btn.grid(row=20, column=2)
        #Row 21 
        legendary_resist_label.grid(row=21, column=0)
        legendary_resist_combobox.grid(row=21, column=1)
        add_legendary_resist_btn.grid(row=21, column=2)
        #Row 22 
        sense_type_label.grid(row=22, column=0)
        sense_type_combobox.grid(row=22, column=1)
        #Row 23
        sense_value_label.grid(row=23, column=0)
        sense_value_entry.grid(row=23, column=1)
        add_sense_btn.grid(row=23, column=2)
        #Row 24 
        lang_label.grid(row=24, column=0)
        lang_combobox.grid(row=24, column=1)
        add_lang_btn.grid(row=24, column=2)


        remove_stat_btn.grid()

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
        #Row 3
        ac_type_display.grid(row=3, column=1)
        #Row 4 
        ac_value_display.grid(row=4, column=1)
        #Row 5 
        hp_value_display.grid(row=5, column=1)
        #Row 6 
        move_speed_display.grid(row=6, column=1)
        #Row 7
        extra_move_display.grid(row=7, column=1)
        #Row 8 
        str_display.grid(row=8, column=1)
        #Row 9 
        dex_display.grid(row=9, column=1)
        #Row 10 
        con_display.grid(row=10, column=1)
        #Row 11 
        int_display.grid(row=11, column=1)
        #Row 12 
        wis_display.grid(row=12, column=1)
        #Row 13 
        cha_display.grid(row=13, column=1)
        #Row 14
        skill_display.grid(row=14, column=1)
        #Row 15
        vuln_display.grid(row=15, column=1)
        #Row 16
        immune_display.grid(row=16, column=1)
        #Row 17 
        cond_immune_display.grid(row=17, column=1)
        #Row 18 
        resist_display.grid(row=18, column=1)
        #Row 19 
        legendary_resist_display.grid(row=19, column=1)
        #Row 20 
        sense_display.grid(row=20, column=1)
        #Row 21
        lang_display.grid(row=21, column=1)
        
        

#Main Loop
if __name__ == "__main__":
    window = Window()
    window.mainloop()