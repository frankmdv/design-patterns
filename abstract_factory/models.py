from abc import ABC, abstractmethod


class GameFactory(ABC):
    @abstractmethod
    def create_knight(self):
        pass

    @abstractmethod
    def create_archer(self):
        pass

    @abstractmethod
    def create_wizard(self):
        pass


class MedievalFactory(GameFactory):
    def create_knight(self):
        return MedievalKnight()

    def create_archer(self):
        return MedievalArcher()

    def create_wizard(self):
        return MedievalWizard()


class FantasyFactory(GameFactory):
    def create_knight(self):
        return FantasyKnight()

    def create_archer(self):
        return FantasyArcher()

    def create_wizard(self):
        return FantasyWizard()


class Knight:
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


class MedievalKnight(Knight):
    def attack(self):
        return "El caballero blande su espada de obsdiana y ataca"

    def move(self):
        return "El caballero se mueve por el terreno de batalla"


class FantasyKnight(Knight):
    def attack(self):
        return "El caballero lanza un ataque con su espada de fuego"

    def move(self):
        return "El caballero fantástico se teletransporta por el terreno de batalla"


class Archer:
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def disappear(self):
        pass


class MedievalArcher(Archer):
    @abstractmethod
    def attack(self):
        return "El arquero lanza una flecha de piedra"

    @abstractmethod
    def disappear(self):
        return "¡El Arquero Medieval desaparece en la niebla como un fantasma!"


class FantasyArcher(Archer):
    @abstractmethod
    def attack(self):
        return "El arquero lanza una flecha de fuego"

    @abstractmethod
    def disappear(self):
        return "¡El Arquero Fantástico se desvanece en una nube de energía mágica!"


class Wizard:
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MedievalWizard(Wizard):
    def attack(self):
        return "El mago lanza un rayo de energía mágica desde su varita, que impacta en su enemigo causándole un gran daño."

    def fly(self):
        return "¡El Mago Medieval extiende sus alas y se eleva en el aire!"


class FantasyWizard(Wizard):
    def attack(self):
        return "El mago conjura una bola de fuego ardiente que explota al impactar en el objetivo, causando daño en un área amplia"

    def fly(self):
        return "¡El Mago Fantástico canaliza la energía mágica y se eleva en el aire como un verdadero maestro de los elementos!"
