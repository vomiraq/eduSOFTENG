# класс Tomato (помидор)
class Tomato:
    # статическое свойство, описывающее все стадии созревания помидора
    states = ['отсутствует', 'цветение', 'зелёный', 'красный']

    # конструктор класса
    def __init__(self, index):
        # динамическое свойство index - индекс помидора на кусте
        self.index = index
        # динамическое свойство state - текущая стадия созревания
        self.state = Tomato.states[0]

    # метод grow переводит томат на следующую стадию созревания
    def grow(self):
        if self.state != Tomato.states[-1]:
            next_index = Tomato.states.index(self.state) + 1
            self.state = Tomato.states[next_index]

    # метод is_ripe проверяет, что томат созрел (достиг стадии 'красный')
    def is_ripe(self):
        return self.state == Tomato.states[-1]


# класс TomatoBush (куст помидоров)
class TomatoBush:
    # конструктор класса
    def __init__(self, count):
        # динамическое свойство tomatoes - список объектов Tomato
        self.tomatoes = [Tomato(index) for index in range(1, count+1)]

    # метод grow_all переводит все томаты на следующую стадию созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # метод all_are_ripe проверяет, все ли томаты созрели
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # метод give_away_all очищает список томатов после сбора урожая
    def give_away_all(self):
        self.tomatoes = []


# класс Gardener (садовник)
class Gardener:
    # конструктор класса
    def __init__(self, name, plant):
        # динамическое свойство name - имя садовника, публичное
        self.name = name
        # динамическое свойство _plant - объект растения (куст), защищённое
        self._plant = plant

    # метод work позволяет садовнику ухаживать за растением
    def work(self):
        print(f"{self.name} ухаживает за растением...")
        self._plant.grow_all()
        print("растение стало более зрелым.")

    # метод harvest проверяет зрелость плодов и собирает урожай
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай!")
            self._plant.give_away_all()
        else:
            print("помидоры ещё не созрели. ухаживайте за ними дальше.")

    # статический метод knowledge_base выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print("справка по садоводству: ухаживайте за растениями регулярно, чтобы они созрели.")

# вызов справки по садоводству
Gardener.knowledge_base()

# создание объекта класса TomatoBush с 3 помидорами
bush = TomatoBush(3)

# создание садовника, который ухаживает за этим кустом
gardener = Gardener("Иван", bush)

# первый уход за кустом
gardener.work()

# попытка собрать урожай до созревания
gardener.harvest()

# второй уход за кустом
gardener.work()
gardener.work()

# попытка собрать урожай после созревания
gardener.harvest()