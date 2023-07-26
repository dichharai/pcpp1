import json
from typing import Dict, Any

class Vehicle:
    def __init__(self, registration_number: str, year_of_production: int, passenger: str, mass: float):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        if passenger == 'y':
            self.passenger = True
        else:
            self.passenger = False
        self.mass = mass

class VehicleEncoder(json.JSONEncoder):
    def default(self, vehicle):
        if isinstance(vehicle, Vehicle):
            return vehicle.__dict__
        else:
            return super().default(self, vehicle)

class VehicleDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.decode_vehicle)

    def decode_vehicle(self, vehicle_dict: Dict[Any, Any]):
        return Vehicle(**vehicle_dict)

question = "What can I do for you?\n1. produce a JSON string \
describing a vehicle\n2. decode a JSON string into vehicle data\n"

choice = -1
try:
    choice = int(input(question))
    if choice == 1:
        print(f"Your choice is {str(choice)}")
        regist_num = input("Registration number: ")
        year_of_prod = int(input("Year of production: "))
        passenger = input("Passenger [y/n]: ")
        if passenger not in ['y', 'n']:
            raise TypeError
        vehicle_mass = float(input("Vehicle mass: "))
        
        v_obj = Vehicle(regist_num, year_of_prod, passenger, vehicle_mass)
        s_obj = json.dumps(v_obj, cls=VehicleEncoder)
        print(f'Resulting JSON string is: \n{s_obj}')
        print(type(s_obj))
    elif choice == 2:
        print(f'Your choice is {str(choice)}')
        s_obj = input("Enter vehicle JSON string: ")
        
        v_obj = json.loads(s_obj, cls=VehicleDecoder)
        print(v_obj, type(v_obj))
        print(v_obj.__dict__)
    else:
        print("incorrect value")
        raise ValueError
    print("Done")

except TypeError as te:
    print("Enter correct option please")
except ValueError as ve:
    print("Enter correct value please")
    