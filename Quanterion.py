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
