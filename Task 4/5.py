# Задание №5*
# Реализуйте итератор колоды карт (52 штуки без джокеров) CardDeck.
# Каждая карта представлена в виде строки типа «2 Пик».
# При вызове функции next() будет представлена следующая карта.
# По окончании перебора всех элементов возникнет ошибка StopIteration.


class CardDeck:
    # Присваиваем переменне в конструкторе
    def __init__(self):
        self.suits = ['Пик', 'Крести', 'Черви', 'Бубен']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.index = 0

    # Говорим что данные итерируемые
    def __iter__(self):
        return self
    # Определяем метод следующей итерации карты из колоды.
    def __next__(self):
        if self.index >= 52:
            raise StopIteration
        else:
            card = self.values[self.index % 13] + ' ' + self.suits[self.index // 13]
            self.index += 1
            return card

deck = CardDeck()
for card in deck:
    print(card)