import game as gam


apple_factory = gam.Factory('Apple Factory')

apple_tree = gam.Source('Apple Tree')

gam.Source.add_collection('tree')
apple_tree.add_to_collection('tree')

apple_factory.add_source(apple_tree, 1)

print(apple_factory.storage)

# print(apple_factory.storage)
# print(gam.Player.credits)
print(gam.Source.collections)
print(apple_factory.sources)
