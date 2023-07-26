class EngraveException(Exception):
    pass



class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @classmethod
    def engrave(cls, name):
        if not name.isalnum() or len(name) > 40:
            raise EngraveException(f"{name} should be alphanumeric and 40 characters long")
        obj = cls()
        obj.text = name
        return obj

w1 = LuxuryWatch()
w2 = LuxuryWatch.engrave("LouiseSarkozhy")

try:
    w3 = LuxuryWatch.engrave("foo@baz.com")
except EngraveException as e:
    print(f"{e.args[0]}")

print(f"Number of watch created: {LuxuryWatch.watches_created}")