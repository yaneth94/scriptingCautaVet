from settings import  api_key_master, api_token_master, api_key, api_token
import requests
import json

# urls from vtex api
headers_master = {
    'content-type': "application/json",
    'accept': "application/vnd.vtex.ds.v10+json",
    'x-vtex-api-appkey': api_key_master,
    'x-vtex-api-apptoken': api_token_master
}
#header vetrob2c
headers = {
    'content-type': "application/json",
    'accept': "application/vnd.vtex.ds.v10+json",
    'x-vtex-api-appkey': api_key,
    'x-vtex-api-apptoken': api_token
}

url_brands = "https://{}.vtexcommercestable.com.br/api/catalog_system/pvt/brand/list"
url_create_brand = "https://{}.vtexcommercestable.com.br/api/catalog/pvt/brand"

response = requests.request("GET", url_brands.format("vetro"), headers=headers_master)
brands = response.json()



for brand in brands:
    print("\033[92m : ******************: {}  ************** \033[0m".format( brand['name']))
    brand_link = str("".join(brand['name'])).replace(" ", "").lower()
    payload = {
        "Id": brand['id'],
        "Name": brand['name'],
        "Text":  brand['name'],
        "Keywords":  brand['name'],
        "SiteTitle": brand['title'],
        "Active": brand['isActive'],
        "MenuHome": True,
        "AdWordsRemarketingCode": "",
        "LomadeeCampaignCode": "",
        "Score": None,
        "LinkId": brand_link
    }
    payload = json.dumps(payload)
    response = requests.request("POST", url_create_brand.format("vetrob2c"), data=payload, headers=headers)
    print(response.text)
    print(payload)
    print("\033[92m : ****************** end: {}  ************** \033[0m".format( brand['name']))