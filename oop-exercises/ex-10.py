class Tires:
    def __init__(self, size):
        self.size = size

    def get_pressure(self):
        return f"pressure of {self.size} tire"

    def pump(self):
        return f"pumping {self.size} tire"


class Engine:
    state = "STOP"
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        self.__class__.state = "START"
        return "starting the engine"

    def stop(self):
        self.__class__.state = "STOP"
        return "stopping the engine"

    @classmethod
    def get_state(cls):
        return cls.state


class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires


city_car = Vehicle(1234, Engine("Electric"), Tires(15))
all_terrain_car = Vehicle(5678, Engine("Petrol"), Tires(18))

print(f"CITY CAR\n{'=' * 8}")

print(city_car.engine.fuel_type)
print(city_car.engine.start())
print(city_car.engine.get_state())
print(city_car.engine.stop())
print(city_car.engine.get_state())
print(city_car.tires.size)
print(city_car.tires.get_pressure())
print(city_car.tires.pump())

print(f"\nALL TERRAIN CAR\n{'=' * 15}")
print(all_terrain_car.engine.fuel_type)
print(all_terrain_car.engine.start())
print(all_terrain_car.engine.get_state())
print(all_terrain_car.engine.stop())
print(all_terrain_car.engine.get_state())
print(all_terrain_car.tires.size)
print(all_terrain_car.tires.get_pressure())
print(all_terrain_car.tires.pump())



