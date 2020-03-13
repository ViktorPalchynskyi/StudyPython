from random import random
from typing import Optional, Any, Union, List, Tuple, Dict, Iterable


class Character:

    def __init__(self, armor: int, power: int):
        self.power = power
        self.armor = armor
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0


c1 = Character(10, 20)

c1.hit(20)

amount: int
amount = None

price: Optional[int]
price = 10
price = None
price = 'asdf'

attack: Any = 1
attack = 'hi'

length: Union[int, float]

length = 1
length = 2.2
length = 'asdf'

quotes: list
quotes = '1adf'

quotes: List[int]  # Set, FrozenSet

quotes.append(1)
quotes.append('asdf')

player: Tuple[str, int] = ("kramnik", 2750)

changes_in_rating: Tuple[int, ...]
changes_in_rating = (1, 2, 3, 4)

changes_in_rating = (1, 'asdf')

chess_players: Dict[str, int] = {'Kramnik': 2750}


def random_stream(min_val: int, max_val: int) -> Iterable[int]:

    while True:
        yield random.randint(min_val, max_val)
        