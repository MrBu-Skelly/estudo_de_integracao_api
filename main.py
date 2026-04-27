import requests

moedas = ["USD-BRL", "EUR-BRL", "GBP-BRL", "BTC-BRL"]

def cotacao(par):
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    try:
        resposta = requests.get(url, timeout=10)
        dados = resposta.json()
        chave = par.replace("-", "")
        return dados[chave]['bid']
    except Exception as e:
        print(f"Erro: {e}")
        return None

for moeda in moedas:
    valor = cotacao(moeda)
    print(f"A cotação de {moeda} é: R$ {valor}")

