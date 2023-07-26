class AccountException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BankAccount:
    def __init__(self, account_number, account_balance):
        self.__account_number = account_number
        self.__account_balance = account_balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, v):
        raise AccountException("Cannot set account number, sorry!")

    @account_number.deleter
    def del_acccount_number(self):
        if self.account_balance > 0:
            raise AccountException("You cannot delete the account right now. The balance is > 0.")

        print(f'inside del_account_number')
        del self.__account_number

    def __del__(self):
        print(f"deleting {self}")

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, value):
        if value < 0:
            raise AccountException("You cannot set negative balance, sorry!")
        self.__account_balance = value

    def bank_operation(self, mode, value):
        if mode == 'w':
            if self.account_balance < value:
                raise AccountException("Your balance does not fill the withdrawl request")
            if value > 100_000:
                print("Adding the withdrawl transaction for auditing purpose")
                self.account_balance -= value
        elif mode == 'd':
            if value > 100_000:
                print('Adding deposit transaction for auditing purpose')
                self.account_balance += value
        else:
            print("Unrecognised operation")

   
        
a1 = BankAccount(1234, 140)
a1.account_balance = 1000

# setting negative balance
try:
    a1.account_balance = -200
except AccountException as e:
    print(e.args[0])

# trying to set negative account number
try:
    a1.account_number = 12345
except AccountException as e:
    print(e.args[0])

# deposit 1_000_000
a1.bank_operation('d', 1_000_000)

# trying to delete non-zero balance account
try:
    del a1.del_acccount_number
except AccountException as e:
    print(e.args[0])


# print(a1)

a1.account_balance = 0

# trying to delete zero balance account
try:
    del a1.del_acccount_number
except AccountException as e:
    print(e.args[0])

# trying to get `account_number` attribute's value
try:
    print(f"a1: {a1.account_number}")
except AttributeError as ae:
    print(ae.args[0])