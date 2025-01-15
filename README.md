# 1_quaternions
группа 5130203/20101

casualdoto - Хрестьяновский Даниил

Tonya-Lyub - Антонина Любецкая

shmel9va - Шмелева Мария

**Репозитории с задачами**:

1_quaternions - https://github.com/casualdoto/1_quaternions

1_caching_decorator - https://github.com/casualdoto/1_caching_decorator

1_figures - https://github.com/casualdoto/1_figures

**Репозиторий с курсовой работой**:

SPBPU_python_final_task - https://github.com/casualdoto/SPBPU_python_final_task

# Кватернионы: Операции и Повороты

Этот проект предоставляет реализацию кватернионов в Python, включая основные операции над ними и функции для поворота векторов в пространстве.

## Структура проекта

```
project_root/
├── quaternion.py # Реализация класса Quaternion
├── test_quaternion.py # Тесты для проекта
└── reqirements.txt # Требования для проекта
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

## Запуск

Настройте виртуальное окружение:

1. Откройте терминал или командную строку.

2. Клонируйте репозиторий:
```bash
git clone https://github.com/casualdoto/1_quaternions
```

3. Перейдите в директорию проекта:
```bash
cd путь/к/проекту
```

4. Создайте виртуальное окружение:
```bash
python -m venv venv
```

5. Активируйте виртуальное окружение:
```bash
venv\\Scripts\\activate
```

6. Установите зависимости:
```bash
pip install -r requirements.txt
```

7. Запустите тесты:
```bash
pytest test_quaternion.py
```

## Тестирование

Тесты для этого проекта находятся в файле `test_quaternion.py` и используют `pytest`. Они покрывают следующие сценарии:

1. **Арифметические операции:** Проверяется корректность выполнения операций сложения, вычитания, умножения и деления между кватернионами.

2. **Модуль и сопряжение:** Убеждается, что модуль кватерниона рассчитывается правильно, а операция сопряжения возвращает ожидаемый результат.

3. **Обратный кватернион:** Тестируется правильность вычисления обратного кватерниона и его использование в делении.

4. **Поворот вектора:** Проверяется, что функция поворота вектора с использованием кватерниона работает корректно и возвращает правильный результат.

5. **Строковое представление:** Проверяется, что метод `__repr__` возвращает строку, корректно представляющую кватернион.



## Примеры использования

### Арифметические операции
```python
from quaternion import Quaternion

q1 = Quaternion(1, 2, 3, 4)
q2 = Quaternion(0.5, 1.5, -2, 3)

print("Кватернион 1:", q1)
print("Кватернион 2:", q2)
print("Сумма:", q1 + q2)
print("Разность:", q1 - q2)
print("Умножение:", q1 * q2)
print("Деление:", q1 / q2)
```

### Поворот вектора
```python
q1 = Quaternion(1, 2, 3, 4)
vector = (1, 0, 0)
rotated_vector = q1.rotate_vector(vector)

print("Поворот вектора (1, 0, 0):", rotated_vector)
```

