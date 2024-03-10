from Src.Logics.convertor import Convertor

class BasicConvertor(Convertor):
   
    def convert(self, field: str, obj) -> dict:
        super().convert(field, obj)
      
        if not isinstance(obj, (int, str, bool)):
            self._error.error = f"Некорректный тип данных передан для конвертации. Ожидается: (int, str, bool). Передан: {type(obj)}"
            return None
      
        try:
            return {field: obj}
        except Exception as ex:
            self._error.set_error(ex)
            return None
