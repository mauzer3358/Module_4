# Домашнее задание по уроку "Пространство имен"
#
#+++++ Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции inner_function, функция должна печатать значение
# "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы


def test_function():
    def inner_function(res1):
        #nonlocal res1
        #global  res1
        print(res1)
    res1 = inner_function('Я в области видимости функции test_function')
result = test_function()

# Попытка обратиться к функции inner_function следующим образом:
#res1 = inner_function('Я в области видимости функции test_function')
# Приведет к ошибке, так как эта функция находится в области видимости функции: test_function
