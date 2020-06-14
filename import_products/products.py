from settings import api_key_master, api_token_master, api_key, api_token
from pandas import ExcelWriter
from pathlib import Path
import pandas as pd
import requests
import json
import os

path_data = Path(__file__).parent.absolute() / 'data_xml.xls'
path_products = Path(__file__).parent.absolute() / 'products.xls'
path_error_sku = Path(__file__).parent.absolute() / 'error-sku.txt'


productos = pd.read_excel(path_data)
products_name_excel = productos['ProductName'].values
products_description_excel = productos['Description'].values
products_code_excel = productos['ProductCode'].values
product_brand_excel = productos['BrandName'].values


products_sku_exist = []
error_detect = 'The column "_SKUReferenceCode" is unique and belongs to another SKU:'
with open(path_error_sku) as f:
    lines = f.readlines()
    for line in lines:
        if error_detect in line:
            products_sku_exist.append(
                line.split(error_detect)[1].strip()[1:-1])


# urls from vtex api
headers_master = {
    'content-type': "application/json",
    'accept': "application/vnd.vtex.ds.v10+json",
    'x-vtex-api-appkey': api_key_master,
    'x-vtex-api-apptoken': api_token_master
}


print("\033[92m Query api from brands \033[0m")
# query at api
url_brands = "https://{}.vtexcommercestable.com.br/api/catalog_system/pvt/brand/list"
response = requests.request(
    "GET", url_brands.format("vetro"), headers=headers_master)
brands_api = response.json()
print("\033[92m Query api from brands \033[0m")

products_id_brand = []
products_brands_name = []
# save brands
brands_dict = {}

for brand in brands_api:
    brands_dict[brand['name']] = brand['id']


for brand_data in product_brand_excel:
    if brand_data == brands_dict.keys():
        # print("\033[92m TIENE {} \033[0m".format(brand['id']))
        products_id_brand.append(brands_dict[brand_data])
        products_brands_name.append(brand_data)
    else:
        # print("\033[94m NO TIENE \033[0m")
        products_id_brand.append('2000012')
        products_brands_name.append('PROVISIONAL')


# ended brands

# make link
print("\033[92m Make caption link \033[0m")
products_captions_link = []
for name in products_name_excel:
    string_without_numbers = ''.join(c if c not in map(
        str, range(0, 10)) else "" for c in name)
    # print(stringWithoutNumbers)
    string_without_caracter_special = string_without_numbers.translate(
        {ord(c): "" for c in """!@#$%^&*()[];:,./<>?\|`~-=_+,"'"""})
    string_lower = string_without_caracter_special.lower()
    link = ' '.join(string_lower.split())
    link = link.strip()
    link = string_lower.replace(" ", "-")
    products_captions_link.append(link)

print("\033[92m Ended caption link \033[0m")
# ended link


# save products

print("\033[92m Begin creation file \033[0m")
df = pd.DataFrame({'_SkuId (Not changeable)': None,
                   '_SkuName': products_name_excel,
                   '_ActivateSkuIfPossible': 'YES',
                   '_SkuIsActive (Not changeable)': 'YES',
                   '_SkuEan': None,
                   '_Height': 1,
                   '_ActualHeight': None,
                   '_Width': 1,
                   '_ActualWidth': None,
                   '_Length': 1,
                   '_ActualLength': None,
                   '_Weight': 1,
                   '_ActualWeight': None,
                   '_MeasurementUnit': 'un',
                   '_UnitMultiplier': 1,
                   '_SKUReferenceCode': products_code_excel,
                   '_RewardValue': None,
                   '_EstimatedDateArrival': None,
                   '_ManufacturerCode': None,
                   '_ProductId (Not changeable': None,
                   '_ProductName (Required)': products_name_excel,
                   '_ProductShortDescription': None,
                   '_ProductIsActive (Not changeable)': 'YES',
                   '_ProductReferenceCodeId': products_code_excel,
                   '_ShowOnSite': 'YES',
                   '_CaptionLink (Not changeable)': products_captions_link,
                   '_ProductDescription': products_description_excel,
                   '_ProductLaunchDate': None,
                   '_Keywords': None,
                   '_SiteTitle': None,
                   '_MetaTagDescription': None,
                   '_SupplierId': None,
                   '_ShowOutOfStock': 'YES',
                   '_Kit (Not changeable)': 'NO',
                   '_DepartamentId (Not changeable)': None,
                   '_DepartamentName': None,
                   '_CategoryId': 100070208,
                   '_CategoryName': 'Vetro shop',
                   '_BrandId': products_id_brand,
                   '_Brand': products_brands_name,
                   '_CubicWeight': '0,0002',
                   '_CommercialCondition': 'Padrão',
                   '_Stores': 1,
                   '_Accessories': None,
                   '_Similar': None,
                   '_Suggestions': None,
                   '_MostrarJunto': None,
                   '_Attachment': None
                   })
df = df[['_SkuId (Not changeable)', '_SkuName', '_ActivateSkuIfPossible', '_SkuIsActive (Not changeable)', '_SkuEan', '_Height', '_ActualHeight', '_Width', '_ActualWidth', '_Length', '_ActualLength', '_Weight', '_ActualWeight', '_MeasurementUnit', '_UnitMultiplier', '_SKUReferenceCode', '_RewardValue', '_EstimatedDateArrival', '_ManufacturerCode', '_ProductId (Not changeable', '_ProductName (Required)', '_ProductShortDescription', '_ProductIsActive (Not changeable)',
         '_ProductReferenceCodeId', '_ShowOnSite', '_CaptionLink (Not changeable)', '_ProductDescription', '_ProductLaunchDate', '_Keywords', '_SiteTitle', '_MetaTagDescription', '_SupplierId', '_ShowOutOfStock', '_Kit (Not changeable)', '_DepartamentId (Not changeable)', '_DepartamentName', '_CategoryId', '_CategoryName', '_BrandId', '_Brand', '_CubicWeight', '_CommercialCondition', '_Stores', '_Accessories', '_Similar', '_Suggestions', '_MostrarJunto', '_Attachment']]
# pridfdt(df.loc[(df._ProductReferenceCodeId in products_sku_exist)])
df = df[~df._ProductReferenceCodeId.isin(products_sku_exist)]
writer = ExcelWriter(path_products)
df.to_excel(writer, 'products', index=False)
writer.save()
print("\033[92m Ended creation file \033[0m")
