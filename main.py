import json
import requests
import hashlib
from classes.alphabetManager import AlphabetManager
from classes.jsonManager import JSONManager

MY_TOKEN = "8a29b12785616a8e7b69e5179d2445c14f121873"
URL_GET = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token="
URL_SUBMIT = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token="

response = requests.get(URL_GET + MY_TOKEN).json()

jsonManager = JSONManager()
alphabetManager = AlphabetManager()

jsonManager.writeJSON(response)
cifrado = response['cifrado']
decifrado = ""

for letter in cifrado:
    if letter != "." and alphabetManager.notIsNumber(letter) and letter != "," and letter != " ":
        index = alphabetManager.getIndexLetter(letter) - int(response['numero_casas'])
        decifrado = decifrado + alphabetManager.getAlphabetLetter(index)
    else:
        decifrado = decifrado + letter

response['decifrado'] = decifrado
response['resumo_criptografico'] = hashlib.sha1(decifrado.encode("utf-8")).hexdigest()

jsonManager.writeJSON(response)
r = requests.post(URL_SUBMIT + MY_TOKEN, files={"answer": json.dumps(response)})
print(r)
print(r.json())
