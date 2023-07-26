import configparser

config = configparser.ConfigParser()
config.read("mess.ini")
print(config.sections())

config2 = configparser.ConfigParser()
sentry = {
    "key": config["sentry"]["key"],
    "secret": config["sentry"]["secret"]
}
config2["sentry"] = sentry

github = {
    "user": config["github"]["user"],
    "password": config["github"]["password"]
}
config2["github"] = github

with open("prod_config.ini", mode="w") as outfile:
    config2.write(outfile)
    
    
config4 = configparser.ConfigParser()
mdb = {"host": config["mariadb"]["host"],
       "name": config["mariadb"]["name"],
       "user": config["mariadb"]["user"],
       "password": config["mariadb"]["password"]
}
config4["mariadb"] = mdb
redis = {"host": config["redis"]["host"],
         "port": config["redis"]["port"],
         "db": config["redis"]["db"]
         }
config4["redis"] = redis

with open("dev_config.ini", mode="w") as outfile:
    config4.write(outfile)


    
    
# config3 = configparser.ConfigParser()
# config3.read("prod_config.ini")

# print(config3.sections())
# print(config3["sentry"]["key"])

config3 = configparser.ConfigParser()
config3.read("dev_config.ini")

print(config3.sections())
print(config3["mariadb"]["host"])