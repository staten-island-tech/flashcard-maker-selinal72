class Merchant:
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)
Joanna = Merchant("Joanna", ['Chicken', 'john pork','beef'])
Joanna.sell('john pork')
Alvin = Merchant("Alvin", ["Human", "Alvin's Servitude", "Breaks", "Organs"])
Alvin.sell("Human")