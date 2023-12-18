# def funct():
    
#     total_start = time.time()

#     while time.time() < total_start + 30:

#         start = time.time()

#         while time.time() < start + 5:
#             pass

#         print(f'{time.time() - total_start} seconds')

#     print('It has been 30 seconds')

# timer = threading.Thread(target=funct)

# timer.start()

# while True:
#     print(input('Say something:\n> '))


import time
import random
import threading


# Class for defining a source of a product
class Source:

    # Dictionary for linking a source type to its name
    sources = {}


    def __init__(self, name, product=None):

        # Define required attributes

        self.name = name


        # Define any provided keyword attributes

        if product is not None and type(product) == Product : associate(product=product, source=self)
        elif product is not None : raise TypeError(f'Product provided for source "{self.name}" is not of type Product (gave type {type(product)})')


        # Add source type to dictionary
        Source.sources[name] = self


    # Optional method, requires the input of ingredients (products) to be able to output product
    def set_ingredients(self, ingredients) : self.ingredients = ingredients


# Class for defining a product
class Product:

    # Dictionary for linking a product type to its name
    products = {}


    def __init__(self, name, source=None, sale_price=None):

        # Define required attributes

        self.name = name


        # Define any provided keyword attributes
        
        if source is not None and type(source) == Source : associate(product=self, source=source)
        elif source is not None : raise TypeError(f'Source provided for product "{self.name}" is not of type Source (gave type {type(source)})')

        if sale_price is not None and (type(sale_price) == int or type(sale_price) == float) : self.sale_price = sale_price
        elif sale_price is not None : raise TypeError(f'Sale price provided for product "{self.name}" must be an integer or a float (gave type {type(sale_price)})') 

        # Add product type to dictionary
        Product.products[name] = self


    # Method for defining a sale price
    def set_sale_price(self, sale_price):
        if type(sale_price) == int or type(sale_price) == float : self.sale_price = sale_price
        else : raise TypeError(f'Sale price provided for product "{self.name}" must be an integer or a float (gave type {type(sale_price)})')


# Class for defining a "farm", basically a world
class Farm:

    # Dictionary for linking a farm to its name
    farms = {}

    def __init__(self, name, inventory={}):

        # Define required attributes
        self.name = name
        self.inventory = inventory

        # Define any provided keyword attributes

        # Add farm to dictionary
        Farm.farms[name] = self


# Function for linking a product and a source
def associate(*, product, source):
    
    if type(product) == Product and type(source) == Source:
        product.source = source
        source.product = product

    else:
        if type(product) != product : raise TypeError(f'Product provided is not of type Product (gave type {type(product)})')
        if type(source) != source : raise TypeError(f'Source provided is not of type Source (gave type {type(source)})')


#############################################################################################################################################
#############################################TESTING-SHIT####################################################################################
################################################################################################################################################
wood = Product('Wood', sale_price=5)
tree = Source('Tree')

ranch = Farm('The Ranch')















