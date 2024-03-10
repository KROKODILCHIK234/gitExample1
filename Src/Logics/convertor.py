import abc
from Src.errors import ErrorProxy
from Src.exceptions import ExceptionProxy

class Convertor(ErrorProxy):
    
    @abc.abstractmethod
    def convert(self, field: str, obj) -> dict:
        """
        Convert the object to a dictionary.
        
        Args:
            field (str): The field name.
            obj (_type_): Any type of data.
        
        Returns:
            dict: The converted dictionary.
        """
        ExceptionProxy.validate(field, str)
        self.clear()
