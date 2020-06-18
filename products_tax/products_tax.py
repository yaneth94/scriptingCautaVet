from settings import api_key, api_token, api_key_nexus
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

list_id_produs, list_product, list_tva, list_id_produs_nva = [], [], [], []
for product_api in products_nexus:
    id_produs = product_api['id_produs']
    produs = {
        "id_produs": product_api['id_produs'],
        "den_produs": product_api['den_produs'],
        "cota_tva_ies": product_api['cota_tva_ies']
    }

    list_tva.append(product_api['cota_tva_ies'])
    list_id_produs.append(id_produs)
    list_id_produs_nva.append(id_produs)
    list_product.append(produs)

list_tva = list(set(list_tva))
list_id_produs = list(set(list_id_produs))
list_id_produs = str(list_id_produs)
list_id_produs = list_id_produs.replace("'", '"')
# print(list_id_produs)

# header vtex
headers = {
    'content-type': "application/json",
    'accept': "application/vnd.vtex.ds.v10+json",
    'x-vtex-api-appkey': api_key,
    'x-vtex-api-apptoken': api_token
}

# url vtex
url_vtex_sku = "https://vetro.vtexcommercestable.com.br/api/catalog_system/pub/sku/stockkeepingunitidsbyrefids"

# call vtex
response = requests.request(
    "POST", url_vtex_sku, data=list_id_produs, headers=headers)
products_vtex = response.json()

filter_vtex_dict = {}

for product in products_vtex.keys():
    if products_vtex[product]:
        filter_vtex_dict[product] = products_vtex[product]

# print(filter_vtex_dict)
products_nexus_vtex = []
count_si, count_no = 0, 0
# print(list(filter_vtex_dict.keys()))
for product in list_product:
    if product['id_produs'] in list(filter_vtex_dict.keys()):
        produs = {
            "id_produs": product['id_produs'],
            "den_produs": product['den_produs'],
            "cota_tva_ies": product['cota_tva_ies']
        }
        products_nexus_vtex.append(produs)
        count_si = count_si + 1
    else:
        count_no = count_no + 1

print(products_nexus_vtex)
print(count_si)
print(count_no)
