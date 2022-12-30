class User:
    def __init__(self, ism, familiya, taxallus, email, tel_raqam, tyil):
        self.name = ism
        self.last_name = familiya
        self.nickname = taxallus
        self.email = email
        self.phone_number = tel_raqam
        self.birth_year = tyil
    def get_name(self):
        return self.name
    def get_last_name(self):
        return self.last_name
    def get_name(self):
        return self.nickname
    def get_nickname(self):
        return self.email
    def get_email(self):
        return self.phone_number
    def get_phone_number(self):
        return self.birth_year
    def get_birth_year(self):
        return f"""Foydalanuvchi {self.nickname} ning  to'liq ismi {self.name} {self.last_name},
Uning telefon raqami: {self.phone_number}, emaili: {self.email} va u {self.birth_year}chi yilda tug'ilgan"""
foydalanuvchi1 = User("Sardor", "Salimov", "Rythm_of_the_knight", "salimovsardor035@gmail.com", "+998946943070", 2009)
print(foydalanuvchi1.get_info())