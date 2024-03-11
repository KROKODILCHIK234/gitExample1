class storage:
    __data = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance

    @property
    def data(self) -> dict:
        return self.__data

    @staticmethod
    def nomenclature_key():
        return "nomenclatures"

    @staticmethod
    def group_key():
        return "groups"

    @staticmethod
    def unit_key():
        return "units"

    @staticmethod
    def receipt_key():
        return "receipts"

    @classmethod
    def get_all_keys(cls):
        keys = []
        methods = [getattr(cls, method) for method in dir(cls) if callable(getattr(cls, method))]
        for method in methods:
            if method.__name__.endswith("_key") and callable(method):
                keys.append(method())
        return keys
    
