# class is grup of attribut(veriable) and mathod
'''Class Class_Name(object): # object is reprasant base class nd is optional
    def __init__(self, perameters): # add to mathod nd attribut #__init__ variable insilation mathod
        self.variable_name = value
        self.variable_name = 'value'  

    def mathod_name(self):
        body of mathod      #self = veriable 

#class name is capitalization
    def mathod_name(self):
        body of mathod '''


class Mobile:
    def __init__(self, m):
        self.model = m

    def show_model(self, p):
        price = p
        print('model: ', self.model, 'price: ', price)

realme = Mobile('Realme X')
realme.show_model(1000)
Realmi = Mobile('Redmi 7s')
Realmi.show_model(2000)
samsung = Mobile('samsung M30')
samsung.show_model(10000)
















    







        
