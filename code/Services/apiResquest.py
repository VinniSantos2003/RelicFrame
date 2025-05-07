import requests
import json
slug = "khora_prime_neuroptics_blueprint"
wfMarketApi = requests.get(f"")
#print(wfMarketApi.status_code)
requestedData = json.loads(wfMarketApi.text)
mediaPreco = 0
print(requestedData["data"][len(requestedData["data"])-1])

for i in range(1,5):
    mediaPreco += requestedData["data"][len(requestedData["data"])-i]["platinum"]

print(mediaPreco/5)

"""
Ordem de requisção da API warframeMarket

1- Montar o Slug(Um item qualquer do warframe que seja trocavel, a slug deve estar em letras minusculas e separada por _ )
2- Realizar requição em "https://api.warframe.market/v2/orders/item/{slug}"
3- Montar Json baseado no .text da requição feita
^Apartir daqui não é necessário mais necessário o acesso a API^

"""