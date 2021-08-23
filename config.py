import json

def read_config():
    with open('config.json', 'r') as f:
        return json.loads(f.read())
