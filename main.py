class Account:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_pin(self, p):
        return self.pin == p

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Pul olindi:", amount)
        else:
            print("Yetarli mablag‘ yo‘q")

def run():
    acc = Account("Jahongir", "1234", 500000)

    for _ in range(3):
        p = input("PIN: ")
        if acc.check_pin(p):
            print("Kirish OK")
            acc.withdraw(int(input("Summa: ")))
            return
        else:
            print("Noto‘g‘ri PIN")

    print("Karta bloklandi")

run()
