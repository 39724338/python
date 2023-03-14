import json

data = {
    "dict": {
        "d1": "v1",
        "d2": None
    },
    "list": [1, 3.56, "12a", (33, -4.4)],
    "str": "str_value",
    "bool_t": True,
    "bool_f": False,
    "NON": None
}

json_data = json.dumps(data)##

print(type(json_data))
print(json_data)
print(data)
