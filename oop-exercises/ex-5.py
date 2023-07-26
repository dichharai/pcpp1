class Scanner:
    def scan(self):
        return "scan() method from Scanner class"

class Printer:
    def print(self):
        return "print() method from Printer class"

class Fax:
    def send(self):
        return f"send() method from Fax class"

    def print(self):
        return f"print() method from Fax class"


class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass

spf = MFD_SPF()
print(spf.scan(), ',', spf.print(), ',', spf.send())

sfp = MFD_SFP()
print(sfp.scan(), ',', sfp.print(), ',', sfp.send())
