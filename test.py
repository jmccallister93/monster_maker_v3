import pandas as pd

spell_dict = {
    "Fireball":"https://www.dndbeyond.com/spells/fireball",
    "Alarm":"https://www.dndbeyond.com/spells/alarm",
    "Catapult":"https://www.dndbeyond.com/spells/catapult"
    }

def dict_value(dictionary):
    for key, value in dict.items():
        if key == "Fireball":
            print(value)

df = pd.DataFrame.from_dict(spell_dict)