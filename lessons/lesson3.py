# Инкапсуляция
import random
#
class BankAccount:

    count = 0

    def __init__(self, user: str, balance, password):
        self.user = user # Открытый
        self._balance = balance # Защищенный атрибут
        self.__password = password # Приватный атрибут
        self.count += 1


    def get_password(self):
        return self.__password

    def __generate_pass(self):
        return random.randint(1, 100)

    def reset_pass(self):
        self.__password = self.__generate_pass()


john = BankAccount(123, 123, 123)

print(dir(john))


from abc import ABC, abstractmethod


test()
# Абстрактный класс
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        """

        """

        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def __init__(self, name):
        self.name =name

    def make_sound(self):
        return print(f"{self.name} Gaf gaf")

    def move(self):
        return print(f"{self.name} move")

tuzik = Dog("Tuzik")
print(tuzik.name)
#


class SmsSend:

    @abstractmethod
    def send_otp_cod(self):
        """
        Вам нужно будет реализовать логику отправки смс для вашей страны
        :return: смс
        """
        pass



class KGSmsSend(SmsSend):
    def send_otp_cod(self):
        pass

# исправил ошибку









# staticmethod (статический метод) — это метод, который не требует доступа к экземпляру или
# классу. Он ведет себя как обычная функция, но внутри класса.


class MathUtils:

    @staticmethod
    def add(a,b):
        return a + b


# print(MathUtils.add(33,77))

# class Person:
#     count = 12
#
#     def __init__(self, num):
#         self.num = num
#
#     @classmethod
#     def test(cls):
#         return f"{cls.count}"


# print(Person.test())




class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def get_name(self):
        return self.name


person = Person("add", 33)

# print(person.get_name)

data = {
    "first": 123,
    "second": 321
}

print(data.get("firsts", "my"))
