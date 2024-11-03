import Quanterion
# Пример использования:
q1 = Quanterion.Quaternion(1, 2, 3, 4)
q2 = Quanterion.Quaternion(0.5, 1.5, -2, 3)

print("Кватернион 1:", q1)
print("Кватернион 2:", q2)
print("Сумма:", q1 + q2)
print("Разность:", q1 - q2)
print("Умножение 1 на 2:", q1 * q2)
print("Умножение 2 на 1:", q2 * q1)
print("Модуль кватерниона 2:", abs(q2))
print("Сопряжение кватерниона 2:", q2.conjugate())
print("Обратный квантерниону 2:", q2.inverse())
print("Деление 1 на 2:", q1/q2)
print("Деление 2 на 1:", q2/q1)
