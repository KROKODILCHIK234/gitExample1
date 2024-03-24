from Src.exceptions import argument_exception
from Src.errors import error_proxy
from datetime import datetime

#
# Прототип для обработки складских транзакций
#
class storage_prototype(error_proxy):
    __data = []
    
    def __init__(self, data: list) -> None:
        if len(data) <= 0:
            self.error = "Набор данных пуст!"
        
        self.__data = data

    def filter(self, start_period: datetime, stop_period: datetime, nomenclature: str = None):
        """
        Фильтрует данные по заданному периоду и номенклатуре.
        
        Args:
            start_period (datetime): Начало периода
            stop_period (datetime): Конец периода
            nomenclature (str, optional): Номенклатура, которую необходимо показать. По умолчанию None.
        
        Returns:
            storage_prototype: Новый экземпляр прототипа с отфильтрованными данными.
        """
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"
            
        if start_period > stop_period:
            self.error = "Некорректный период!"
            
        if not self.is_empty:
            return self.__data
        
        result = []
        for item in self.__data:
            if item.period > start_period and item.period <= stop_period:
                if nomenclature is None or item.nomenclature == nomenclature:
                    result.append(item)
                
        return storage_prototype(result)
    
    @property
    def data(self):
        """
        Полученные данные
        Returns:
        list: Список данных
        """
        return self.__data  
