from Src.reference import reference
from Src.exceptions import exception_proxy, argument_exception

class unit_model(reference):
    
    def __init__(self, name: str, base: reference = None, coeff: int = 1):
        super().__init__(name)
        self.__base_unit = base
        self.__coefficient = coeff if coeff > 0 else 1
        
    @property
    def base_unit(self) -> reference:
        return self.__base_unit

    @base_unit.setter
    def base_unit(self, value: reference):
        exception_proxy.validate(value, reference)
        self.__base_unit = value
        
    @property
    def coefficient(self):
        return self.__coefficient
    
    @coefficient.setter
    def coefficient(self, value: int):
        exception_proxy.validate(value, int)
        if value <= 0:
            raise argument_exception("Значение коэффициента должно быть > 0!")
        self.__coefficient = value  
    
    @classmethod
    def create_unit(cls, name: str, base=None, coeff=1):
        return cls(name, base, coeff)
    
    @staticmethod
    def create_gram():
        return unit_model("грамм")

    @staticmethod
    def create_kilogram():
        base = unit_model.create_gram()
        return unit_model("килограмм", base, 1000)
    
    @staticmethod
    def create_piece():
        return unit_model("штука")
    
    @staticmethod
    def create_milliliter():
        return unit_model("миллилитр")
    
    @staticmethod
    def create_liter():
        base = unit_model.create_milliliter()
        return unit_model("литр", base, 1000)
