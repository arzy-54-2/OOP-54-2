from django.db.models.expressions import result
rates = {
    "KGS":1,
    "USD":89,
    "EUR":96,
    "RUB":1.2
}


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    #  В сомы
    def convert_to_kgs(self):
        return self.amount*rates[self.currency]

    # сложение
    def __add__(self,other):
        total = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total, "KGS")
    # -
    def __sub__(self,other):
        total = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total, "KGS")
    # *
    def __mul__(self,number):
        return Money(self.amount * number, self.currency)
    # /
    def __truediv__(self,number):
        return Money(self.amount / number, self.currency)


    def __str__(self):
        return f"{round(self.amount,2)} {self.currency}"



money1 = Money(100,"USD")
money2 = Money(5002, "KGS")

result = money1 + money2

print(result)

