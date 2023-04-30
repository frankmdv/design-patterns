class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = "Llamar al método que devuelve la instancia de la clase"

        return cls._instance
