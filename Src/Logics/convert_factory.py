from Src.Logics.basic_convertor import BasicConvertor
from Src.Logics.datetime_convertor import DatetimeConvertor
from Src.exceptions import ExceptionProxy, OperationException
from Src.reference import Reference
from Src.Logics.convertor import Convertor

import datetime

class ReferenceConvertor(Convertor):
    
    def convert(self, field: str, obj) -> dict:
        factory = ConvertFactory()
        return factory.convert(obj)
    

class ConvertFactory:
    _maps = {}
    
    def __init__(self) -> None:
        self._maps[datetime.datetime] = DatetimeConvertor
        self._maps[dict] = BasicConvertor
        self._maps[int] = BasicConvertor
        self._maps[str] = BasicConvertor
        self._maps[bool] = BasicConvertor
        
        for inheritor in Reference.__subclasses__():
            self._maps[inheritor] = ReferenceConvertor
    
        
    def convert(self, obj) -> dict:
        result = self.__convert_list("data", obj)
        if result is not None:
            return result
        
        result = {}
        fields = Reference.create_fields(obj)
        
        for field in fields:
            attribute = getattr(obj.__class__, field)
            if isinstance(attribute, property):
                value = getattr(obj, field)
                
                dictionary = self.__convert_list(field, value)
                if dictionary is None:
                    dictionary = self.__convert_item(field, value)
                    
                if len(dictionary) == 1:
                    result[field] = dictionary[field]
                else:
                    result[field] = dictionary       
          
        return result  
    
    def __convert_item(self, field: str, source):
        ExceptionProxy.validate(field, str)
        if source is None:
            return {field: None}
        
        if type(source) not in self._maps.keys():
            raise OperationException(f"Не возможно подобрать конвертор для типа {type(source)}")

        convertor = self._maps[type(source)]()
        dictionary = convertor.convert(field, source)
        
        if not convertor.is_empty:
            raise OperationException(f"Ошибка при конвертации данных {convertor.error}")
        
        return  dictionary
            
    def __convert_list(self, field: str, source) -> list:
        ExceptionProxy.validate(field, str)
        if not isinstance(source, list):
            return None
        
        items = []
        for item in source:
            items.append(self.__convert_item(field, item))  
        
        return items
