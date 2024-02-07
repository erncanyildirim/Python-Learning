class Calisan:
    rise_rate = 1.1
    def __init__(self, name, surname, wage):
        self.name = name
        self.surname = surname
        self.wage = wage
        self.email = f'{name.lower()}{surname.lower()}@gmail.com'

    def show_info(self):
        print(f'Name: {self.name}\nSurname: {self.surname}\nWage: {self.wage}')

class Yazilimci(Calisan):
    def __init__(self, name, surname, wage, lang):
        super().__init__(name, surname, wage)
        self.lang = lang
    rise_rate = 1.2


class Yonetici(Calisan):
    def __init__(self, name, surname, wage, employees = None):
        super().__init__(name, surname, wage)
        self.employees = employees
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employe(self,employe):
        self.employe = employe
        if employe not in self.employees:
            self.employees.append(employe)

    def del_employe(self, employe):
        self.employe = employe
        if employe in self.employees:
            self.employees.remove(employe)

    def show_employees(self):
        for self.employe in self.employees:
            print(self.employe.show_info())
            print("------------------")


calisan1 = Calisan("ErenCan", "Yildirim", 100000)
calisan2 = Calisan("Sümbül", "Bingöl", 20000)

yazilimci1 = Yazilimci("Ecrin", "Yildirim", 5000, "Python")
yazilimci2 = Yazilimci("ErenCan", "Yildirim", 60000, "C++")
yazilimci3 = Yazilimci("Sümbül", "Bingöl", 100000, "Python")

yonetici1 = Yonetici("Süer", "Yildirim", 999999)
yonetici1.add_employe(yazilimci2)
yonetici1.add_employe(yazilimci3)
yonetici1.show_employees()



