import json
from os import write

def extract_route(requisicao):
    if requisicao.startswith('GET'):
        lista1 = requisicao.split("GET /")
    else:
        lista1 = requisicao.split("POST /")

    lista2 = lista1[1].split(" ")
    return lista2[0]

def read_file(path):
    lista = str(path).split(".")
    if lista[-1]=="txt" or lista[-1]=="html" or lista[-1]=="css" or lista[-1]=="js":
        with open(path, "rt") as file:
            text = file.read()
            return text
    else:
        with open(path, "rb") as file:
            binary = file.read()
        return binary

def load_data(nomeJson):
    filePath = "data/"+nomeJson
    with open(filePath, "rt", encoding="utf-8") as text:
        content = text.read()
        contentPython = json.loads(content)
        return contentPython

def load_template(file_path):
    file = open("templates/"+file_path)
    content = file.read()
    file.close()
    return content

def adiciona_dic(dicionario):
    read = load_data('notes.json')
    read.append(dicionario)
    dicionario = json.dumps(read)
    with open('data/notes.json', "w", encoding="uft-8") as text:
        content = text.write(dicionario)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        headers=f"\n{headers}"
    response=f"HTTP/1.1{code} {reason}{headers}\n\n{body}".encode()
    return response
    