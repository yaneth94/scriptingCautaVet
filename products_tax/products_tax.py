from settings import api_key, api_token, api_key_nexus
from pathlib import Path
import os
import requests
import json

# header nexus
headers_nexus = {
    'content-type': 'application/json',
    'Authorization': 'Basic ' + api_key_nexus
}


# url nexus
url_nexus = "http://nexus.vetro.vet:5100/api/v3/read/preturi"

payload = {}
payload['id_document'] = "2(1)"
payload['id_gestiune'] = "1(1)"
payload = json.dumps(payload)

# call nexus
response = requests.request(
    "POST", url_nexus, data=payload, headers=headers_nexus)
products_nexus = response.json()
products_nexus = products_nexus['result']

list_id_produs, list_product, list_id_produs_nva = [], [], []
for product_api in products_nexus:
    id_produs = product_api['id_produs']
    produs = {
        "id_produs": product_api['id_produs'],
        "den_produs": product_api['den_produs'],
        "cota_tva_ies": product_api['cota_tva_ies']
    }

    list_id_produs.append(id_produs)
    # esto ver despues
    list_id_produs_nva.append(id_produs)
    list_product.append(produs)


list_id_produs = list(set(list_id_produs))
list_id_produs = str(list_id_produs)
list_id_produs = list_id_produs.replace("'", '"')


# header vtex
headers = {
    'content-type': "application/json",
    'accept': "application/vnd.vtex.ds.v10+json",
    'x-vtex-api-appkey': api_key,
    'x-vtex-api-apptoken': api_token
}


print("\033[92m   ****** Begin Query api nexus from products  ****** \033[0m")

# url vtex
url_vtex_sku = "https://vetro.vtexcommercestable.com.br/api/catalog_system/pub/sku/stockkeepingunitidsbyrefids"

# call vtex
response = requests.request(
    "POST", url_vtex_sku, data=list_id_produs, headers=headers)
products_vtex = response.json()

print("\x1b[1;33m  ****** Ended Query api nexus from products  ****** \033[0m")


print("\033[92m   ****** Begin Delete products wth sku none ****** \033[0m")
filter_vtex_dict = {}
# eliminando de skus con none
for product in products_vtex.keys():
    if products_vtex[product]:
        filter_vtex_dict[product] = products_vtex[product]

print("\x1b[1;33m  ****** Ended Delete products wth sku none ****** \033[0m")


print("\033[92m   ****** Begin Products equals in vtex ****** \033[0m")

# llamada a api de vtex para sacar los nombres de los productos y que no sean de nexus
url_sku_id = "https://vetro.vtexcommercestable.com.br/api/catalog_system/pvt/sku/stockkeepingunitbyid/{}"

# sacando los que coincidan con nexus
products_nexus_vtex = []
for product in list_product:
    if product['id_produs'] in list(filter_vtex_dict.keys()):
        response = requests.request(
            "GET", url_sku_id.format(filter_vtex_dict[product['id_produs']]), headers=headers)
        sku_api = response.json()
        produs = {
            "id_produs": product['id_produs'],
            "den_produs": sku_api['SkuName'],
            "cota_tva_ies": product['cota_tva_ies'],
            "product_id": sku_api['ProductId'],
            "sku_id": filter_vtex_dict[product['id_produs']]
        }
        products_nexus_vtex.append(produs)


print("\x1b[1;33m  ****** Ended Products equals in vtex ****** \033[0m")

"""
for product in products_nexus_vtex:
    response = requests.request(
        "GET", url_sku_id.format(product['sku_id']), headers=headers)
    sku_api = response.json()
    product['den_produs'] = sku_api['SkuName']
"""

print("\033[92m   ****** Begin Classification by tva ****** \033[0m")

products_tva_dict = {}
for product in products_nexus_vtex:
    # asignacion
    cota_tva = product['cota_tva_ies']
    #name = product['den_produs']
    product_id = product['product_id']
    if not cota_tva in products_tva_dict.keys():
        products_tva_dict[cota_tva] = []
        products_tva_dict[cota_tva].append(product_id)
    else:
        products_tva_dict[cota_tva].append(product_id)

print("\x1b[1;33m  ****** Ended Classification by tva ****** \033[0m")

print("\033[92m   ****** Begin Create txt file ****** \033[0m")

path_products = Path(__file__).parent.absolute() / 'products'
for tva in products_tva_dict.keys():
    chunck = 1
    path_file = 'tax-{}-{}.txt'
    path_product = path_products / path_file.format(tva, 1)
    file = open(path_product, "wt")
    # quitando repetidos
    products_tva = list(set(products_tva_dict[tva]))
    # terminando repetidos
    numero_product = 0
    for line in products_tva:
        numero_product = numero_product + 1
        if numero_product % 199 == 0:
            chunck = chunck+1
            path_product = path_products/path_file.format(tva, chunck)
            file = open(path_product, "wt")

        file.write(str(line) + '\n')
        # print(line)
    file.close()

print("\x1b[1;33m  ****** Ended Create txt file ****** \033[0m")
