from abc import ABC, abstractmethod


class Unit(ABC):

    @abstractmethod
    def attack(self):
        pass


class Archer(Unit):

    def attack(self):
        return "Arquero: Dispara flechas"


class Knight(Unit):

    def attack(self):
        return "Caballero: Ataca con su espada"


class Building(ABC):

    @abstractmethod
    def produce_unit(self):
        pass


class Barracks(Building):

    def produce_unit(self):
        return Knight()


class ArcheryRange(Building):

    def produce_unit(self):
        return Archer()


class GameFactory(ABC):

    @abstractmethod
    def create_unit(self):
        pass

    @abstractmethod
    def create_building(self):
        pass


class MedievalFactory(GameFactory):

    def create_unit(self):
        return Knight()

    def create_building(self):
        return Barracks()


class FantasyFactory(GameFactory):

    def create_unit(self):
        return Archer()

    def create_building(self):
        return ArcheryRange()
