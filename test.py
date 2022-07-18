#Setup the score to modifier formula
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
def calculate_score_modifier(ability_score, modifier_dict):
    if ability_score == "0" or ability_score == "1":
        mod = modifier_dict["0"]
        print(mod)
    elif ability_score == "2" or ability_score == "3":
        mod = modifier_dict["2"]
        print(mod)
    elif ability_score == "4" or ability_score == "5":
        mod = modifier_dict["4"]
        print(mod)
    elif ability_score == "6" or ability_score == "7":
        mod = modifier_dict["6"]
        print(mod)
    elif ability_score == "8" or ability_score == "9":
        mod = modifier_dict["8"]
        print(mod)
    elif ability_score == "10" or ability_score == "11":
        mod = modifier_dict["10"]
        print(mod)
    elif ability_score == "12" or ability_score == "13":
        mod = modifier_dict["12"]
        print(mod)
    elif ability_score == "14" or ability_score == "15":
        mod = modifier_dict["14"]
        print(mod)
    elif ability_score == "16" or ability_score == "17":
        mod = modifier_dict["16"]
        print(mod)
    elif ability_score == "18" or ability_score == "19":
        mod = modifier_dict["18"]
        print(mod)
    elif ability_score == "20" or ability_score == "21":
        mod = modifier_dict["20"]
        print(mod)
    elif ability_score == "22" or ability_score == "23":
        mod = modifier_dict["22"]
        print(mod)   
    elif ability_score == "24" or ability_score == "25":
        mod = modifier_dict["24"]
        print(mod) 
    elif ability_score == "26" or ability_score == "27":
        mod = modifier_dict["26"]
        print(mod)
    elif ability_score == "28" or ability_score == "29":
        mod = modifier_dict["28"]
        print(mod)
    elif ability_score == "30":
        mod = modifier_dict["30"]
        print(mod)
calculate_score_modifier("31", modifier_dict)
