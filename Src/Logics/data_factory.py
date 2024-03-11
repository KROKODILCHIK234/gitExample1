from Logics.data_presentation import convert
from  Logics.Formats.data_csv import csv_convert
from Logics.Formats.data_markdown import markdown_convert
from Logics.Formats.data_json import json_convert
from Logics.Formats.data_csv import csv_convert
from Logics.Formats.data_markdown import markdown_convert
from Src.errors import exception_proxy, argument_exception, operation_exception

class data_factory:
    __maps = {}

    def __init__(self) -> None:
        self.__build_structure()

    def __build_structure(self):
        self.__maps["csv"] = csv_convert
        self.__maps["markdown"] = markdown_convert
        self.__maps["json"] = json_convert


    def create(self, format: str, data) -> convert:
        exception_proxy.is_valide(format, str)
        if data is None:
            raise argument_exception("Данные не переданы")

        if len(data) == 0:
            raise argument_exception("Пустые данные")

        if format not in self.__maps.keys():
            operation_exception("Неверная операция ")



        convert_type = self.__maps[format]
        result = convert_type(data)
        return result
