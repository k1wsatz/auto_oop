class Auto:
    def __init__(self, model, max_speed):
        self.model = model
        self.engine = False
        self.speed = 0
        self.max_speed = max_speed

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print("Silnik odpalony")
        else:
            print('Nie odpalaj odpalonego!')

    def stop_engine(self):
        if self.speed == 0:
            self.engine = False
            print('Silnik zgaszony')
        else:
            print('Zatrzymaj fure!')

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f'Jedziesz z prędkością {self.speed} km/h')
        else:
            print('Odpal silnik')

    def slow_down(self, amount):
        self.speed = max(self.speed - amount, 0)
        print(f'Jedziesz z prędkością {self.speed} km/h')


bmw = Auto('GT-R', 330)
tico = Auto('Tico', 210)

print(bmw)

bmw.start_engine()
tico.start_engine()
bmw.speed_up(20)
tico.speed_up(500)
bmw.stop_engine()
bmw.speed_up(50)
bmw.speed_up(100)
bmw.slow_down(10)
bmw.speed_up(100)
bmw.slow_down(50)
bmw.slow_down(500)
bmw.stop_engine()

print(bmw.model)
print(bmw.max_speed)
