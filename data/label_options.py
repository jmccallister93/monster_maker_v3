import random

#-----------------#
#-----LABELS------#
#-----------------#
#Monster Name
monster_name_options_label = ['Vampmirage',
                        'Soilbrute',
                        'Cavehound',
                        'Grievemask',
                        'The Hollow Body',
                        'The Jagged Glob',
                        'The Calm Creature',
                        'The Feral Assassin Leopard',
                        'The Mad Tomb Leopard',
                        'The Silver Berserker Freak',
                        'Terrordeviation',
                        'Glowghoul',
                        'Infernalling',
                        'Gasface',
                        'The Feline Freak',
                        'The Gruesome Glob',
                        'The Lone Weirdo',
                        'The Stalking Bane Wolf',
                        'The Burnt Doom Snake',
                        'The White-Eyed Doom Scorpion',
                        'Dreamcrackle',
                        'Caveghoul',
                        'Plaguepest',
                        'Flamestrike',
                        'The Haunting Abomination',
                        'The Bewitched Monstrosity',
                        'The Gross Howler',
                        'The Cold-Blooded Doom Phoenix',
                        'The Sapphire Cinder Cobra',
                        'The Ebon Army Fiend']
#Size
size_options_label = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
#Monster Type
monster_type_options_label = ["Aberration", "Beast", 
                        "Celestial", "Construct", "Dragon", 
                        "Elemental", "Fey", "Fiend", 
                        "Giant", "Humanoid", "Monstrosity", 
                        "Ooze", "Plant", "Undead"
                        ]
#AC Type                        
ac_type_options_label = ["Ancestral", "Magic", "Natural", "Worn"]

#AC Value
ac_value_options_label = [
                    "7","8","9","10",
                    "11","12","13","14",
                    "15","16","17","18",
                    "19","20","21","22",
                    "23","24","25","26",
                    ]

# #HP Value
# hp_value_options_label = random.randrange(2, 1000, 5)

#Move Speed
move_speed_options_label = [
                            "10 ft","20 ft","30 ft",
                            "40 ft","50 ft","60 ft",
                            "70 ft","80 ft","90 ft",
                            "100 ft","110 ft","120 ft"
                            ]

#Extra Move Type
extra_move_type_options_label = ["Burrow", "Climb", "Fly", "Swim"]

#Extra Move Speed
extra_move_speed_options_label = [ 
                            "10 ft","20 ft","30 ft",
                            "40 ft","50 ft","60 ft",
                            "70 ft","80 ft","90 ft",
                            "100 ft","110 ft","120 ft"
                            ]

#Stats
stats_options_label = [
            "1","2","3","4","5","6","7","8",
            "9","10","11","12","13",
            "14","15","16","17","18",
            "19","20","21","22","23",
            "24","25","26","27","28",
            "29","30",
        ]
#Skills
skill_type_options_label = ["Random","None","Acrobatics","Animal Handling",
                        "Arcana","Athletics","Deception",
                        "History","Insight","Intimidation",
                        "Investigation","Medicine","Nature",
                        "Perception","Performance","Persuasion",
                        "Religion","Sleight of Hand","Stealth",
                        "Survival",
                        ]

#Skills Value
skill_value_options_label = ["+1","+2","+3",
                            "+4","+5","+6",
                            "+7","+8",
                            "+9","+10"]

#Vulnerabilites
vuln_options_label = ["Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]

#Immunities
immune_options_label = ["Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]

#Condition Immunities
cond_immune_options_label = ["Blinded","Charmed",
                                "Deafened", "Frightened", "Grappled",
                                "Incapacitaed", "Paralyzed", "Petrified",
                                "Poisoned", "Prone", "Restrained",
                                "Stunned", "Unconscious", "Exhausted"]

#Resistances
resist_options_label = ["Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]

#Legendary Resistances 
legendary_resist_options_label = ["1", "2", "3",
                                "4", "5", "6", "7",
                                "8", "9", "10"]

#Senses
sense_type_options_label = ["Darkvision","Blindsight","Truesight","Tremorsense"]

#Senses Value
sense_value_options_label = [
                                "10 ft","20 ft","30 ft",
                                "40 ft","50 ft","60 ft",
                                "70 ft","80 ft","90 ft",
                                "100 ft","110 ft","120 ft"
                                ]

#Language
lang_options_label = ["Random","Common","Dwarvish",
                        "Elvish","Giant","Gnomish",
                        "Goblin","Halfling","Orc",
                        "Abyssal","Celestial","Deep Speech",
                        "Draconic","Infernal","Primordial",
                        "Sylvan","Undercommon"
                        ]

#Special Traits TODO
pass 

#Actions
action_options_label = ["Bite", "Bite & Shake","Call / Howl","Claw","Death from Above",
                                    "Head Butt","Mule Kick","Pounce","Roll over","Stomp","Swallow Whole",
                                    "Tail Slap" ,"Tentacle","Trample","Weapon (Appendage / Natural Weapons)",
                                    "Weapon (Blood)","Weapon (Breath / Spit)","Weapon (External Glands Spray)",
                                    "Weapon (Gaze)","Weapon (Saliva)" ,"Weapon (Scream / Howl / Roar)",
                                    "Weapon (Touch)" ,"Weapon (Web Spinners)"]

#Legendary Action
legendary_action_options_label = ["Difficult Terrain", "Obscure Sight",
                                            "Snaring", "Knockdown", "Lighting Change", 
                                            "Heal Dampening", "Spell Dampening", "Effect on Enter",
                                            "Effect on Exit", "Free Action", "Free Reaction",
                                            "Free Spell", "Free Ability"]

#Lair Action
lair_action_options_label = ["Difficult Terrain", "Obscure Sight",
                                            "Snaring", "Knockdown", "Lighting Change", 
                                            "Heal Dampening", "Spell Dampening", "Effect on Enter",
                                            "Effect on Exit", "Free Action", "Free Reaction",
                                            "Free Spell", "Free Ability"]

#Spells TODO
spell_options_label = ["Fireball"]    

#-----------------------------#
#---Labels for Right Frame----#
#-----------------------------#
monster_stat_list = [
                        "Monster Name",
                        "Size",
                        "Monster Type",
                        "AC Type",
                        "AC",
                        "HP",
                        "Speed",
                        "Extra Move Type",
                        "STR",
                        "DEX",
                        "CON",
                        "INT",
                        "WIS",
                        "CHA",
                        "Skills",
                        "Vulnerabilities",
                        "Immunities",
                        "Condition Immunities",
                        "Resistances",
                        "Legendary Resistances",
                        "Senses",
                        "Languages",
                        "Special Traits",
                        "Actions",
                        "Legendary Actions",
                        "Lair Actions",
                        "Spells"
                    ]