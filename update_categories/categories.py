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

url_categories = "https://{}.vtexcommercestable.com.br/api/catalog_system/pub/category/tree/20"
url_create_category = "https://{}.vtexcommercestable.com.br/api/catalog/pvt/category"

response = requests.request("GET", url_categories.format("vetro"), headers=headers_master)
categories = response.json()

def creation_payload(category, category_id = None):
    payload = {}
    payload['Name'] = category["name"]
    payload['Keywords'] = ""
    payload['Title'] = category["Title"]
    payload['Description'] = category["MetaTagDescription"]
    payload['AdWordsRemarketingCode'] = None
    payload['LomadeeCampaignCode'] = None
    payload['FatherCategoryId'] = category_id
    payload['GlobalCategoryId'] = None
    payload['ShowInStoreFront'] = True
    payload['IsActive'] = True
    payload['ActiveStoreFrontLink'] = True
    payload['ShowBrandFilter'] = True
    payload['Score']= None
    payload['StockKeepingUnitSelectionMode']= "SPECIFICATION"
    return payload

def children_function(category,father,category_id):
    print("\033[94m  begin hijo: {} his father is: {} with id of father: {}  \033[0m".format(category["name"],father['name'],father['id']))

    #creation payload
    payload = creation_payload(category,category_id)
    #save category
    payload = json.dumps(payload)
    #print(payload)
    response = requests.request('POST', url_create_category.format("vetrob2c"), data=payload, headers=headers)
    print(response.text)
    response = response.json()
    #save category_id
    category_id = response['Id']
   
    #end category

    # map childrens
    if category['hasChildren']:
        childrens = category["children"]
        for children in range(0,len(childrens)):
            children_function(childrens[children],category,category_id)

    # end map childrens
    print("\x1b[1;33m  end hijo: {} his father is: {} with id of father: {}  \033[0m".format(category["name"],father['name'],father['id']))

for category in categories:
    print("\033[92m  ***************** begin padre: {}  ***************** \033[0m".format(category["name"]))
    
    #creation payload
    payload = creation_payload(category)
    #save category
    payload = json.dumps(payload)
    response = requests.request('POST', url_create_category.format("vetrob2c"), data=payload, headers=headers)
    print(response.text)
    response = response.json()
    #save category_id
    category_id = response['Id']
    
    #end save category

    # map childrens
    if category['hasChildren']:
        childrens = category["children"]
        for children in range(0,len(childrens)):
            children_function(childrens[children],category, category_id)
    #end map childrens
        
    print("\033[92m ***************** end padre: {} *********************** \033[0m".format(category["name"]))



