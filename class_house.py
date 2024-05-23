class House:
    def __init__(self):
        self.numberOfFloors = 10
        for i in range(self.numberOfFloors):
            print(f'Текущий этаж равен {i}')


floor = House()