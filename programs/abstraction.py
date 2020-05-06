from abc import abstractmethod, ABCMeta

class Parent(object):

    @abstractmethod
    def show_properties(self):
        raise NotImplementedError

class Child(Parent):
    def __init_subclass__(self):
        pass

    def __init__(self):
        pass

c = Child()
c.show_properties()