class Computer:
    def __init__(self, computer_type, computer_model, computer_os, computer_storage, computer_ram):
        self.computer_type = computer_type
        self.computer_model = computer_model
        self.computer_os = computer_os
        self.computer_storage = computer_storage
        self.computer_ram = computer_ram

    def playGame(self, game):
        print("%s (%s) playing %s" % (self.computer_type, self.computer_model, game))


class Desktop(Computer):
    def __init__(self, computer_model, computer_os, computer_storage, computer_ram):
        Computer.__init__(self, "Desktop", computer_model, computer_os, computer_storage, computer_ram)


class Laptop(Computer):
    def __init__(self, computer_model, computer_os, computer_storage, computer_ram):
        Computer.__init__(self, "Laptop", computer_model, computer_os, computer_storage, computer_ram)


chromebook = Laptop("Chromebook", "Linux", "500GB", "4GB DDr3")
aftershock = Desktop("Aftershock Desktop", "Windows", "1TB", "16GB GDDr5")

print("---------------------------")
print(chromebook.computer_type)
print(chromebook.computer_model)
print(chromebook.computer_os)
print(chromebook.computer_storage)
print(chromebook.computer_ram)
print("---------------------------")
print(aftershock.computer_type)
print(aftershock.computer_model)
print(aftershock.computer_os)
print(aftershock.computer_storage)
print(aftershock.computer_ram)
print("---------------------------")
chromebook.playGame("Team Fortress 2")
aftershock.playGame("Factorio")

