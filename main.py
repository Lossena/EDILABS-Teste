#importar a biblioteca requests para consumir a API
import requests 
#importar a biblioteca datetime para ter a data atual
from datetime import date

#salvar a URL da API em uma variavel para ficar mais legivel
url = "https://restcountries.com/v3.1/independent?status=true&fields=languages,capital"

#salva a data atual formatada em uma variavel
today = date.today().strftime("%d/%m/%Y")

#faz um request do tipo get na API
r = requests.get(url)
#salva a resposta formatada em json
response = r.json()

#abre o arquivo de texto para edição
f = open("arquivo.txt", "w")

#escreve a primeira linha do arquivo contendo o Encoding e a data atual
f.write(f"Encoding: utf-8, Data: {today}\n\n")

#usa a função enumerate para retornar tanto indice quanto o elemento atual da lista
for index,element in enumerate(response):
  #cria a variavel e atribui + ou - dependendo se for par ou impar
  operator = ""
  if index %2 == 0:
    operator = "+"
  else: 
    operator = "-"

  #cria o texto formatado contendo o operador, indice e o nome da capital com seus idiomas
  capital_line = f"{operator} Capital n°{index}, Nome: {element['capital'][0]}, Idiomas: {element['languages']}\n" 
  
  #escreve uma linha para cada elemento da lista com o texto formatado
  f.write(capital_line)

#fecha o arquivo manualmente para evitar erros no fechamento automatico do python
f.close()