from dataclasses import dataclass

# task 1

@dataclass
class Tovar:
    name_of_item: str
    name_of_stor: str
    item_amount: float

@dataclass
class Cklad:
    info_item_index: float
    info_item_name: str
    sortirovka_name: str
    sortirovka_stor: str
    sortirovka_prise: float
    summa_item_prise: float


# task 2


class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        return False

    def trumpet(self):
        if self.bee <= self.elephant:
            return 'tuu-tu-doo-doo'
        return 'wzzzzz'

    def eat(self, meal, value):
        if meal == 'nectar':
            self.bee += value
            self.elephant -= value
        elif meal == 'grass':
            self.bee -= value
            self.elephant += value
        if self.elephant > 100:
            self.elephant = 100
        elif self.elephant < 0:
            self.elephant = 0
        if self.bee > 100:
            self.bee = 100
        elif self.bee < 0:
            self.bee = 0

    def get_parts(self):
        return (self.bee, self.elephant)

# task 3

class Bus:
    PAY_COEFF = 0.01
    MAX_PASSENGERS = 60

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.passengers = 0
        self.money = 0

    def move(self, distance):
        self.money += Bus.PAY_COEFF * self.passengers * distance
        super().move(distance)

    def enter(self, passengers):
        if passengers + self.passengers > Bus.MAX_PASSENGERS:
            print('Достигнута максимальная вместимость автобуса')
            print('Уехать смогли только {:d}'.format(Bus.MAX_PASSENGERS - self.passengers))
            print('Остались {:d}'.format(passengers - (Bus.MAX_PASSENGERS - self.passengers)))
            passengers = Bus.MAX_PASSENGERS - self.passengers
        return passengers

    def exit(self, passengers):
        if passengers > self.passengers:
            print('Вышли все из автобуса')
            passengers = self.passengers
        return passengers

    def __str__(self):
        lines = [super().__str__(),
                 f'В автобусе {self.passengers} пассажиров',
                 f'У водителя {round(self.money, 2)} денег']
        return '\n'.join(lines)