class Person(object):
    '''
    Pass following arguments
    name: Name of person
    age: age or person
    sex: Male or Female
    '''
    def __init__(self, name='', age=25, sex="Male"):
        # Initialize all the attributes
        self.name = name
        self.age = age
        self.sex = sex
        print("Initialization is done")

    @property
    def is_male(self):
        if self.sex == 'Male':
            return True
        return False

class Employee(Person):
    def __init__(self, name='', age=25, sex="Male"):
        self.post = "Employee"

        super().__init__(name=name, age=age, sex=sex)

class Manager(Person):
    def __init__(self, name='', age=25, sex="Male"):
        self.post = "Manager"

        super().__init__(name=name, age=age, sex=sex)


hardik = Employee(name="Hardik", age=29, sex="Male")
shailaja = Manager()
shailaja.sex = 'Female'
shailaja.name = "Shailaja"
shailaja.age = 28
shailaja.abcd = 10

print(shailaja.name, shailaja.age, shailaja.sex, shailaja.is_male, shailaja.post)
print(hardik.name, hardik.age, hardik.sex, hardik.is_male, hardik.post)