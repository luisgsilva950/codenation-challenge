import requests

from jsonManager import JSONManager

myToken = "8a29b12785616a8e7b69e5179d2445c14f121873"
URL_BASE = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token="

response = requests.get(URL_BASE+myToken).json()
jsonManager = JSONManager()

jsonManager.writeJSON(str(response))

print("Response", response)