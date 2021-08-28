class product:
    deliveryCharge=50
    def __init__(self,nam="Teddy Bear", prc=500):
        self.name=nam
        self.price=prc
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price + product.deliveryCharge
    def __str__(self):
        return "The {} will cost you Rs.{}.".format(self.get_name(),self.get_price())

class gift(product):
    wrappingCharge=100
    def __init__(self, nam, prc):
        super().__init__(nam, prc)
    def get_price(self):
        return self.price + product.deliveryCharge + gift.wrappingCharge

p1 = product('abc', 1000)
print("total price for {} is {}".format (p1.get_name(), p1.get_price()))
g1 = gift('abc', 1500)
print("total price for {} is {}".format (p1.get_name(), p1.get_price()))
