class Product:
    
    products = {}

    def __init__(self, name, sale_price):

        self.name = name
        self.sale_price = sale_price
        self.source = None

        Product.products[self.name.lower()] = self

class Source:
    
    sources = []
    
    def __init__(self, name):

        self.name = name
        self.product = None

        Source.sources.append(self)

# Function for linking a product and a source
def link(product, source):

    # Unlink the product's current source from the product
    if product.source is not None:
        product.source.product = None

    # Assign new source to the product
    product.source = source

    # Unlink the source's current product from the source
    if source.product is not None:
        source.product.source = None

    # Assign new product to the source
    source.product = product

class Factory:
    
    factories = []

    def __init__(self, name):

        self.name = name

        self.sources = {}
        self.storage = {}

        Factory.factories.append(self)

    def give(self, product, amount):

        if product in self.storage:
            self.storage[product.name.lower()] += amount

        else:
            self.storage[product.name.lower()] = amount


class Player:

    credits = 0

# apple = Product('Apple')
# apple_tree = Source('Apple Tree')

# link(apple, apple_tree)

# apple_factory = Factory('Apple Factory')


