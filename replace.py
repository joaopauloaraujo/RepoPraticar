import json
import os

def replaceTxt(tipo):
    with open(os.getcwd()+'\\config.json', "r") as read_file:
        data = json.load(read_file)
    path = data['path']
    file = data['file']

    for arq in file:
        with open(path + arq['name'], 'r') as fd:
            txt = fd.read()

        for i in arq['words']:
            if(tipo == 1):
                txt = txt.replace(i['isapi'], i['standalone'])
            else:
                txt = txt.replace(i['standalone'], i['isapi'])

        with open(path + arq['name'], 'w') as fd:
            fd.write(txt)

while(True):
    print(":: 1 - CREATE STANDALONE...(EXE)")
    print(":: 2 - CREATE ISAPI........(DLL)")
    print(":: 3 - EXIT ")

    valor = int(input(">> "))
    if(valor == 3):
        break
    replaceTxt(valor)
   # os.system('cls')
