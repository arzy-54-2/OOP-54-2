# Инкапсуляция
import random
#
# class BankAccount:
#
#     def __init__(self, user, balance, password):
#         self.user = user # Открытый
#         self._balance = balance # Защищенный атрибут
#         self.__password = password # Приватный атрибут
#
#
#     def get_password(self):
#         return self.__password
#
#     def __generate_pass(self):
#         return random.randint(1, 100)
#
#     def reset_pass(self):
#         self.__password = self.__generate_pass()
#
#
# john = BankAccount("John", 1000, "123321")

# print(dir(john))


from abc import ABC, abstractmethod



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