class Phone:
    def __init__(self, number):
        self.number = number
    
    def turn_on(self):
        return f'mobile phone {self.number} is turned on'

    def turn_off(self):
        return 'mobile phone is turned off'

    def call(self, number):
        return f'calling {number}'

ph1 = Phone('01632-960004')
ph2 = Phone('01632-960012')

print(ph1.turn_on())
print(ph2.turn_on())

print(ph1.call('555-34343'))

print(ph1.turn_off())
print(ph2.turn_off())