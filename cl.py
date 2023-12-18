import game as gam


class Apple(gam.Product):

    apples = {}

    def __init__(self, name, sale_price):
        gam.Product.__init__(self, name, sale_price)

        Apple.apples[self.name.lower()] = self


golden_apple = Apple('Golden Apple', 5)
red_apple = Apple('Red Apple', 2)

apple_factory = gam.Factory('Apple Factory')

apple_factory.give(red_apple, 4)
apple_factory.give(golden_apple, 2)

print(apple_factory.storage)

for type in apple_factory.storage:
    sale_price = gam.Product.products[type].sale_price
    gam.Player.credits += sale_price * apple_factory.storage[type]
    apple_factory.storage[type] = 0

print(apple_factory.storage)
print(gam.Player.credits)
