
class car(object):
    def __init__(self,wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self. make = make
        self.model = model
        self.year =year
        self.sold_on = sold_on

    def sale_price(self):
        if self.sold_on is not None:
            return 0.0
        else:
            return 5000* self.wheels

    def purchase_price(self):
        if self.sold_on is not None:
            return 0.0
        else:
            return 8000 - (0.10 * self.miles)
