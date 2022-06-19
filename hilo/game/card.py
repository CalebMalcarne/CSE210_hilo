#Code by Caleb Malcarne
import random

class Card():
    #constructs new Card
    #initalisez _value with 0
    def __init__(self):
        self._value = 0

    #picks a random number from 1- 13 and store it in _value
    def draw_Card(self):
        self._value = random.randint(1,13)
        return self._value