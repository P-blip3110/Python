import json

def dict_to_json(dict_data):
    json_data = json.dumps(dict_data, indent=4)
    print (json_data)
    return 'executed'
    pass

dict_to_json({'a': 1, 'b': 2, 'c': 3})