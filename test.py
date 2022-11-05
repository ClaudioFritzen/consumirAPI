import requests

#pegamos o link aonde a API esta disponivel
link = 'https://testapi.claudiofritzen.repl.co/totalvendas'
print('resultado do link', link)
# fazendo a requsição para o link
requisicao = requests.get(link)
print('Receberemos um codigo pra ver se o site esta no ar', requisicao)

# tranformando o cod recebido em json
print(requisicao.json())