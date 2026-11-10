from dice import Dice

class Weapon:
    """Represents a weapon that uses dice to determine damage."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Create a weapon with a name and a damage dice."""
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's damage dice and return the damage value."""
        return self.damage_dice.roll()