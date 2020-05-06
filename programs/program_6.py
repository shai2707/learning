
class Brand:
    def __init__(self, name, owner):
        self.owner = owner
        self.name = name
        self.famous = True

    def __str__(self):
        return self.name + ' owned by ' + self.owner

    def __repr__(self):
        return '<object of {"name":'+ self.name + '}>'

class Tyre:
    def __init__(self, count, spare=True):
        self.count = count
        self.spare = spare

    def __str__(self):
        return str(self.count) + ' tyres'

class Vehicle:
    def __init__(self, brand, value, color, tyre):
        self.brand = Brand(name=brand, owner="Hardik")
        self.value = value
        self.color = color
        self.tyre = Tyre(count=tyre)

    def to_dict(self):
        return {
            'brand': self.brand.__dict__,
            'value': self.value,
            'color': self.color,
            'tyre': self.tyre.__dict__
        }

class Car(Vehicle):
    def __init__(self, brand, value, color, tyre=4):
        super().__init__(brand, value, color, tyre)

class Auto(Vehicle):
    def __init__(self, brand, value, color, tyre=3):
        super().__init__(brand, value, color, tyre)


auto = Auto('Tata', 100000, 'black')
print(auto.brand, auto.value, auto.color, auto.tyre, auto.brand.owner)
print(auto.to_dict())
print(auto.__dict__)

amaze = Car('Honda', 780000, 'golder brown')
print(amaze.brand, amaze.value, amaze.color, amaze.tyre, amaze.tyre.spare)
print(amaze.to_dict())