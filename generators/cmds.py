import datetime
from generators.utils import progressbar


def generate_commands(input: str, version: str) -> dict:
    with open(input, "r") as f:
        commands = f.readlines()

    dt = datetime.datetime.now(datetime.UTC)
    commands_json = {
        "version": version,
        "time": dt.strftime("%Y-%m-%YT%H:%M:%SZ"),
        "commands": {}
    }

    for i, command in enumerate(commands):
        if not command.startswith("sim"):
            continue
        
        ratio = (i+1)/len(commands)*100
        print(f"@\033[34mcommand\033[32m {progressbar(ratio)} \033[0m{round(ratio)}% ({i+1}/{len(commands)})                  ", end="\r")
        cmd = command.split(" ")
        cmd = [i for i in cmd if i]
        desc = [a for i,a in enumerate(cmd) if (i != 0)]
        desc[len(desc)-1] = desc[len(desc)-1][:-1]
        name = command.split(' ')[0]
        commands_json["commands"].update({
            name: {
                "name":name,
                "description":' '.join(desc)
            }}
        )

    print("")

    return commands_json