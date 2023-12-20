class Product:
    
    products = {}
    collections = {}

    def __init__(self, name, sale_price):

        self.name = name
        self.sale_price = sale_price
        self.source = None

        Product.products[self.name.lower()] = self

    # Method for adding a product to a collection
    def add_to_collection(self, collection):
        Product.collections[collection].append(self.name.lower())

    # Method for adding a product collection
    @classmethod
    def add_collection(cls, collection_name):
        cls.collections[collection_name] = []

class Source:
    
    sources = {}
    collections = {}
    
    def __init__(self, name):

        self.name = name
        self.product = None

        Source.sources[self.name.lower()] = self

    # Method for adding a source to a collection
    def add_to_collection(self, collection):
        Source.collections[collection].append(self.name.lower())
    
    # Method for adding a source collection
    @classmethod
    def add_collection(cls, collection_name):
        cls.collections[collection_name] = []

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

    def give(self, type, level, amount):

        try:
            key = f'{type.name.lower()} {str(level)}'

        except AttributeError:
            raise AttributeError(f'ATTRIBUTE ERROR IN FACTORY.GIVE NEEDS TO BE FINISHED')

        # This section searches for the item in the factory
        # It is added if not found
        if isinstance(type, Product) and key in self.storage:
            self.storage[key] += amount

        elif isinstance(type, Product) and key not in self.storage:
            self.storage[key] = amount

        elif isinstance(type, Source) and key in self.sources:
            self.sources[key] += amount
        
        elif isinstance(type, Source) and key not in self.sources:
            self.sources[key] = amount

        else:
            raise TypeError(f'{type} must be a Product or a Source, eventually other things')



class Player:

    credits = 0


    

