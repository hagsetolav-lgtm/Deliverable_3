# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from items import Weapon

class Character:
    """Represents a character in the RPG"""

    def __init__(
        self, 
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
    ) -> None:
        """Create a character with  full HP, base damage and an optional weapon."""
        if hp_max < 0:
            raise ValueError("Maximum HP cannot be negative.")
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

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
        """Attack another character using weapon damage or unarmed base damage."""
        if self.weapon is None:
            damage = self.damage
        else:
            damage = self.weapon.roll_damage()

        target.take_damage(damage)

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

class Warrior(Character):
    """A warrior who has armor which reduces incoming damage."""

    def __init__(
        self, 
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
        armor: int = 5,
    ) -> None:
        """Create a warrior with the given armor."""
        super().__init__(name, hp_max, damage, weapon)
        if armor < 0:
            raise ValueError("Armor value cannot be negative.")
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Apply the damage that gets through the armor to the warrior's HP."""
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")
        remaining_damage = max(0, amount - self.armor)
        super().take_damage(remaining_damage)


class Mage(Character):
    """A character who uses mana to cast spells."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
        mana: int = 30,
        mana_max: int = 30,
    ) -> None:
        """Create a mage with a given mana and a maximum mana amount."""
        super().__init__(name, hp_max, damage, weapon)
        if not 0 <= mana <= mana_max:
            raise ValueError("Mana must be between 0 and mana_max.")
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target: Character) -> None:
        """Cast a spell if enough mana is available, otherwise use base attack."""
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(2 * self.damage)
        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)