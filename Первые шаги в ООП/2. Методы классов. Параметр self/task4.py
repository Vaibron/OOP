'''
Из входного потока читаются строки данных с помощью команды:
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    # считывание списка строк из входного потока
в формате: id, name, old, salary (записанные через пробел). Например:
1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
То есть, каждая строка это элемент списка Ist_in.
Необходимо в класс DataBase:
    class DataBase:
        lst_data = []
        FIELDS = ('id', 'name', 'old', 'salary")
добавить два метода:
select(self, a, b) - возвращает список из элементов списка Ist_data в диапазоне [а; b] (включительно) по их индексам (не id, а индексам списка); также учесть, что граница в может превышать длину списка.
insert(self, data) - для добавления в список Ist_data новых данных из переданного списка строк data;
Каждая запись в списке Ist_data должна быть представлена словарем в формате:
    (id": "номер", "пате': 'имя', 'old': 'возраст', 'salary: 'зарплата")
Например:
    {id: '1', 'name': 'Cepreй', 'old': '35', 'salary": "120000"}
Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции FIELDS.
Р. С. Ваша задача только добавить два метода в класс DataBase.
'''


import sys
# здесь объявляются все необходимые классы

# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

# здесь создаются объекты классов и вызываются нужные методы