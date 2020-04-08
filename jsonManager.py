import json

class JSONManager:
    def __init__(self):
        pass

    def writeJSON(self, content):
        with open('answer.json', 'w') as f:
            json.dump(content, f)

    def readJSON(self, file):
        with open(file, 'r') as f:
            return json.load(f)