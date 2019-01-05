class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_card(self):
        return self.suit, self.value

    def to_string(self):
        return str(self.value) + self.suit + ' '