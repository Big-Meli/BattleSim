import random
import time
import re
import json
import asyncio
from termcolor import colored

class battle_sim:
    class utils:
        class json:
            def get():
                with open("BattleSim/SaveData/Players.json") as file:
                    battle_sim.utils.json.save_data = json.load(file)
                
            with open("BattleSim/SaveData/Players.json") as file:
                save_data = json.load(file)

        class text:
            def cyan(text):
                return colored(text, "cyan")
        class skills:
            data = ""
        def import_magic():
            with open("Utils/Skills.json", "r") as file:
                battle_sim.utils.skills = json.load(file)

        def handle_exit():
            print("Would you like to see", battle_sim.utils.text.cyan("statistics"), "about how your session went?")
            console = input(battle_sim.utils.text.cyan(">> "))

            if re.match(r"\s*[yYeEsS\s*]+\s*", console):
                print(battle_sim.utils.text.cyan("_______Statistics_______"))
                print("stat_header :", battle_sim.utils.text.cyan("stat_val"))
                print("stat_header :", battle_sim.utils.text.cyan("stat_val"))
                print("stat_header :", battle_sim.utils.text.cyan("stat_val"))
                print("stat_header :", battle_sim.utils.text.cyan("stat_val"))
                print("stat_header :", battle_sim.utils.text.cyan("stat_val"))
                print(battle_sim.utils.text.cyan("________________________"))
            else:
                print("In that case, in the event that something", battle_sim.utils.text.cyan("went wrong"), "and save data would be lost.. ", battle_sim.utils.text.cyan("saving"), "!")
                battle_sim.player.utils.dump_save()
                print("Saving has", battle_sim.utils.text.cyan("finished"), "! Goodbye!")
                quit()

    class player:
        class utils:
            def print_ui():
                pass
    
            def dump_save():
                global save_data
                
                if not battle_sim.player.player_id in battle_sim.utils.json.save_data:
                    battle_sim.utils.json.save_data[battle_sim.player.player_id] = {} 

                battle_sim.utils.json.save_data[battle_sim.player.player_id]["health"] = battle_sim.player.health
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["strength"] = battle_sim.player.strength
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["magic"] = battle_sim.player.magic
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["mana"] = battle_sim.player.mana
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["speed"] = battle_sim.player.speed
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["skills"] = battle_sim.player.magic
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["player_id"] = battle_sim.player.player_id
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["stamina"] = battle_sim.player.stamina
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["resistance"] = battle_sim.player.resistance
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["level"] = battle_sim.player.level
                battle_sim.utils.json.save_data[battle_sim.player.player_id]["xp"] = battle_sim.player.xp

                with open("BattleSim/SaveData/Players.json", "w") as file:
                    json.dump(battle_sim.utils.json.save_data, file, sort_keys=True, indent=4, separators=(',', ': '))

                with open("BattleSim/SaveData/Players.json") as file:
                    battle_sim.utils.json.save_data = json.load(file)
                    
        health = 10
        level = 1
        magic = []
        mana = 10
        player_id = None
        resistance = 10
        skills = []
        speed = 10
        stamina = 10
        strength = 10
        xp = 0

    class board:
        def lay_out():
            pass

    class game:
        pass