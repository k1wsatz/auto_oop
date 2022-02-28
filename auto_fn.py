nissan_gtr = {
    "model": "Gt-r",
    "engine": False,
    "speed": 0,
    "max_speed": 330,
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
        #####################################################
        # if auto["speed"] + amount >= auto["max_speed"]:   #
        #     auto["speed"] = auto["max_speed"]             #
        # else:                                             #
        #     auto["speed"] += amount                       #
        ########### same thing in one line below ############
        auto["speed"] = min(auto["speed"] + amount, auto["max_speed"])
        print(f'Jedziesz z prędkością {auto["speed"]} km/h')
    else:
        print('Odpal silnik')


def slow_down(auto, amount):
    auto["speed"] = max(auto["speed"] - amount, 0)
    print(f'Jedziesz z prędkością {auto["speed"]} km/h')


print(nissan_gtr)
start_engine(nissan_gtr)
speed_up(nissan_gtr, 200)
stop_engine(nissan_gtr)
speed_up(nissan_gtr, 20)
speed_up(nissan_gtr, 20)
speed_up(nissan_gtr, 100)
slow_down(nissan_gtr, 20)
slow_down(nissan_gtr, 300)
slow_down(nissan_gtr, 20)
stop_engine(nissan_gtr)
print(nissan_gtr)
