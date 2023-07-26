import requests
import json
import sqlite3

# class VintageCarDB:
#     def __init__(self):
#         self.conn = sqlite3.connect('vintage_car.db')
#         self.c = self.conn.cursor()
#         self.create_table()

#     def create_table(self):
#         stmt = '''CREATE TABLE IF NOT EXISTS vintage_cars(
#             id INTEGER PRIMARY KEY,
#             brand STRING,
#             model STRING,
#             production_year INTEGER
#             convertible BOOLEAN
#             )'''

# vcar_db = VintageCarDB()

CAR_URL = 'http://localhost:3000'
def check_server(cid=None):
    # returns True or False;
    # when invoked without arguments simply checks if server responds;
    # invoked with car ID checks if the ID is present in the database;
    if not cid:
        reply = requests.head(f'{CAR_URL}')
    else:
        reply = requests.get(f'{CAR_URL}/cars/{cid}')

    return reply.status_code == requests.codes.ok




def print_menu():
    # prints user menu - nothing else happens here;
    td_border = '+'+'-'*28+'+'
    print(td_border)
    print('|'.ljust(4) + 'Vintage Cars Database' + '|'.rjust(5))
    print(td_border)



def read_user_choice():
    # reads user choice and checks if it's valid;
    # returns '0', '1', '2', '3' or '4' 
    print("MENU")
    print("="*4)
    print('1. List cars')
    print('2. Add new car')
    print('3. Delete car')
    print('4. Update car')
    print('0. Exit')

    choice = int(input("Enter your choice (0..4: "))
    return str(choice)



def print_header():
    # prints elegant cars table header;
    header = ["id", "brand", "model", "production_year", "convertible"]
    width = [5, 10, 10, 20, 20]

    print('| ', end="")
    for (h, w) in zip(header, width):
        print(h.ljust(w), end="| ")
    print()

def print_car(car):
    # prints one car's data in a way that fits the header;
    header = ["id", "brand", "model", "production_year", "convertible"]
    width = [5, 10, 10, 20, 20]

    print("| ", end="")
    for (h, w) in zip(header, width):
        print(str(car[h]).strip('\n').ljust(w), end="| ")
        # print(car[h], end="")
    print()

def list_cars():
    # gets all cars' data from server and prints it;
    # if the database is empty prints diagnostic message instead;
    print_header()
    cars = requests.get(f'{CAR_URL}/cars')

    for car in cars.json():
        print_car(car)
    

"""
def name_is_valid(name):
# checks if name (brand or model) is valid;
# valid name is non-empty string containing
# digits, letters and spaces;
# returns True or False;
"""
def enter_id():
    # allows user to enter car's ID and checks if it's valid;
    # valid ID consists of digits only;
    # returns int or None (if user enters an empty line);
    car_id = int(input("Car ID (empty string to exit) "))
    if str(car_id).strip() == "":
        return None
    return car_id

"""
def enter_production_year():
# allows user to enter car's production year and checks if it's valid;
# valid production year is an int from range 1900..2000;
# returns int or None  (if user enters an empty line);


def enter_name(what):
# allows user to enter car's name (brand or model) and checks if it's valid;
# uses name_is_valid() to check the entered name;
# returns string or None  (if user enters an empty line);
# argument describes which of two names is entered currently ('brand' or 'model');

def enter_convertible():
# allows user to enter Yes/No answer determining if the car is convertible;
# returns True, False or None  (if user enters an empty line);
"""
def delete_car():
    # asks user for car's ID and tries to delete it from database;
    car_id = int(input("Enter car's id to delete: "))

    try:
        resp = requests.delete(f'{CAR_URL}/cars/{car_id}')
        print(resp.status_code)
    
    except requests.RequestExcption:
        print("Communication erro")
    else:
        if resp.status_code == requests.codes.ok:
            print("Delete successful")
        else:
            print("debug")


def input_car_data(with_id):
    # lets user enter car data;
    # argument determines if the car's ID is entered (True) or not (False);
    # returns None if user cancels the operation or a dictionary of the following structure:
    # {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
    if with_id:
        car_id = int(input("Car ID (empty string to exit) "))
        if str(car_id).strip() == "":
            exit()
        car_brand = input("Car brand (empty string to exit) ")
        if car_brand.strip() == "":
            exit()
        car_model = input("Car model (empty string to exit) ")
        if str(car_model).strip() == "":
            exit()
        car_prod = int(input("Car production year (empty string to exit) "))
        if str(car_prod).strip() == "":
            exit()
        car_conv = input("Is this car convertible? [y/n] ")
        if car_conv.strip() == "":
            exit()
        if car_conv == 'n':
            car_conv = False
        else:
            car_conv = True

        print(car_id, car_brand, car_model)

        car_obj = {"id": car_id, "brand": car_brand, "model": car_model, "production_year": car_prod, "convertible": car_conv}
        # print(requests.codes)
        h_content = {"Content-Type": "application/json"}
        try:
            jobj = json.dumps(car_obj)
            print(jobj)
            resp = requests.post(f'{CAR_URL}/cars', headers=h_content, data=jobj)
            print(resp.status_code, resp.json(), type(resp))

        except requests.RequestException:
            print("Communication error")
        else:
            if resp.status_code == requests.codes.created:
                print("created!")
            else:
                print(resp.status_code)
                print("Check the problem!")
    else:
        car_brand = input("Car brand (empty string to exit) ")
        if car_brand.strip() == "":
            exit()
        car_model = input("Car model (empty string to exit) ")
        if str(car_model).strip() == "":
            exit()
        car_prod = int(input("Car production year (empty string to exit) "))
        if str(car_prod).strip() == "":
            exit()
        car_conv = input("Is this car convertible? [y/n] ")
        if car_conv.strip() == "":
            exit()
        if car_conv == 'n':
            car_conv = False
        else:
            car_conv = True

        car_obj = {"brand": car_brand, "model": car_model, "production_year": car_prod, "convertible": car_conv}
        # print(requests.codes)
        return car_obj



def add_car():
    # invokes input_car_data(True) to gather car's info and adds it to the database;
    input_car_data(True)



def update_car():
    # invokes enter_id() to get car's ID if the ID is present in the database;
    # invokes input_car_data(False) to gather new car's info and updates the database;
    cid = enter_id()
    updated_car = input_car_data(False)

    h_content = {"Content-Type": "application/json"}

    try:
        jobj = json.dumps(updated_car)
        print(jobj)
        resp = requests.put(f'{CAR_URL}/cars/{cid}', headers=h_content, data=jobj)
        print(resp.status_code, resp.json(), type(resp))

    except requests.RequestException:
        print("Communication error")
    else:
        if resp.status_code == requests.codes.ok:
            print("updated!")
        else:
            print(resp.status_code)
            print("Check the problem!")
    

while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
