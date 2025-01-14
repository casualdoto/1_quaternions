# 1_quaternions
группа 5130203/20101

casualdoto - Хрестьяновский Даниил

Tonya-Lyub - Антонина Любецкая

shmel9va - Шмелева Мария

Репозитории с задачами:

1_quaternions - https://github.com/casualdoto/1_quaternions

1_caching_decorator - https://github.com/casualdoto/1_caching_decorator

1_figures - https://github.com/casualdoto/1_figures

# Кватернионы: Операции и Повороты

Этот проект предоставляет реализацию кватернионов в Python, включая основные операции над ними и функции для поворота векторов в пространстве.

## Структура проекта

```
project_root/
├── Quanterion.py # Реализация класса Quaternion
└── main.py # Пример использования кватернионов
```

## Возможности

- **Арифметические операции**:
  - Сложение (`+`)
  - Вычитание (`-`)
  - Умножение (`*`)
  - Деление (`/`)
- **Другие функции**:
  - Вычисление модуля (`abs`)
  - Сопряжение
  - Обратный кватернион
  - Поворот векторов в пространстве

## Примеры использования

### Арифметические операции
```python
from Quanterion import Quaternion

q1 = Quaternion(1, 2, 3, 4)
q2 = Quaternion(0.5, 1.5, -2, 3)

print("Кватернион 1:", q1)
print("Кватернион 2:", q2)
print("Сумма:", q1 + q2)
print("Разность:", q1 - q2)
print("Умножение:", q1 * q2)
print("Деление:", q1 / q2)

### Поворот вектора
```python
q1 = Quaternion(1, 2, 3, 4)
vector = (1, 0, 0)
rotated_vector = q1.rotate_vector(vector)

print("Поворот вектора (1, 0, 0):", rotated_vector)

## Запуск проекта

### Установка

**Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/casualdoto/1_quaternions
   cd project_root
   ```
### Запуск проекта

**Запустите файл main.py для демонстрации возможностей класса:**:
```python
python main.py

