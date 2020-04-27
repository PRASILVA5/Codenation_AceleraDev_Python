# PauloRASilva
# Links uteis:
# https://cryptii.com/
# https://www.convertstring.com/pt_PT/Hash/SHA1
# https://github.com/PRASILVA5

import requests
import hashlib
import json

alfabetoString = "abcdefghijklmnopqrstuvwxyz"
alfabetoLista = list(alfabetoString)
decifradoLista = []
urlGet = 'EscreverGetUrl'
urlPost = 'EscreverPostUrl'

# Get request
r = requests.get(urlGet)

data = r.json()
nunCasas = int(data["numero_casas"])
cifradoLista = list(data["cifrado"])

# Lógica Decrypt
for letra in cifradoLista:
    if letra in alfabetoLista:
        posLetra = alfabetoLista.index(letra) + 2
        if posLetra + nunCasas <= 25:
            decifradoLista.append(alfabetoLista[posLetra + nunCasas])
        else:
            decifradoLista.append(alfabetoLista[posLetra + nunCasas - 26])
    else:
        decifradoLista.append(letra)
decifradoString = ''.join(decifradoLista)
print(decifradoString)

# Hash em Sha1
hashResult = hashlib.sha1(decifradoString.encode())
print(hashResult.hexdigest())

# Atualizando dicionario "data"
data["decifrado"] = decifradoString
data["resumo_criptografico"] = hashResult.hexdigest()
print(data)

# Criando arquivo json
with open('answer.json', 'w') as outfile:
    json.dump(data, outfile)

# Post request
files = {'answer': ('answer.json', open('answer.json', 'rb'), 'multipart/form-data')}
rtn = requests.post(urlPost, files=files)
