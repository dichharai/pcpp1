import abc


class Scanner(abc.ABC):

    @abc.abstractmethod
    def scan_document():
        pass

    @abc.abstractmethod
    def get_scanner_status():
        pass


class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document():
        pass

    @abc.abstractmethod
    def get_printer_status():
        pass


class MFD1(Scanner, Printer):
    def scan_document(self):
        return f'scanned document'

    def get_scanner_status(self):
        return f'Resolution: 480p, SN: S12345'

    def print_document(self):
        return f'printed document'
    
    def get_printer_status(self):
        return f'Resolution: 480p, SN: P12345'



class MFD2(Scanner, Printer):
    def scan_document(self):
        return f'scanned document'

    def get_scanner_status(self):
        return f'Resolution: 720p, SN: S67890'

    def print_document(self):
        return f'printed document'
    
    def get_printer_status(self):
        return f'Resolution: 720p, SN: P67890'


class MFD3(Scanner, Printer):
    def scan_document(self):
        return f'scanned document'

    def get_scanner_status(self):
        return f'Resolution: 1080p, SN: S162738'

    def print_document(self):
        return f'printed document'
    
    def get_printer_status(self):
        return f'Resolution: 480p, SN: P162738'


mfd1 = MFD1()
mfd2 = MFD2()
mfd3 = MFD3()

print(mfd1.print_document(), mfd1.get_printer_status(), mfd1.scan_document(), mfd1.get_printer_status())
print(mfd2.print_document(), mfd2.get_printer_status(), mfd2.scan_document(), mfd2.get_printer_status())
print(mfd3.print_document(), mfd3.get_printer_status(), mfd3.scan_document(), mfd3.get_printer_status())