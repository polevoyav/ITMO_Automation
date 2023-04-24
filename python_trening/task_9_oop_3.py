class Soda:
    def __init__(self, int = None):
        self.int = int
    def show_my_drink(self):
        if self.int:
            print(f'Газировка и {self.int}')
        else:
            print('Обычная газировка')
drink1 = Soda()
drink2 = Soda('malina')
drink1.show_my_drink()
drink2.show_my_drink()



