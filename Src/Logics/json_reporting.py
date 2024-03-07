from Src.Logics.reporting import reporting
from Src.exceptions import operation_exception
from Src.reference import reference
import json

class json_reporting(reporting):
    
    def create(self, typeKey: str):
        super().create(typeKey)
        result = []
        
        # Исходные данные
        items = self.data[typeKey]
        if items is None:
            raise operation_exception("Данные не заполнены!")
        
        if len(items) == 0:
            raise operation_exception("Нет данных!")
        
        for item in items:
            data = {}  
            for field in self.fields:
                value = getattr(item, field)
                data[field] = value
            
            result.append(data)
        
        data_json = json.dumps(result)
        return data_json
