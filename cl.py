import game as gam


apple_factory = gam.Factory('Apple Factory')

apple_tree = gam.Source('Apple Tree')
apple = gam.Product('Apple', 2)

tomato_plant = gam.Source('Tomato Plant')
tomato = gam.Product('Tomato', 2)

apple_factory.give(apple_tree, 1, 1)
apple_factory.give(tomato_plant, 1, 1)

print(apple_factory.storage)

# print(gam.Player.credits)
#print(gam.Source.collections)
print(apple_factory.sources)

