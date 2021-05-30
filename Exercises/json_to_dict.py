import json

def json_to_dict(json_data):
    dict_data = json.loads(json_data)
    print (dict_data)
    return "executed"

json_to_dict('{"a": 1, "b": 2, "c": 3}')