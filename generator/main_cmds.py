import json


with open("Commands.txt", "r") as f:
    commands = f.readlines()

commands_json = {}

for i, command in enumerate(commands):
    print(f"@command {i+1}/{len(commands)}: " + command.split(' ')[0])
    cmd = command.split(" ")
    cmd = [i for i in cmd if i]
    desc = [a for i,a in enumerate(cmd) if (i != 0)]
    desc[len(desc)-1] = desc[len(desc)-1][:-1]

    commands_json.update({
        command.split(' ')[0]: {
            "name":command.split(" ")[0],
            "description":' '.join(desc)
        }
    })

with open("json_files/commands.json", "w") as f:
    json.dump(commands_json, f, indent=4)


print("Succesfully made converted to JSON!")