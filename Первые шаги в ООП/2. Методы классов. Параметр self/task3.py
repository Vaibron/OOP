'''
Имеется следующий класс для считывания информации из входного потока:

    import sys
    class StreamReader:
        FIELDS = ('d', 'title', 'pages')
        def readlines(self):
            lst_in = list(map(str.strip, sys.stdin.readlines())) # считывание списка строк из входного потока sd = StreamData()
            res = sd.create(self.FIELDS, lst_in)
            return sd, res

Которым, затем, можно воспользоваться следующим образом:

sr = StreamReader()
data, result = sr.readlines()

Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
    def create(self, fields, Ist_values): ....

который бы на входе получал кортеж FIELDS из названий локальных атрибутов (передается в атрибут fields) 
и список строк Ist_in (передается в атрибут Ist_values) и формировал бы в объекте класса StreamData локальные свойства с именами полей из fields 
и соответствующими значениями из Ist_values.
Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False. 
Если число полей и число строк не совпадает, то метод create() возвращает False и локальные атрибуты создавать не нужно.
Р.Ѕ. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.

Пример входной информации 
    (Sample Input):
    10
    (Sample Output):
    512
'''