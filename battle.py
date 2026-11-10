from character import Character


class Battle:
    """Manages a battle between two characters which is turn-based."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Storing the two characters which will battle each other."""
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Let the hero attack the enemy, and surviving enemy counterattack the hero."""
        if not self.hero.is_alive or not self.enemy.is_alive:
            return

        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Play rounds until one of the characters reaches 0 HP."""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()