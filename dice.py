import random

class Dice:
    """Represents a dice with a specified number of sides."""

    def __init__(self, sides: int=6) -> None:
        """Create a dice with at least two sides."""
        if not isinstance(sides, int):
            raise TypeError("Number of sides must be an integer.")
        if sides < 2:
            raise ValueError("A dice must have  at least two sides.")
        self.sides = sides

    def roll(self) -> int:
        """Return a random integer between 1 and the number of sides (inclusive)."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Return a string showing the numbers of sides on the dice."""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Roll the dice when the object is called."""
        return self.roll()