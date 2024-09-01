# Проект Ульяна Рогова Домашняя работа 14.1

## Описание:

Создание ядра для интернет-магазина

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:AelitaDi/homework-module-4.git
```
2. Установите зависимости: mypy, flake8, black, isort, pytest, pytest-cov

## Применение:

1. Создана сущность ``Product``
2. Создана сущность ``Category``
3. В файле ``utils.py`` реализованы функции для считывания данных из JSON-файла.
4. Метод ``add_product`` позволяет добавить продукт в категорию.
5. Метод ``products_list`` выводит список продуктов в данной категории.
6. Метод ``price`` позволяет задать новую стоимость товару. Включает в себя проверку на корректность значения и на снижение стоимости.
7. Метод ``new_product`` создает объект класса ``Product`` из словаря.
8. Метод ``__add__`` для класса Product позволяет складывать стоимость всех товаров на складе.
9. Методы ``__str__`` для классов Product и Category выводят их строковые отображения.
10.  Вспомогательный класс ``ProductIterator`` позволяет итерироваться по всем товарам из заданной категории.
11. Создана сущность ``Smartphone`` из сущности ``Product``
12. Создана сущность ``LawnGrass`` из сущности ``Product``


## Тестирование:

Для тестирования используется pytest  
Для запуска тестов введите в терминале команду pytest