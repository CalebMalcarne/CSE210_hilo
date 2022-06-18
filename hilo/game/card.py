import random

class Card():
    def __init__(self):
        self._value = 0

    def draw_Card(self):
        self._value = random.randint(1,13)