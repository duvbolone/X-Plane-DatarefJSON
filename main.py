import sys
import json
import os
import platform

from generators.cmds import generate_commands
from generators.drefs import generate_datarefs

def info(name, value):
    print(f"\t{name}: \033[1m{value}\033[0m")

def error(text):
    print(f"\033[31mERROR\033[0m: {text}")

def warn(text):
    print(f"\033[33mWARNING\033[0m: {text}")

def cinput(text):
    inp = input(f"{text}: \033[34;1m")
    print("\033[0m", end="")
    return inp

print("\033[94;1mX-Plane-DatarefJSON\n\033[0m")

indent = None
if "-I" in sys.argv:
    index = sys.argv.index("-I")
    try:
        indent = int(sys.argv[index+1])
    except:
        error("Invalid indent value!")

if indent or indent == 0:
    warn("You have set an indent value. While indented JSON improves readability, it significantly increases file sizes.")

system_name = platform.system().lower()
info("Platform", f"{system_name} ({platform.platform()})")

xplane_path = ""
xplane_version = 0
paths = []

if system_name == "windows":
    active_drives = []
    for letter in "ABDEFGHIJKLMNOPQRSTUVWXYZ":
        if os.path.exists(f"{letter}:\\"):
            active_drives.append(letter)

    paths = [
        r"C:\Program Files (x86)\Steam\steamapps\common",
        r"C:\Program Files (x86)\Steam\steamapps\common"
    ]

    for drive in active_drives:
        paths.append(rf"{drive}:\SteamLibrary\steamapps\common")

elif system_name == "darwin":
    paths = [
        os.path.expanduser("~/Library/Application Support/Steam/steamapps/common")
    ]
    

for path in paths:
    path12 = os.path.join(path, "X-Plane 12")

    if os.path.exists(path12):
        xplane_path = path12
        xplane_version = 12
        break

    path11 = os.path.join(path, "X-Plane 11")

    if os.path.exists(path11):
        xplane_path = path11
        xplane_version = 11
        break

if not xplane_path:
    error("No X-Plane path found!")
    xplane_path = cinput("Please enter your X-Plane installation path")
    if not os.path.exists(xplane_path):
        error("Directory not found.")
        exit(1)
    if not os.path.isdir(xplane_path):
        error("Not a directory.")
        exit(1)

    xplane_version = int(xplane_path.split()[-1])


info("X-Plane path", xplane_path)
info("X-Plane version", xplane_version)
print("")
plugins_path = os.path.join(xplane_path, "Resources", "plugins")
if not os.path.exists(plugins_path):
    error("No plugins folder found! Your X-Plane installation might be incomplete.")
    plugins_path = cinput("Please enter the path of the directory where 'DataRefs.txt' and 'Commands.txt' can be found")

datarefs_path = os.path.join(plugins_path, "DataRefs.txt")
if not os.path.exists(datarefs_path):
    error("No 'DataRefs.txt' found.")
    datarefs_path = cinput("If the file has a different name, then please enter its name (with extension)")
    if not os.path.exists(datarefs_path):
        error("File not found")
        exit(1)

commands_path = os.path.join(plugins_path, "Commands.txt")
if not os.path.exists(commands_path):
    error("No 'Commands.txt' found.")
    commands_path = cinput("If the file has a different name, then please enter its name (with extension)")
    if not os.path.exists(commands_path):
        error("File not found")
        exit(1)

try:
    full_version = ""
    
    with open(datarefs_path, "r") as f:
        content = f.readline()
        full_version = content.split()[1]
    
    datarefs = generate_datarefs(datarefs_path, full_version)
    commands = generate_commands(commands_path, full_version)

    with open("datarefs.json", "w") as f:
        f.write(json.dumps(datarefs, indent=indent))

    with open("commands.json", "w") as f:
        f.write(json.dumps(commands, indent=indent))

except PermissionError as e:
    error(f"Couldn't access to certain files:\n\n{e}")
    exit(1)
except FileNotFoundError as e:
    error(f"Couldn't find certain files:\n\n{e}")
    exit(1)
except Exception as e:
    error(f"Something went wrong:\n\n{e}")
    exit(1)

print("\n\033[32;1mSuccess!\033[0m")
print("Exported to 'datarefs.json' and 'commands.json'")