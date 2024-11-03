import math


class Quaternion:
    def __init__(self, w, x, y, z):
        """
        Инициализация кватерниона.
        :param w: скалярная часть
        :param x: векторная часть x
        :param y: векторная часть y
        :param z: векторная часть z
        """
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """
        Представление кватерниона в читаемом формате.
        """
        return f"Quaternion({self.w}, {self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        """
        Операция сложения двух кватернионов.
        :param other: другой кватернион
        :return: новый кватернион, являющийся результатом сложения
        """
        return Quaternion(
            self.w + other.w,
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        """
        Операция вычитания двух кватернионов.
        :param other: другой кватернион
        :return: новый кватернион, являющийся результатом вычитания
        """
        return Quaternion(
            self.w - other.w,
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__(self, other):
        """
        Операция умножения двух кватернионов.
        """
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y + self.y * other.w + self.z * other.x - self.x * other.z
        z = self.w * other.z + self.x * other.y + self.z * other.w - self.y * other.x
        return Quaternion(w, x, y, z)

    def __abs__(self):
        """
        Вычисление модуля кватерниона.
        """
        return math.sqrt(self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2)

    def conjugate(self):
        """
        Вычисление сопряжения кватерниона.
        """
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def inverse(self):
        """
        Вычисление обратного кватерниона.
        """
        mod_squared = abs(self) ** 2
        conjugate = self.conjugate()
        return Quaternion(
            conjugate.w / mod_squared,
            conjugate.x / mod_squared,
            conjugate.y / mod_squared,
            conjugate.z / mod_squared
        )

    def __truediv__(self, other):
        """
        Переопределение оператора деления для кватернионов.
        Деление одного кватерниона на другой реализовано как умножение на обратный кватернион.
        """
        return self * other.inverse()
