# wzorzec projektowy fabryka
def auto_factory(model, max_speed):
    return {
        "model": model,
        "engine": False,
        "speed": 0,
        "max_speed": max_speed,
    }


def start_engine(auto):
    if not auto["engine"]:
        auto["engine"] = True
        print("Silnik odpalony")
    else:
        print('Nie odpalaj odpalonego!')


def stop_engine(auto):
    if auto["speed"] == 0:
        auto["engine"] = False
        print('Silnik zgaszony')
    else:
        print('Zatrzymaj fure!')


def speed_up(auto, amount):
    if auto["engine"]:
        auto["speed"] = min(auto["speed"] + amount, auto["max_speed"])
        print(f'Jedziesz z prędkością {auto["speed"]} km/h')
    else:
        print('Odpal silnik')


def slow_down(auto, amount):
    auto["speed"] = max(auto["speed"] - amount, 0)
    print(f'Jedziesz z prędkością {auto["speed"]} km/h')


nissan_gtr = auto_factory('Gt-r', 330)
tico = auto_factory('Tico', 210)

print(nissan_gtr)
start_engine(nissan_gtr)
start_engine(tico)
speed_up(nissan_gtr, 20)
speed_up(tico, 500)
stop_engine(nissan_gtr)
speed_up(nissan_gtr, 50)
speed_up(nissan_gtr, 100)
slow_down(nissan_gtr, 10)
speed_up(nissan_gtr, 100)
slow_down(nissan_gtr, 50)
slow_down(nissan_gtr, 500)
stop_engine(nissan_gtr)

print(nissan_gtr)
print(tico)