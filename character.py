# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage

    def take_damage(self, amount:int) -> None:
        """Reduce the character's HP by a specified amount, down to a minimum of 0."""
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")
        self._hp = max(0, self._hp - amount)

    def heal(self, amount: int) -> None:
        """Restore the chracter's HP by a spexified amount, up to the maximum HP."""
        if amount < 0:
            raise ValueError("Heal amount cannot be negative.")
        self._hp = min(self.hp_max, self._hp + amount)

    def attack(self, target: "Character") -> None:
        """Attack and deal damage to the target character."""
        target.take_damage(self.damage)

    @property
    def is_alive(self) -> bool:
        """Return True while the character is alive (HP > 0), otherwise False."""
        return self._hp > 0


    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
