import json

def load_patents(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_companies(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
