import datetime
from generators.utils import progressbar


def generate_datarefs(input: str, version: str) -> dict:
    with open(input, "r") as f:
        datarefs = f.readlines()

    dt = datetime.datetime.now(datetime.UTC)
    datarefs_json = {
        "version": version,
        "time": dt.strftime("%Y-%m-%YT%H:%M:%SZ"),
        "datarefs": {}
    }

    for i, dataref in enumerate(datarefs):
        if not dataref.startswith("sim"):
            continue

        ratio = (i+1)/len(datarefs)*100
        print(f"@\033[34mdataref\033[32m {progressbar(ratio)} \033[0m{round(ratio)}% ({i+1}/{len(datarefs)})                  ", end="\r")
        dref = dataref.split("\t")
        dref = [i for i in dref if i]

        if len(dataref.split('\t')) == 2:
            datarefs_json["datarefs"].update({
                dataref.split('\t')[0]: {
                    "path":dataref.split("\t")[0],
                }
            })
        if len(dataref.split('\t')) == 3:
            datarefs_json["datarefs"].update({
                dataref.split('\t')[0]: {
                    "path":dataref.split("\t")[0],
                    "type":dataref.split("\t")[1],
                }
            })
        if len(dataref.split('\t')) == 4:
            writable = True if dataref.split("\t")[2] == "n" else False
            datarefs_json["datarefs"].update({
                dataref.split('\t')[0]: {
                    "path":dataref.split("\t")[0],
                    "type":dataref.split("\t")[1],
                    "writable":writable,
                }
            })
        if len(dataref.split('\t')) == 5:
            writable = True if dataref.split("\t")[2] == "n" else False
            datarefs_json["datarefs"].update({
                dataref.split('\t')[0]: {
                    "path":dataref.split("\t")[0],
                    "type":dataref.split("\t")[1],
                    "writable":writable,
                    "unit":dataref.split("\t")[3],
                }
            })
        if len(dataref.split('\t')) == 6:
            writable = True if dataref.split("\t")[2] == "n" else False
            datarefs_json["datarefs"].update({
                dataref.split('\t')[0]: {
                    "path":dataref.split("\t")[0],
                    "type":dataref.split("\t")[1],
                    "writable":writable,
                    "unit":dataref.split("\t")[3],
                    "description":dataref.split("\t")[4]
                }
            })

    print("")

    return datarefs_json