class Device(object):
    def __init__(self, name, ram, model):
        self.name = name
        self.ram = ram
        self.model = model

    def show_device(self):
        print(self.name, self.ram, self.model, self.type, sep=", ")

class Mobile(Device):
    def __init__(self, name, ram, model):
        super().__init__(name, ram, model)
        self.type = 'Mobile'

    def show_device(self):
        print(self.name, self.ram, self.model, self.type, sep=" = ")
        super().show_device()
        print(self.name, self.ram, self.model, self.type, sep=" => ")

class Laptop(Device):
    def __init__(self, name, ram, model):
        super().__init__(name, ram, model)
        self.type = 'Laptop'
        
class Tablet(Device):
    def __init__(self, name, ram, model):
        super().__init__(name, ram, model)
        self.type = 'Tablet'



if __name__ == "__main__":
    mobile = Mobile('Shailaja\'s Phone', '4GB', 'Samsung M30')
    laptop = Laptop('Hardik\'s laptop', '8GB', 'Surface Laptop 1')
    tablet = Tablet('Bhavik\'s tablet', '3GB', 'Ipad mini 2')

    mobile.show_device()
    laptop.show_device()
    tablet.show_device()