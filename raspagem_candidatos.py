import requests
from bs4 import BeautifulSoup

link = "http://localhost:8000"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, "html.parser")
profissao = site.findAll("h4")
sobre = site.findAll("pre")
pessoa = site.findAll("h2")

def profissoes():
    for x in profissao:
        print(x.text, x.next_sibling)

def qtd_pessoa_profissao(a):
    cont = 0
    for x in profissao:
        if(a == x.text):
            cont = cont + 1
    print(cont)

def mostrarSobre():
    for x in sobre:
        print(x.text+
              "\n----------------------------------------------------------------------------------------------------------------\n", 
              x.next_sibling)

def mostrarSobrePessoa(a):
    z = []
    r = []
    t = 0
    for x in pessoa:
        z.append(x)
        if(a == x.text): 
            t = len(z)
            break;     
    for y in sobre: 
        r.append(y.text) 
    if(t == 0):
        print("Pessoa não existe!")
    else:
        print(r[t-1]) 

def mostrarProfissaoPessoa(a):
    z = []
    r = []
    t = 0
    for x in pessoa:
        z.append(x)
        if(a == x.text): 
            t = len(z)
            break;     
    for y in profissao: 
        r.append(y.text) 
    if(t == 0):
        print("Pessoa não existe!")
    else:
        print(r[t-1])         


profissoes()