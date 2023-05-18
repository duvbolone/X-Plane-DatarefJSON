import json


with open("DataRefs.txt", "r") as f:
    datarefs = f.readlines()

datarefs_json = {}

for i, dataref in enumerate(datarefs):
    print(f"@dataref {i+1}/{len(datarefs)}: " + dataref.split('\t')[0])
    dref = dataref.split("\t")
    dref = [i for i in dref if i]

    if len(dataref.split('\t')) == 2:
        datarefs_json.update({
            dataref.split('\t')[0]: {
                "path":dataref.split("\t")[0],
            }
        })
    if len(dataref.split('\t')) == 3:
        datarefs_json.update({
            dataref.split('\t')[0]: {
                "path":dataref.split("\t")[0],
                "type":dataref.split("\t")[1],
            }
        })
    if len(dataref.split('\t')) == 4:
        writable = True if dataref.split("\t")[2] == "n" else False
        datarefs_json.update({
            dataref.split('\t')[0]: {
                "path":dataref.split("\t")[0],
                "type":dataref.split("\t")[1],
                "writable":writable,
            }
        })
    if len(dataref.split('\t')) == 5:
        writable = True if dataref.split("\t")[2] == "n" else False
        datarefs_json.update({
            dataref.split('\t')[0]: {
                "path":dataref.split("\t")[0],
                "type":dataref.split("\t")[1],
                "writable":writable,
                "unit":dataref.split("\t")[3],
            }
        })
    if len(dataref.split('\t')) == 6:
        writable = True if dataref.split("\t")[2] == "n" else False
        datarefs_json.update({
            dataref.split('\t')[0]: {
                "path":dataref.split("\t")[0],
                "type":dataref.split("\t")[1],
                "writable":writable,
                "unit":dataref.split("\t")[3],
                "description":dataref.split("\t")[4]
            }
        })

with open("json_files/datarefs.json", "w") as f:
    json.dump(datarefs_json, f, indent=4)


print("Succesfully made converted to JSON!")