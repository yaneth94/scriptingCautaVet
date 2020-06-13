from pathlib import Path
import os
from json_branduri import branduri

path_branduri = Path(__file__).parent.absolute() / 'branduri'


list_brands_text = []

list_brands_image = []

list_brands_col = []

list_brands_row = []

for row in range(1, 8):
    name_row = "flex-layout.row#branduri-row-{}".format(row)
    brand_row = {
        name_row: {
            "children": [
                "flex-layout.col#branduri-col-row-1-{}".format(row),
                "flex-layout.col#branduri-col-row-2-{}".format(row),
                "flex-layout.col#branduri-col-row-3-{}".format(row),
                "flex-layout.col#branduri-col-row-4-{}".format(row),
                "flex-layout.col#branduri-col-row-5-{}".format(row)
            ]
        }
    }
    brand_row = '''{}'''.format(
        str(brand_row)[1:-1]).replace("'", '"')
    list_brands_row.append(brand_row)

for brand in range(0, len(branduri)):
    brands = branduri[brand]
    # creation rich-text for branduri
    name_rich = "rich-text#branduri-col-row-{}-{}".format(
        brands['column'], brands['row'])

    brand_rich_text = {
        name_rich: {
            "props": {
                "text": "**{}**".format(brands['name']),
                "textAlignment": "CENTER",
                "textPosition": "CENTER"
            }
        }
    }
    brand_rich_text = '''{}'''.format(
        str(brand_rich_text)[1:-1]).replace("'", '"')

    list_brands_text.append(brand_rich_text)

    # creation image for branduri
    name_image = "image#branduri-{}-{}".format(brands['column'], brands['row'])

    brand_image = {
        name_image: {
            "props": {
                "src": "{}".format(brands['image']),
                "maxHeight": 200
            }
        }
    }
    brand_image = '''{}'''.format(
        str(brand_image)[1:-1]).replace("'", '"')

    list_brands_image.append(brand_image)

    # creation flex-col for branduri
    name_col = "flex-layout.col#branduri-col-row-{}-{}".format(
        brands['column'], brands['row'])
    brand_col = {
        name_col: {
            "children": [name_image, name_rich],
            "props": {
                "paddingLeft": 5,
                "paddingRight": 5
            }
        }
    }
    # print(name_col)
    brand_col = '''{}'''.format(
        str(brand_col)[1:-1]).replace("'", '"')
    list_brands_col.append(brand_col)


#list_brands_text = str(list_brands_text).replace("'", '')
# print(list_brands_text)

def parse_strings(list_brand):
    parse_brands = str(list_brand).replace("'", '')[1:-1]
    parse_brands = "{ %s }" % (parse_brands)
    return parse_brands


path_image = path_branduri / 'image_branduri.jsonc'
parse_brands_image = parse_strings(list_brands_image)
file = open(path_image, "wt")
file.write(parse_brands_image)
file.close()

path_text = path_branduri / 'text_branduri.jsonc'
parse_brands_text = parse_strings(list_brands_text)
file = open(path_text, "wt")
file.write(parse_brands_text)
file.close()

path_row = path_branduri / 'flex_row_branduri.jsonc'
parse_brands_row = parse_strings(list_brands_row)
file = open(path_row, "wt")
file.write(parse_brands_row)
file.close()

path_flex_col = path_branduri / 'flex_col_branduri.jsonc'
parse_brands_col = parse_strings(list_brands_col)
file = open(path_flex_col, "wt")
file.write(parse_brands_col)
file.close()
