#1 qism
talabalar = []
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.fullname = f"{self.ism} {self.familiya}"
        self.passport = passport
        self.tyil = tyil
        
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
class Fan:
    def __init__(self, fan_nomi):
        self.name = fan_nomi.title()
        self.number = 0
        self.students = list()
    def get_name(self):
        return self.name
    def add_student(self, student_name):
        self.students.append(student_name)
        self.number += 1
        return f"{self.name} faniga {student_name} qo'shildi!"
    def remove_student(self, student_name):
        self.students.remove(student_name)
        self.number -= 1
        return f"{self.name} fanidan {student_name} ketdi!"
    def get_students(self):
        return self.students
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        talabalar.append(self.fullname)
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    def fanga_yozil(self, subject):
        self.fanlar.append(subject.get_name())
        return subject.add_student(self.fullname)
    def remove_fan(self, subject):
        if subject.get_name() in self.fanlar:
            self.fanlar.remove(subject.get_name())
            return subject.remove_student(self.fullname)
        else:
            return f"Siz, {self.fullname} {subject.get_name()} faniga yozilmagansiz"

matem = Fan("Matematika")
rus_tili = Fan("Rus tili")
ona_tili = Fan("Ona tili")
english = Fan("Ingliz tili")
science = Fan("Science")
history = Fan("Tarix")
geography = Fan("Geografiya")
comp_science = Fan("Computer Science")
manzil = Manzil(29, "Islom Karimov", "Navoiy", "Navoiy")
talabacha = Talaba("Sardor", "Salimov", "NFS023302", 2009, "0611238800", manzil)
print(talabacha.fanga_yozil(science))
print(talabacha.fanga_yozil(comp_science))
print(talabacha.fanga_yozil(matem))
print(talabacha.fanga_yozil(english))
print(talabacha.remove_fan(english))
print(talabacha.remove_fan(geography))
print(talabacha.fanlar)