"""
This is not a Python module.
This is designed to be run using Minescript.

 █▀▀ █▀█ █▀▀ █▀▄ █ ▀█▀ █▀\n
 █▄▄ █▀▄ ██▄ █▄▀ █ ░█░ ▄█

M4elstr0m (https://github.com/M4elstr0m) for conceiving this script (MetalDetector) you are currently reading and also for the Megascan module, used in this script

maxuser (https://github.com/maxuser0) for creating the wonderful Minescript mod

Refer to README.md for more user-friendly explanations

"""

from megascan import * # to parse Minecraft blocks using Minescript

import argparse # for in-game arguments parsing
import keyboard as kb # to implement the exit script feature using keybind

###

def __leaving():
    """
    Displays an exit message
    """

    ms.echo_json(
            {
                "text":"",
                "extra": [
                {
                        "text": f"Metal Detector: ",
                        "color": "#0b9411",
                        "bold": True
                },
                {
                        "text": f"Leaving...",
                        "color": "#afe49e",
                        "bold": False
                }
                ]
            }
        )

def __Deadstop():
    """
    Triggers the Deadswitch, allowing the script to stop
    """

    global Deadswitch
    Deadswitch = False
    __leaving()
    if debug:
        debug_echo("deadswitch triggered")

def __nothingwasfound():
    """
    Displays the message that will show up when no ore was found
    """

    ms.echo_json(
            {
                "text":"",
                "extra": [
                {
                        "text": f"Metal Detector: ",
                        "color": "#0b9411",
                        "bold": True
                },
                {
                        "text": f"{orename}\n",
                        "color": "#afe49e",
                        "bold": False
                },
                {
                        "text": f"Nothing was found",
                        "color": "#afe49e",
                        "bold": True
                }
                ]
            }
        )

def __howtoleave():
    """
    Displays the help about leaving the script (how to trigger the Deadswitch)
    """
    ms.echo_json(
            {
                "text":"",
                "extra": [
                {
                        "text": f"Metal Detector: ",
                        "color": "#0b9411",
                        "bold": True
                },
                {
                        "text": f"Press '{str.upper(keybind)}' key to leave",
                        "color": "#afe49e",
                        "bold": False
                }
                ]
            }
        )

def __help():
    """
    Displays the generic help tips and exit()
    """
    ms.echo_json(
            {
                "text":"",
                "extra": [
                {
                        "text": f"Metal Detector: ",
                        "color": "#0b9411",
                        "bold": True
                },
                {
                        "text": f"Help and Usage ",
                        "color": "#afe49e",
                        "bold": False
                },
                {
                        "text": f"by M4elstr0m\n",
                        "color": "#0b9411",
                        "bold": True
                },
                {
                        "text": f"Basic usage: \\metaldetector <command> <mode> <ore>\n",
                        "color": "#afe49e",
                        "bold": True
                },
                {
                        "text": f"Example: \\metaldetector start radar iron\n",
                        "color": "#afe49e",
                        "bold": False
                },
                {
                        "text": f"\n<command>:\nstart: starts a scan\n",
                        "color": "#afe49e",
                        "bold": False
                },
                {
                        "text": f"\n<mode>:\ncheck: scans one time and stops\nradar: keeps scanning around the player without remembering anything from the previous scans\nmap: keeps scanning around the player and keeps previous scans in memory, so detected ores will keep showing up until they are broken\n",
                        "color": "#afe49e",
                        "bold": False
                },
                {
                        "text": f"\n<ore>:\nMust be an ore name, for e.g 'Diamond', or its first three letters, e.g 'Dia'\n",
                        "color": "#afe49e",
                        "bold": False
                },
                {
                        "text": f"\nPress {str.upper(keybind)} to stop any running loops",
                        "color": "#afe49e",
                        "bold": True
                }
                ]
            }
        )
    exit()

def __matchore(name:str) -> tuple[str, list[str]]:
    """
    Returns the generic name and blocks ids from a given ore

    :param str name: A string value corresponding of an ore name

    :returns tuple(str, list[str]): A tuple containing ore's generic name and its ore(s) block(s) id(s)
    """

    blockids_dict:dict[str,list[str]] = {
        "coal" : ["minecraft:coal_ore","minecraft:deepslate_coal_ore"],
        "copper" : ["minecraft:copper_ore","minecraft:deepslate_copper_ore"],
        "diamond" : ["minecraft:diamond_ore", "minecraft:deepslate_diamond_ore"],
        "emerald" : ["minecraft:emerald_ore", "minecraft:deepslate_emerald_ore"],
        "gold" : ["minecraft:gold_ore", "minecraft:deepslate_gold_ore", "minecraft:nether_gold_ore"],
        "iron" : ["minecraft:iron_ore", "minecraft:deepslate_iron_ore"],
        "lapis" : ["minecraft:lapis_ore", "minecraft:deepslate_lapis_ore"],
        "netherite" : ["minecraft:ancient_debris"],
        "quartz" : ["minecraft:nether_quartz_ore", "minecraft:quartz_ore"],
        "redstone" : ["minecraft:redstone_ore[lit=false]", "minecraft:deepslate_redstone_ore[lit=false]", "minecraft:redstone_ore[lit=true]", "minecraft:deepslate_redstone_ore[lit=true]"]

    }
    
    possibilities:dict[tuple[str],tuple[str, list]] = {
        ("coa", "coal"): ("Coal", blockids_dict["coal"]),
        ("cop", "copper"): ("Copper", blockids_dict["copper"]),
        ("dia", "diamond"): ("Diamond", blockids_dict["diamond"]),
        ("eme", "emerald"): ("Emerald", blockids_dict["emerald"]),
        ("gol", "gold"): ("Gold", blockids_dict["gold"]),
        ("iro", "iron"): ("Iron", blockids_dict["iron"]),
        ("lap", "lapis", "lazuli"): ("Lapis Lazuli", blockids_dict["lapis"]),
        ("net", "anc", "netherite", "ancient", "debris"): ("Ancient Debris", blockids_dict["netherite"]),
        ("qua", "quartz") : ("Quartz", blockids_dict["quartz"]),
        ("red","redstone"): ("Redstone", blockids_dict["redstone"]),
        ("overworld"): ("Overworld Dimension", [block for ore in ["coal", "copper", "diamond", "emerald", "gold", "iron", "lapis", "redstone"] for block in blockids_dict[ore]]),
        ("nether"): ("Nether Dimension", [block for ore in ["gold", "netherite", "quartz"] for block in blockids_dict[ore]])
    }

    for key in possibilities:
        if name in key:
            return possibilities[key]
    return ("Ancient Debris", ["minecraft:ancient_debris"]) # default value

###############################
"""        Main Loop        """
###############################
parser = argparse.ArgumentParser(description="MetalDetector by M4elstr0m")

parser.add_argument("command", nargs="?", default=None, help="Main command: start")
"""\\metaldetector start"""

parser.add_argument("mode", nargs="?", default="check", help="Mode: check, radar, or map")
"""\\metaldetector start check"""

parser.add_argument("ore", nargs="?", default=None, help="Ore name from Minecraft (e.g: diamond, dia, netherite, net)")
"""\\metaldetector start check netherite"""

args = parser.parse_args()

###################################
""" Default values and settings """
###################################

keybind:str = "ctrl+m"
"""Keybind to leave the script"""

md_radius_x, md_radius_y, md_radius_z = 20, 2, 20
"""Radius value to scan"""

orename:str = "Ancient Debris"
"""Generic name of the ore you are searching for"""

blocks:list = ["minecraft:ancient_debris"]
"""Block(s) id(s) of the ore(s) you are searching for"""

mode:str = "check"
"""Running mode of the MetalDetector. MUST only take among those values: check, radar, map"""

"""                             """

if args.command: # check if command argument exists

    if args.command.lower() in ["start", "s"]:

        if args.mode: # check if mode argument exists

            if args.mode.lower() in ["c", "check", "1", "single"]:
                mode = "check"
            elif args.mode.lower() in ["r", "radar", "2"]:
                mode = "radar"
            elif args.mode.lower() in ["m", "map", "3","memory"]:
                mode = "map"

    else:
        __help()

else:
    __help()

if args.ore: # check if ore argument exists
    orename, blocks = __matchore(args.ore.lower())

    if debug:
        debug_echo(blocks)

if mode in ["radar", "map"]: # (if there is a while loop we must set up the Deadswitch)
    global Deadswitch
    Deadswitch:bool = True

    kb.add_hotkey(keybind, __Deadstop)

    __howtoleave()

### Script is starting its 'main' feature from this point

megascan:Megascan = Megascan()
"""Instance of Megascan for the MetalDetector"""

if mode == "radar": # radar mode (no memory mode)

    while Deadswitch:
        megascan.refresh(PlayerCoordinates(), radius_x=md_radius_x, radius_y=md_radius_y, radius_z=md_radius_z)
        """Erases current Megascan content and replaces it"""

        search:dict = megascan.reverse_search(blocks)
        """dictionary containing the search results for a given list of blocks"""
        
        if debug:
            debug_echo(search)

        if len(search) > 0:
            display_text:str = ""
            """Coordinates that will be shown in the chat as output"""
            
            for coor in search:
                display_text += f"{coor}\n"

            ms.echo_json({"text":"","extra": [{"text": f"Metal Detector: ","color": "#0b9411","bold": True},{"text": f"{orename}\n","color": "#afe49e","bold": False},{"text": f"{display_text}","color": "#afe49e","bold": False},{"text": f"{len(search)} {orename} found","color": "#afe49e","bold": True}]})

        else:
            __nothingwasfound()

        if not Deadswitch: # more frequent checks for Deadswitch allows script to stop earlier
            break

        time.sleep(9/2) # 9 seconds is the delay before the last chat message to clear out

        if not Deadswitch:
            break

        time.sleep(9/2)

elif mode == "map": # map mode (memory mode)

    while Deadswitch:
        megascan.extend(PlayerCoordinates(), radius_x=md_radius_x, radius_y=md_radius_y, radius_z=md_radius_z)

        search:dict = megascan.reverse_search(blocks)
        
        if debug:
            debug_echo(search)

        unmatching_were_found:int = 0
        """
        Counting system incrementing when a block from the Megascan content does'nt match with reality
        This is basically used with the 'map' mode since there will be changes to previous scans (for e.g if a block has been broken since the previous scan)
        """

        if len(search) > 0:
            display_text:str = ""
            
            for coor in search:
                realblock:str = ms.getblock(coor[0],coor[1],coor[2])
                if realblock in blocks:
                    display_text += f"{coor}\n"
                else:
                    search[coor] = realblock
                    unmatching_were_found += 1

            if unmatching_were_found > 0:
                megascan + search # It merges both. Please refer to Megascan docs ( ref: Megascan.__add__(): )

                if len(search)-unmatching_were_found > 0:
                    ms.echo_json({"text":"","extra": [{"text": f"Metal Detector: ","color": "#0b9411","bold": True},{"text": f"{orename}\n","color": "#afe49e","bold": False},{"text": f"{display_text}","color": "#afe49e","bold": False},{"text": f"{len(search)-unmatching_were_found} {orename} found","color": "#afe49e","bold": True}]})
                    # exotic echo that excludes the unmatching ones

                else:
                    __nothingwasfound()

            else:
                ms.echo_json({"text":"","extra": [{"text": f"Metal Detector: ","color": "#0b9411","bold": True},{"text": f"{orename}\n","color": "#afe49e","bold": False},{"text": f"{display_text}","color": "#afe49e","bold": False},{"text": f"{len(search)} {orename} found","color": "#afe49e","bold": True}]})
                # default one

        else:
            __nothingwasfound()

        if not Deadswitch:
            break

        time.sleep(9/2)

        if not Deadswitch:
            break
        
        megascan.extend(PlayerCoordinates(), radius_x=md_radius_x, radius_y=md_radius_y, radius_z=md_radius_z)
        # a more frequent scan to count more blocks at once, more precise results

        time.sleep(9/2)

else:  # check mode (single scan mode)

    megascan.refresh(PlayerCoordinates(), radius_x=md_radius_x, radius_y=md_radius_y, radius_z=md_radius_z)
    search:dict = megascan.reverse_search(blocks)

    if debug:
        debug_echo(search)

    if len(search) > 0:
        display_text:str = ""
        
        for coor in search:
            display_text += f"{coor}\n"

        ms.echo_json({"text":"","extra": [{"text": f"Metal Detector: ","color": "#0b9411","bold": True},{"text": f"{orename}\n","color": "#afe49e","bold": False},{"text": f"{display_text}","color": "#afe49e","bold": False},{"text": f"{len(search)} {orename} found","color": "#afe49e","bold": True}]})
    
    else:
        __nothingwasfound()


"""                      
 █▀▀ █▀█ █▀▀ █▀▄ █ ▀█▀ █▀
 █▄▄ █▀▄ ██▄ █▄▀ █ ░█░ ▄█

M4elstr0m (https://github.com/M4elstr0m) for conceiving this script (MetalDetector) you are currently reading and also for the Megascan module, used in this script

maxuser (https://github.com/maxuser0) for creating the wonderful Minescript mod

Refer to README.md for more user-friendly explanations

"""