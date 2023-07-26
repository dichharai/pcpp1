import csv

class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone



class Phone:
    contacts = []
    def __init__(self):
        self.load_contacts_from_csv()

    def load_contacts_from_csv(self):
        with open('contacts.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["Name"]
                phone = row["Phone"]
                Phone.contacts.append(PhoneContact(name, phone))

        # print(Phone.contacts)


    def search_contacts(self, phrase):
        res = [contact for contact in Phone.contacts if contact.name.startswith(phrase)]
        if not res:
            print("No contacs found.")
            return
       
        for contact in res:
            print(f'{contact.name} ({contact.phone})' )


p = Phone()
p.search_contacts('fa')


