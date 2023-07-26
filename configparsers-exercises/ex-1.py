import configparser

config = configparser.ConfigParser()
config.read('config-1.ini')

config2 = configparser.ConfigParser()
# print(config.sections())

config2["sentry"] = config["sentry"]
config2["github"] = config["github"]

# github = {"github": config["github"]}
print(config["sentry"], type(config["sentry"]))


with open("prod_config.ini", mode='w', newline='') as outfile:
    config2.write(outfile)


config3 = configparser.ConfigParser()
config3["mariadb"] = config["mariadb"]
config3["redis"] = config["redis"]

with open("dev_config.ini", mode="w") as outfile2:
    config3.write(outfile2)
