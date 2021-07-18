

class Product:

    def __init__(self,pid,pnm,pqty,pric,pven,pcat):
        self.prodId = int(pid)
        self.prodName = pnm
        self.prodQty = int(pqty)
        self.prodPrice = float(pric)
        self.prodVendor = pven
        self.prodCategory = pcat

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''


p1 = Product(pid=7711,pnm='Mobile1',pqty=23,pric=16289.23,pven='Flipkart',pcat='ET')
p2 = Product(pid=102,pnm='Mobile2',pqty=3,pric=15289.23,pven='Flipkart',pcat='ET')
p3 = Product(pid=103,pnm='Mobile3',pqty=53,pric=15289.23,pven='Flipkart',pcat='ET')
p4 = Product(pid=104,pnm='Mobile4',pqty=26,pric=12889.23,pven='Flipkart',pcat='ET')
p5 = Product(pid=105,pnm='Mobile5',pqty=73,pric=12789.23,pven='Flipkart',pcat='ET')
products = [p1,p2,p3,p4,p5]

#with --> context manager -->
            # what is the context manager-- context manager is the functionality --> to make sure--> resource will be closed
                                # once we exit --> with block -->
                                #context manager--> is class --. which has 2 imp methods ->
                                                    #__enter__ --> intialization
                                                    #__exit__  --> resource cleanup activities
            # can we write custom context manager -->
                    #yes --> how ??

import re

import os
ans = os.getcwd() # present working director -->

COMMON_PATH = '\\ecom_data\\'

TEXT_FILE_PATH = ans+COMMON_PATH+'sample.txt'
CSV_FILE_PATH = ans+COMMON_PATH+'prod.csv'
JSON_FILE_PATH = ans+COMMON_PATH+'prod.json'
print(TEXT_FILE_PATH)
'''
                        file present asel tr                        file absent asel                    remarks
r                          read operation                           error: file not found               make sure ki file present kara 
w                          new file:overwrite                       newfile                             always new file:
a                           append :write                            newfile:write                      depends on situation:safe
b                           --------------------------multimedia context [any file format--pdf/image/video/audio]--------------------------------------                
x                           error                                       no error                        just to check file presence

r+                        r-> same as above --> except--> this can perform --> read+write operation --> seek-> read cursor--> zero'th position
w+                        w-> same as above --> except--> this can perform --> read+write operation --> write sample--> read cursor
a+                        read+write[append] ---> 
b+                        --------------------------multimedia context [any file format--pdf/image/video/audio]--------------------------------------                


rw
wr
rb


'''

import json
def write_data_into_json():
    prod_dict_list = []
    for prod in products:
        prod_dict_list.append(prod.__dict__)
    jsonstr = json.dumps(prod_dict_list)
    print(jsonstr)
    print(JSON_FILE_PATH)
    with open(JSON_FILE_PATH,'w') as file:
        file.writelines(jsonstr)
        print('Contents written...')
    print('Json Contents Written into file..!')


#write_data_into_json()

def read_data_from_json():
    with open(JSON_FILE_PATH,'r') as file:
        jsoncontents = json.load(file)
        prodList = []
        for record in jsoncontents:
            prodList.append(Product(pid=record.get('prodId'),pnm=record.get('prodName'),pqty=record.get('prodQty'),
                    pric=record.get('prodPrice'),pven=record.get('prodVendor'),pcat=record.get('prodCategory')))
        return prodList


def get_max_price_product():
    products = read_data_from_json()
    products.sort(key=lambda prod : prod.prodPrice,reverse=True)
    return  products[0]

prodlist = read_data_from_json()
print(prodlist)

ans = get_max_price_product()
print(ans)

def write_data_into_csv():
    pass

def read_data_from_csv():
    pass


#default -- db -.sqlite3

# we need install 3rd party libs - to support- - excel/yaml/xml/db read write operations
def write_data_into_excel():
    pass

def read_data_from_excel():
    pass

def write_data_into_xml():
    pass

def read_data_from_xml():
    pass

def write_data_into_yaml():
    pass

def read_data_from_yaml():
    pass











