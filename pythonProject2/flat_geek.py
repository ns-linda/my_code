Input ={
    "Key1": "Value1",
    "Key2": {
        "Key21": "Value21",
        "Key22": {
            "Key221": "Value221"
        }
    },
    "Key3": ["Value31", "Value32"]
}
result = {}

for key, val in Input.items():
    if len(val) > 0