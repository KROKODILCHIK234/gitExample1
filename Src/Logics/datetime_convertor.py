class DateTimeConvertor(convertor):

    def convert(self, field: str, obj):
        super().convert(field, obj)
        
        if not isinstance(obj, datetime):
            self._error.error = f"Invalid data type for conversion. Expected: datetime. Received: {type(obj)}"
            return None
        
        try:
            formatted_datetime = obj.strftime('%Y-%m-%d %H:%M:%S')  
            return {field: formatted_datetime}
        except Exception as ex:
            self.set_error(ex)
