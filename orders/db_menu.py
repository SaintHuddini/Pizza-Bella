"""
Foods in the database and how I did it inte the shell
"""
from orders.models import Recipe


salad = [
    {'name': 'Garden Salad', 'category': 'SALLAD', 'price': 7.55},
    {'name': 'Greek Salad', 'category': 'SALLAD', 'price': 9.75},
    {'name': 'Antipasto', 'category': 'SALLAD', 'price': 7.45},
    {'name': 'Salad w/Tuna', 'category': 'SALLAD', 'price': 8.95},
]

for fresh in salad:
    name = fresh.get('name')
    price = fresh.get('price')
    category = fresh.get('category')
    new = Recipe(name=name, price=price, category=category)
    new.save()

# PASTA
pasta = [
    {'name': 'Baked Ziti w/ Mozzarella', 'category': 'PASTA', 'price': 6.90},
    {'name': 'Baked Ziti w/ Meatballs', 'category': 'PASTA', 'price': 7.85},
    {'name': 'Baked Ziti w/ Chicken', 'category': 'PASTA', 'price': 5.85},
]

for oat in pasta:
    name = oat.get('name')
    category = oat.get('category')
    price = oat.get('price')
    new = Recipe(name=name, price=price, category=category)
    new.save()

# Kebab
kebab = [
    {'name': 'Shish Kebab', 'category': 'KEBAB', 'price': 8.90},
    {'name': 'Kebab with pita bread', 'category': 'KEBAB', 'price': 7.85},
    {'name': 'Kebab with fries', 'category': 'KEBAB', 'price': 5.85},
]

for meat in kebab:
    name = meat.get('name')
    category = meat.get('category')
    price = meat.get('price')
    new = Recipe(name=name, price=price, category=category)
    new.save()


# Hamburgers
hamburger = [
    {'name': 'New York 90g w/ fries ', 'category': 'HAMBURGER', 'price': 8.90},
    {'name': 'New York 160g w/ fries', 'category': 'HAMBURGER', 'price': 7.85},
    {'name': 'New York 220g w/ fries ', 'category': 'HAMBURGER', 'price': 5.85},
    {'name': 'Texas Ranger 90g w/ fries ', 'category': 'HAMBURGER', 'price': 8.90},
    {'name': 'Texas Ranger 160g w/ fries', 'category': 'HAMBURGER', 'price': 7.85},
    {'name': 'Texas Ranger 220g w/ fries ', 'category': 'HAMBURGER', 'price': 5.85},
    {'name': 'Mexican 90g w/ fries ', 'category': 'HAMBURGER', 'price': 8.90},
    {'name': 'Mexican 160g w/ fries', 'category': 'HAMBURGER', 'price': 7.85},
    {'name': 'Mexican 220g w/ fries ', 'category': 'HAMBURGER', 'price': 5.85},
    {'name': 'Tripple Cheese 90g w/ fries ',
     'category': 'HAMBURGER', 'price': 8.90},
    {'name': 'Tripple Cheese 160g w/ fries',
     'category': 'HAMBURGER', 'price': 7.85},
    {'name': 'Tripple Cheese 220g w/ fries ',
     'category': 'HAMBURGER', 'price': 5.85},
    {'name': 'London Burger 90g w/ fries ',
     'category': 'HAMBURGER', 'price': 8.90},
    {'name': 'London Burger 160g w/ fries', 'category': 'HAMBURGER', 'price': 7.85},
    {'name': 'London Burger 220g w/ fries ',
     'category': 'HAMBURGER', 'price': 5.85},
]

for meat in hamburger:
    name = meat.get('name')
    category = meat.get('category')
    price = meat.get('price')
    new = Recipe(name=name, price=price, category=category)
    new.save()


pizza = [
    {'name': 'Margherita - Standard', 'category': 'PIZZA', 'price': 4.90},
    {'name': 'Margherita - Family', 'category': 'PIZZA', 'price': 7.90},
    {'name': 'Marinara - Small', 'category': 'PIZZA', 'price': 4.85},
    {'name': 'Marinara - Family', 'category': 'PIZZA', 'price': 7.85},
    {'name': 'Frutti di Mare - Standard', 'category': 'PIZZA', 'price': 5.85},
    {'name': 'Frutti di Mare - Family ', 'category': 'PIZZA', 'price': 8.85},
    {'name': 'Quattro Formaggi - Standard', 'category': 'PIZZA', 'price': 5.85},
    {'name': 'Quattro Formaggi - Family', 'category': 'PIZZA', 'price': 8.85},
    {'name': 'Pugliese - Standard', 'category': 'PIZZA', 'price': 5.55},
    {'name': 'Pugliese - Family', 'category': 'PIZZA', 'price': 8.55},
    {'name': 'Montanara - Standard', 'category': 'PIZZA', 'price': 4.95},
    {'name': 'Montanara - Family', 'category': 'PIZZA', 'price': 7.95},
    {'name': 'Emiliana - Standard', 'category': 'PIZZA', 'price': 5.25},
    {'name': 'Emiliana - Family ', 'category': 'PIZZA', 'price': 8.25},
    {'name': 'Romana - Standard', 'category': 'PIZZA', 'price': 5.35},
    {'name': 'Romana - Family', 'category': 'PIZZA', 'price': 8.35},
    {'name': 'Fattoria - Standard', 'category': 'PIZZA', 'price': 5.55},
    {'name': 'Fattoria - Family', 'category': 'PIZZA', 'price': 8.55},
    {'name': 'Schiacciata - Standard', 'category': 'PIZZA', 'price': 6.00},
    {'name': 'Schiacciata - Family', 'category': 'PIZZA', 'price': 9.00},
    {'name': 'Cardinale - Standard', 'category': 'PIZZA', 'price': 6.25},
    {'name': 'Cardinale - Family', 'category': 'PIZZA', 'price': 9.25},
    {'name': 'Americana - Standard', 'category': 'PIZZA', 'price': 6.25},
    {'name': 'Americana - Family', 'category': 'PIZZA', 'price': 9.55},
    {'name': 'Prosciutto e Funghi - Standard', 'category': 'PIZZA', 'price': 5.85},
    {'name': 'Prosciutto e Funghi - Family', 'category': 'PIZZA', 'price': 8.85}
]

for cheese in pizza:
    name = cheese.get('name')
    category = cheese.get('category')
    price = cheese.get('price')
    new = Recipe(name=name, price=price, category=category)
    new.save()
