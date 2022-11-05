Como consumir uma API cria por você no RePlit
 
 Essa API foi criada para fins didaticos.
 A base de dados está junto com o projeto

 # codigo usado no replit
 import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#tabela = pd.read_csv('revisao.csv')
#total_vendas = tabela['Vendas'].sum()
#print(total_vendas)


@app.route('/')
def homepage():
  return 'API está no ar'

@app.route('/totalvendas')
def totalvendas():
  tabela = pd.read_csv('revisao.csv')
  total_vendas = tabela['Vendas'].sum()

  # criamos a nossa resposta da nossa API
  resultado = {'total_vendas': total_vendas}
  return jsonify(resultado)


app.run(host='0.0.0.0')

________________________________________________

Agora iremos criar um codigo para consumir essa API, certifique-se que a API estava ligada para
fazer o teste
_______________________________________
1° primeiro instale o pagote "requests"
    pip install requests

2° chame ela