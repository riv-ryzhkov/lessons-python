# Клас Медіатора (авіадиспетчер)
class AirTrafficControl:
    def __init__(self):
        self.aircrafts = []

    def register_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def communicate(self, sender, message):
        for aircraft in self.aircrafts:
            if aircraft != sender:
                aircraft.receive_message(message)


# Клас Повітряного Судна
class Aircraft:
    def __init__(self, atc, name):
        self.atc = atc
        self.name = name
        self.atc.register_aircraft(self)

    def send_message(self, message):
        print(f"{self.name} sent message: {message} <to Dispatcher>")
        self.atc.communicate(self, message)

    def receive_message(self, message):
        print(f"{self.name} received message: {message} <<<from Dispatcher>>>")


# Приклад використання
if __name__ == "__main__":
    atc1 = AirTrafficControl()

    plane1 = Aircraft(atc1, "Plane 1")
    plane2 = Aircraft(atc1, "Plane 2")
    plane3 = Aircraft(atc1, "Plane 3")

    plane1.send_message("Traffic in the area, please respond.")
    print('.' * 80)
    plane2.send_message("This is Plane 2, we hear you.")
    print('.' * 80)
    plane3.send_message("This is Plane 3, we hear you.")
    print('=' * 80)
