

def get_item(items, x):
    if x >= len(items) or x < 0:
        return None
        
    return items[x]


	
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x)) #"roo"

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x)) # None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 3
print(get_item(items, x)) # rabbit


