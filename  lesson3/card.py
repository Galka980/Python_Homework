class Card:
    number = "0000 0000 0000 0000"
    validData = (11/28)
    holder = "unknown"

    def __init__(self, number, data, holder):
        self.number = number
        self.validData = data
        self.holder = holder

    def pay (self, amount):
            print("с карты",self.number, "списали", amount)


