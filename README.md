# X-Plane-DatarefJSON

## All **X-Plane datarefs** and **commands** in **JSON** format.

## Format
All exported files are - as the project name says - converted in JSON format.

Example:
```json
{
    "version": "1208",
    "time": "2023-12-24T12:39:00Z",
    "datarefs": {
        "sim/world/boat/carrier_deck_height_mtr": {
            "path": "sim/world/boat/carrier_deck_height_mtr",
            "type": "float",
            "writable": false,
            "unit": "meters",
            "description": "Deck height of the carrier (in coordinates of the OBJ model)"
        },
    }
}
```
| Key                      | Description                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `version`                | The X-Plane version the datarefs come from. This information is taken from the top of the `DataRefs.txt` file. |
| `time`                   | When the JSON file was generated in ISO 8601 format (UTC).                                                     |
| `datarefs` or `commands` | Contains all the datarefs or commands depending on the file.                                                   |

> [!NOTE]
> Not all datarefs have every property (`type`, `type`, etc.) available. In the generated JSON file missing properties are simply dropped, so you should always check if the key exists before trying to access it.