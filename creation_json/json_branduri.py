from pathlib import Path
import os

path_branduri = Path(__file__).parent.absolute() / 'branduri'

branduri = [
    {
        "name": "A.G CHIM",
        "row": 1,
        "column": 1,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "ADVANCE VET",
        "row": 1,
        "column": 2,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "AGROSEM",
        "row": 1,
        "column": 3,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "Alfavet",
        "row": 1,
        "column": 4,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "ALLFEED INTERNATIONAL",
        "row": 1,
        "column": 5,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "ALLFLEX",
        "row": 2,
        "column": 1,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "Animedica",
        "row": 2,
        "column": 2,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592014363/vetroB2B/branduri/branduri-2_b2b_krqsdx.gif"
    },
    {
        "name": "Antibiotica S.A",
        "row": 2,
        "column": 3,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592014962/vetroB2B/branduri/branduri-3_b2b_i0zqhb.gif"
    },
    {
        "name": "APARATURA SI CONSUMABILE",
        "row": 2,
        "column": 4,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "AST Farma",
        "row": 2,
        "column": 5,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592014363/vetroB2B/branduri/branduri-4_b2b_dvwwyk.gif"
    },
    {
        "name": "AVENTIX",
        "row": 3,
        "column": 1,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "AYURVET",
        "row": 3,
        "column": 2,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "B.Braun",
        "row": 3,
        "column": 3,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592014363/vetroB2B/branduri/branduri-5_b2b_vtmahc.gif"
    },
    {
        "name": "Bast-The Chemical Company",
        "row": 3,
        "column": 4,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592014363/vetroB2B/branduri/branduri-6_b2b_bbhbpu.gif"
    },
    {
        "name": "Bayer",
        "row": 3,
        "column": 5,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "Bayer Environmental Science",
        "row": 4,
        "column": 1,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592019916/vetroB2B/branduri/branduri-7_b2b_cax5lz.gif"
    },
    {
        "name": "Beohringer Ingelheim",
        "row": 4,
        "column": 2,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592019916/vetroB2B/branduri/branduri-8_b2b_ppjuea.gif"
    },
    {
        "name": "BIOCANINA",
        "row": 4,
        "column": 3,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "Bioveta",
        "row": 4,
        "column": 4,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592019916/vetroB2B/branduri/branduri-9_b2b_h4yjxu.gif"
    },
    {
        "name": "BIO-X DIAGNOSTICS",
        "row": 4,
        "column": 5,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "Catalysis",
        "row": 5,
        "column": 1,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "Cenavisa",
        "row": 5,
        "column": 2,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592019916/vetroB2B/branduri/branduri-10_b2b_f4xoxk.gif"
    },
    {
        "name": "CEVA POULTRY",
        "row": 5,
        "column": 3,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "CEVA RUMANINANTS",
        "row": 5,
        "column": 4,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "CEVA Sante Animale",
        "row": 5,
        "column": 5,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592019916/vetroB2B/branduri/branduri-11_b2b_j6gkkh.gif"
    },
    {
        "name": "CEVA SWINE",
        "row": 6,
        "column": 1,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "CEVA VITAMINE",
        "row": 6,
        "column": 2,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "Cp-Pharma",
        "row": 6,
        "column": 3,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "Crida Pharm",
        "row": 6,
        "column": 4,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    },
    {
        "name": "Dechra",
        "row": 6,
        "column": 5,
        "image": "https://res.cloudinary.com/vetro-solution/image/upload/v1592012648/vetroB2B/branduri/branduri-1_b2b.gif"
    }


]

list_brands_text = []

list_brands_image = []

list_brands_col = []

for brand in range(0, len(branduri)):
    brands = branduri[brand]
    print(brands)
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

path_flex_col = path_branduri / 'flex_col_branduri.jsonc'
parse_brands_col = parse_strings(list_brands_col)
file = open(path_flex_col, "wt")
file.write(parse_brands_col)
file.close()
