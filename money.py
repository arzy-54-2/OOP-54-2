from abc import ABC

rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}

class Money:


    def __init__(self, amount,currency):
        self.amount = amount
        self.currency = currency.upper()


    def convert_to_kgs(self):
        if self.currency in rates.keys():
            return self.amount * rates[self.currency]
        else:
            return "Такой валюты нет"

    def __add__(self, other):
        return self.convert_to_kgs() + other.convert_to_kgs()

    def __sub__(self, other):
        if self.convert_to_kgs() >= other.convert_to_kgs():
            return self.convert_to_kgs() - other.convert_to_kgs()
        else:
            return other.convert_to_kgs() - self.convert_to_kgs()

    def __mul__(self, number):
        return self.convert_to_kgs() * number

    def __truediv__(self, num):
            return self.convert_to_kgs() / num

    def __str__(self):
        return f"{self.amount} {self.currency}"


money = Money(100, "RUB")
print(money)
#print(money.convert_to_kgs())

#money1 = Money(100, "USD")
#money2 = Money(5000, "eur")

#print(money1 - money2)
