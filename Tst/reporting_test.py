import unittest
from Src.Logics.reporting import reporting
from Src.Models.unit_model import unit_model
from Src.Storage.storage import storage
from Src.Logics.csv_reporting import csv_reporting
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.group_model import group_model
from Src.Logics.markdown_reporting import markdown_reporting
from Src.Logics.json_reporting import json_reporting

class ReportingTest(unittest.TestCase):
    
    def test_json_reporting_build(self):
        # Preparation
        data = {storage.unit_key(): [unit_model.create_gram()]}
        report = json_reporting(data)
        
        # Action
        result = report.create(storage.unit_key())
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)   
    
    def test_reporting_build(self):
        # Preparation
        data = {storage.unit_key(): [unit_model.create_gram()]}
        
        # Action
        result = reporting.build(storage.unit_key(), data)
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
    def test_csv_create_unit_key(self):
        # Preparation
        data = {storage.unit_key(): [unit_model.create_gram()]}
        report = csv_reporting(data)
        
        # Action
        result = report.create(storage.unit_key())
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
    def test_csv_create_nomenclature_key(self):
        # Preparation
        data = {
            storage.nomenclature_key(): [nomenclature_model("Тушка бройлера", group_model.create_default_group(), unit_model.create_killogram())]
        }
        report = csv_reporting(data)
        
        # Action
        result = report.create(storage.nomenclature_key())
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
        with open("csv_report.csv", "w") as file:
            file.write(result)
        
    def test_markdown_create_unit_key(self):
        # Preparation
        data = {storage.unit_key(): [unit_model.create_gram()]}
        report = markdown_reporting(data)
        
        # Action
        result = report.create(storage.unit_key())
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
        with open("markdown_report.md", "w") as file:
            file.write(result)
