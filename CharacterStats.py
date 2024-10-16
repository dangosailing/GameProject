class CharacterStats:
    """
    Class to define character stats
    """

    def __init__(self, hp: int, attack: int, defense: int, agility: int) -> None:
        self.__hp = hp  # Character HP pool: trigger win or fail state for battle
        self.__attack = attack  # Character attack value: damage to hp = attack of character - def of opponent
        self.__defense = defense  # Character defense value: damage to hp = attack of character - def of opponent
        self.__agility = (
            agility  # Character agility value: determines who goes first in a round
        )

    def get_hp(self) -> int:
        """
        hp getter method
        """
        return self.__hp

    def set_hp(self, hp: int) -> None:
        """
        hp setter method
        """
        self.__hp = hp

    def get_attack(self) -> int:
        """
        attack getter method
        """
        return self.__attack

    def set_attack(self, attack: int) -> None:
        """
        attack setter method
        """
        self.__attack = attack

    def get_defense(self) -> int:
        """
        defense getter method
        """
        return self.__defense

    def set_defense(self, defense: int) -> None:
        """
        defense setter method
        """
        self.__defense = defense

    def get_agility(self) -> int:
        """
        agility getter method
        """
        return self.__agility

    def set_agility(self, agility: int) -> None:
        """
        agility setter method
        """
        self.__agility = agility
