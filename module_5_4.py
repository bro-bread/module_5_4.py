class House():
    houses_history = []
    def __new__(cls, *args, **kwargs):
        for i in args:
            if type(i) == str:
                cls.houses_history.append(i)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new = range(new_floor)
        if self.number_of_floors < new_floor:
            print("Ошибка")
        else:
            for i in new:
                print(i)
                if (i + 1) == new_floor:
                    print(new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название:{self.name} , кол-во этажей: {self.number_of_floors}")

    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.number_of_floors < other.number_of_floors:
            return True
        else:
            return False

    def __le__(self, other):
        if self.number_of_floors <= other.number_of_floors:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number_of_floors > other.number_of_floors:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.number_of_floors >= other.number_of_floors:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.number_of_floors != other.number_of_floors:
            return True
        else:
            return False

    def __add__(self, value):
        if type(value) == int:
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __del__(self):
        return print(f"{self.name} снесён, но он останется в истории")

    def __radd__(self, value):
        value + self.number_of_floors
        return self

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)



