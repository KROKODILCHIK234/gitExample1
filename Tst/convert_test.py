from src.logics.start_factory import StartFactory
from src.logics.convert_factory import ConvertFactory

import unittest
import json

class ConvertTest(unittest.TestCase):

    def test_convert_nomenclature(self):
        items = StartFactory.create_nomenclatures()
        factory = ConvertFactory()
        if not items:
            raise Exception("Список номенклатуры пуст!")
        
        item = items[0]
        
        result = factory.convert(item)
        
        self.assertIsNotNone(result)
        json_text = json.dumps(result, sort_keys=True, indent=4)
       
        with open("nomenclature.json", "w") as file:
            file.write(json_text)

    def test_convert_nomenclatures(self):
        items = StartFactory.create_nomenclatures()
        factory = ConvertFactory()
        
        result = factory.convert(items)
        
        self.assertIsNotNone(result)
        json_text = json.dumps(result, sort_keys=True, indent=4)
       
        with open("nomenclatures.json", "w") as file:
            file.write(json_text)
