# Создать класс магазина. Конструктор должен инициализировать зачения:
# 'Название магазина', 'Количество проданных товаров'. 
# Реализовать методы обьекта, которые будут увеличивать кол-во проданных товаров, 
# и реализовать вывод значения переменной класса, которая будет хранить 
# общее кол-во товаров проданных всеми магазинами.

class Market:

    Total_value = []

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def incr(self):
        Total_value = []
        Total_value.append(self.value)
        print(Total_value)

    def summ_markets(self):
        summ_of_markets = 0
        Total_value = []
        for i in Total_value:
            summ_of_markets +=i
        print(summ_of_markets)

    def __add__(self, other):
        Total_value = Market(name=self.name, value=self.value + other.value)
        return print(Total_value)

    def __str__(self):
        return self.name
        

Allo = Market('Allo', 400)
Citrus = Market('Citrus', 500)

print(Allo.incr())
print(Citrus.incr())

Allo+Citrus

# TOTAL = Market('Total', 0)
# print(TOTAL.summ_markets())





