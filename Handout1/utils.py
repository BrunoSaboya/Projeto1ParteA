import json
from json import encoder
import os

def extract_route(request):
    filename=''
    if len(request.split())>0:
        filename = request.split()[1][1:]
    return filename

def read_file(path):
    filename, file_extension = os.path.splitext('/path/to/somefile.ext')
    extensions_list = [".txt", ".html", ".css", ".js"]
    if file_extension in extensions_list:
        file = open(path, "rt")
        return file.read()
    else:
        file = open(path, "rb")
        return file.read()

def load_data(nomeJson):
    filePath = "Handout1/data/"+nomeJson
    with open(filePath, "rt", encoding="utf-8") as text:
        content = text.read()
        contentPython = json.loads(content)
        return contentPython

def load_template(file_path):
    file = open("Handout1/templates/"+file_path, 'r', encoding="utf-8")
    content = file.read()
    file.close()
    return content

def adiciona_dic(dicionario):
    read = load_data('notes.json')
    read.append(dicionario)
    dicionario = json.dumps(read)
    with open('Handout1/data/notes.json', "w", encoding="uft-8") as text:
        content = text.write(dicionario)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == "":
        skip = ""
    else:
        skip = "\n"
    if isinstance(body,str):
        body = body.encode()
    return ("HTTP/1.1 "+f"{code} "+reason+skip+headers+"\n\n").encode()+body
    
def extract_route(request):
    filename=''
    if len(request.split())>0:
        filename = request.split()[1][1:]
    return filename

def read_file(path):
    filename, file_extension = os.path.splitext('/path/to/somefile.ext')
    extensions_list = [".txt", ".html", ".css", ".js"]
    if file_extension in extensions_list:
        file = open(path, "rt")
        return file.read()
    else:
        file = open(path, "rb")
        return file.read()

# def load_data(banco):
#     db = Database(banco)
#     notes:list[Note] = db.get_all()
#     return notes



# def build_response(body='', code=200, reason='OK', headers=''):
#     if headers == "":
#         skip = ""
#     else:
#         skip = "\n"
#     if isinstance(body,str):
#         body = body.encode()
#     return ("HTTP/1.1 "+f"{code} "+reason+skip+headers+"\n\n").encode()+body