# 🌍 Overview
A Minecraft metal detector mod written in Python using <b>[Minescript](https://minescript.net/)</b> and <b>[mc-megascan](https://github.com/M4elstr0m/mc-megascan/)</b> that helps you locate ores in-game. It has a strong docstring within its source code, maintaining readability and accessibility for anyone aiming to use it in their projects.<br>

This was conceived for Minescript v4.0

## <p align="center">Please star this repository if you find it useful ⭐</p>

### ⚠️ <ins>Disclaimer</ins>

#### Using this script outside of your own server is considered <b>cheating</b>. You must ask the administrators for authorization before using such scripts online.
I am <b>not responsible</b> of your usage of the mc-MetalDetector, keep in mind that this should not be allowed in multiplayer and will be considered as X-ray.
<br> 
### 🛑 Use it at your own risks.

## 📦 Installation

1. Follow installation instructions for <b>[mc-megascan](https://github.com/M4elstr0m/mc-megascan/)</b>
2. Put the `metaldetector.py` file into your `minescript` folder, where your mc-megascan file (`megascan.py`) is also located
3. You can now run the MetalDetector in-game using the command `\metaldetector` with <b>[Minescript](https://minescript.net/)</b> installed

## 📚 Usage

Run this script in Minecraft by typing `\metaldetector` in the chat. Notice that this is a backslash "\\" not an usual slash "/"

##
Displays the generic help message

```bash
\metaldetector help
```

Overall basic usage is split in 3 arguments: the `command`, the `mode` and the `ore`

```bash
\metaldetector <command> <mode> <ore>
```

For now, there is only one possible `command` which is `start`, so every use of the MetalDetector should begin like following <br> *Note that you could also replace `start` by `s`*

```bash
\metaldetector start <mode> <ore>
```

Then there are 3 different `modes` that modifies the behavior of the MetalDetector:

- `check` : It will check for a specific ore in your area one time, then will stop. Mostly used to perform a quick single check-up of your area
  
- `radar` : It will keep checking for a specific ore around you until you press a *keybind* (`CTRL + M` by default). If you get too far from a detected ore, this ore will not show-up
  
- &nbsp;`map`&nbsp;&nbsp; : Same as the `radar` mode, but will keep in memory ores that were previously within range, until you mine it of course. Useful when travelling at high speed for example

So the command will be composed as following

```bash
\metaldetector start check <ore>

\metaldetector start radar <ore>

\metaldetector start map <ore>
```

Each mode has a "shortcut" version of itself; For example, the `check` mode could also be written as `c`, `1` or `single`

```bash
\metaldetector s c <ore>
```

Shortcut versions of `modes`:

- `check` : `c` , `1` , `single`
  
- `radar` : `r` , `2`
  
- &nbsp;`map`&nbsp;&nbsp; : `m` , `3` , `memory`

And last but not least, you will have to specify an `ore` to search for, or an array of ores

```bash
\metaldetector s c diamond
```

Like the other arguments, there are shortcuts versions and/or aliases for each `ore` <br> *Those are generally speaking the three first characters of the `ore` (e.g: `diamond` could be written `dia`)*

Shortcut versions of `ores`:

- `coal` : `coa`
  
- `copper` : `cop`
  
- `diamond` : `dia`
  
- `emerald` : `eme`
  
- `gold` : `gol`
  
- `iron` : `iro`
  
- `lapis` : `lap` , `lazuli`
  
- `netherite` : `net` , `ancient` , `anc` , `debris`
  
- `quartz` : `qua`
  
- `redstone` : `red`

- `overworld` : *None*
  
- `nether` : *None*

As you can see, you can also specify a dimension so it will only scan for `ores` that are generated in this specific dimension

```
\metaldetector s c overworld
```

By default, leaving an argument with a blank value after the `start` command will lead to the MetalDetector searching for netherite a single time ;)

All those default values and settings can be changed anytime at the <b>[line 255](https://github.com/M4elstr0m/mc-MetalDetector/blob/main/metaldetector.py#L225)</b> of the `metaldetector.py`

To search for anything else than ores, please use <b>[mc-megascan](https://github.com/M4elstr0m/mc-megascan/)</b>

## 🖼️ Gallery

<details>
  <summary>Screenshot of a player using the MetalDetector on `radar` to find coal</summary>
  <img width="1430" height="1079" alt="mc-metaldetector_gallery-1" src="https://github.com/user-attachments/assets/6e5059a1-83bc-46c7-810a-1f4ca0394f28" />
</details>

## 🗒️ Credits

<b>[M4elstr0m](https://github.com/M4elstr0m)</b> for conceiving this script (<b>mc-MetalDetector</b>) you are currently consulting on Github

<b>[maxuser](https://github.com/maxuser0)</b> for creating the wonderful <b>[Minescript](https://minescript.net/)</b> mod

All the people who starred one of my repositories
