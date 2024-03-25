from Src.Logics.storage_service import storage_service
import unittest
from datetime import datetime
from unittest.mock import Mock

class TestStorageService(unittest.TestCase):
    def setUp(self):
        # Устанавливаем начальные данные для тестов
        self.data = [{"date": "2024-03-19", "value": 100}, {"date": "2024-03-20", "value": 150}]
        self.storage = storage_service(self.data)

    def test_create_turns(self):
        # Проверяем, что create_turns возвращает ожидаемый результат
        start_period = datetime(2024, 3, 19)
        stop_period = datetime(2024, 3, 20)
        result = self.storage.create_turns(start_period, stop_period)
        self.assertEqual(result, {"2024-03-19": 100, "2024-03-20": 150})

    def test_create_turns_invalid_parameters(self):
        # Проверяем, что create_turns вызывает исключение при некорректных параметрах
        start_period = datetime(2024, 3, 20)
        stop_period = datetime(2024, 3, 19)
        with self.assertRaises(argument_exception):
            self.storage.create_turns(start_period, stop_period)

    def test_create_response(self):
        # Проверяем, что create_response форматирует данные корректно
        mock_app = Mock()
        result = storage_service.create_response(self.data, mock_app)
        self.assertEqual(result.status, 200)
        self.assertEqual(result.mimetype, "application/json; charset=utf-8")
        self.assertIn("2024-03-19", result.response)
        self.assertIn("2024-03-20", result.response)
        self.assertIn("100", result.response)
        self.assertIn("150", result.response)

if __name__ == '__main__':
    unittest.main()
