from Src.reference import reference
from Src.Storage.storage import storage
from Src.Models.storage_turn_model import storage_turn_model
class process_storage_turn():
    @staticmethod
    def calculate(transactions: reference):
        result = {}
        turns = []
        for transaction in transactions:
            key = (transaction.nomenclature, transaction.storage, transaction.unit)
            size = transaction.size * transaction.type.type
            if key in result.keys():
                result[key] += size
            else:
                result[key] = size
        for k, v in result.items():
            turn = storage_turn_model.create(k[1], v, key[0], k[2])
            turns.append(turn)
        return turns
        

class process_factory:
    __maps = {}
    def __init__(self):
        self.__build()
    
    def __build(self):
        self.__maps[storage.process_turn_key()] = process_storage_turn

    def create_turns(self, key):
        if key not in self.__maps.keys():
            raise Exception("Нет обработчика для ", key)
        result = self.__maps[key]()

        return result
    
