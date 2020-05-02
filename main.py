import random
import time
import re
import json
from battle_sim import battle_sim

def handle_ui():
    print(battle_sim.utils.text.cyan("___________________"))
    print(f"Health: {battle_sim.utils.text.cyan(battle_sim.player.health)}")
    print(f"Magic: {battle_sim.utils.text.cyan(battle_sim.player.magic)}")
    print(f"Mana: {battle_sim.utils.text.cyan(battle_sim.player.mana)}")
    print(f"Resistance: {battle_sim.utils.text.cyan(battle_sim.player.resistance)}")
    print(f"Skills: {battle_sim.utils.text.cyan(battle_sim.player.skills)}")
    print(f"Speed: {battle_sim.utils.text.cyan(battle_sim.player.speed)}")
    print(f"Stamina: {battle_sim.utils.text.cyan(battle_sim.player.stamina)}")
    print(f"Strength: {battle_sim.utils.text.cyan(battle_sim.player.strength)}")
    print(battle_sim.utils.text.cyan("___________________"))
    print(f"Level: {battle_sim.utils.text.cyan(battle_sim.player.level)}")
    print(f"Xp: {battle_sim.utils.text.cyan(battle_sim.player.xp)}")
    print(battle_sim.utils.text.cyan("___________________"))

def handle_skill(magic_name):
    player = battle_sim.utils.json.save_data
    with open ("BattleSim/Utils/Skills.json") as file:
        skills = json.load(file)

    for effect in skills["Frost"]["properties"]["trigger"]["effects"]:
        try:
            attributes = effect.split(".")

            if attributes[2] == "add":
                if attributes[0] == "player":
                    battle_sim.utils.json.save_data[str(battle_sim.player.player_id)][str(attributes[1])] += skills["Frost"]["properties"]["trigger"]["effects"][effect]

                    battle_sim.utils.dump_save()
            
            if attributes[2] == "remove":
                if attributes[0] == "player":
                    battle_sim.utils.json.save_data[str(battle_sim.player.player_id)][str(attributes[1])] -= skills["Frost"]["properties"]["trigger"]["effects"][effect]

                    battle_sim.utils.dump_save()

            if attributes[2] == "set":
                if attributes[0] == "player":
                    battle_sim.utils.json.save_data[str(battle_sim.player.player_id)][str(attributes[1])] = skills["Frost"]["properties"]["trigger"]["effects"][effect]

                    battle_sim.utils.dump_save()

            if attributes[2] == "push":
                if attributes[0] == "player":
                    battle_sim.utils.json.save_data[str(battle_sim.player.player_id)][str(attributes[1])] += skills["Frost"]["properties"]["trigger"]["effects"][effect]

                    battle_sim.utils.dump_save()

            if attributes[2] == "pull":
                if attributes[0] == "player":
                    battle_sim.utils.json.save_data[str(battle_sim.player.player_id)][str(attributes[1])] += skills["Frost"]["properties"]["trigger"]["effects"][effect]

                    battle_sim.utils.dump_save()
        except:
            pass
def handle_begin():
    handle_ui()
    handle_skill("Frost")
    handle_ui()

def handle_new_save():

    print("Now creating a new save file, please", battle_sim.utils.text.cyan("wait"), "the new save proccess will be finished", battle_sim.utils.text.cyan("momentarily"), "!")

    tmp_id = 0
    while str(tmp_id) in battle_sim.utils.json.save_data:
        tmp_id += 1

    print("We found you a new", battle_sim.utils.text.cyan("id"), "! Your new id number is", battle_sim.utils.text.cyan(tmp_id),"! Please make sure to", battle_sim.utils.text.cyan("not"), "forgot it!")

    print("Now finished the player creation proccess, sending you to", battle_sim.utils.text.cyan("main game"), "!")

    battle_sim.player.player_id = str(tmp_id)
    battle_sim.player.utils.dump_save()

    battle_sim.player.utils.save_data = battle_sim.utils.json.save_data[str(tmp_id)]
    handle_begin()

def handle_load_save():

    print("To load a save file, provide us with an", battle_sim.utils.text.cyan("id"),"!")
    console = input(battle_sim.utils.text.cyan(">> "))
    
    if console in battle_sim.utils.json.save_data:
        print("Great, you're all loaded up! Let's", battle_sim.utils.text.cyan("begin"), "shall we?")
        battle_sim.player.utils.save_data = battle_sim.utils.json.save_data[console]
        battle_sim.player.player_id = console
        handle_begin()

    else:
        print("We couldn't find a save file with id", battle_sim.utils.text.cyan(console), ".. would you like to", battle_sim.utils.text.cyan("load"), "a different save file", battle_sim.utils.text.cyan("id"), "or would you like to create a", battle_sim.utils.text.cyan("new"), "save file?")
        console = input(battle_sim.utils.text.cyan(">> "))

        if re.match(r"\s*[nNeEwW\s*]+\s*",console):
            handle_new_save()
        else:
            handle_load_save()

def handle_start():
    print("Welcome to the", battle_sim.utils.text.cyan("BattleSimulator"), "!")
    print("Would you like to load a save?")
    console = input(battle_sim.utils.text.cyan(">> "))

    if re.match(r"\s*[nNoO\s*]+\s*", console):
        handle_new_save()
    else:
        handle_load_save()

handle_start()

battle_sim.utils.handle_exit()