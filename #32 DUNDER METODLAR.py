from uuid import uuid4
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
class Talaba(Shaxs):
    """Talaba klassi"""
    talabalar = []
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        self.__id = uuid4()
        Talaba.talabalar.append(self.fullname)
        Talaba.__talabalar_soni += 1
    def get_passport(self):
        return self.passport
    def get_id(self):
        """Talabaning ID raqami"""
        return self.__id
    def __repr__(self):
        return f"{self.fullname}: {self.bosqich}chi bosqich talabasi"
    def __lt__(self, y):
        return self.bosqich < y.bosqich
    def __eq__(self, y):
        return self.bosqich == y.bosqich
    def __le__(self, y):
        return self.bosqich <= y.bosqich
    @classmethod
    def get_talabalar_royxati(cls):
        return cls.talabalar
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
    
    def add_bosqich(self, add=1):
        self.bosqich += add
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    def turn_object(self):
        if self.passport == self or self.__id == self:
            return self
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    def fanga_yozil(self, subject):
        self.fanlar.append(subject)
        return subject.add_student(self)
    def remove_fan(self, subject):
        if subject in self.fanlar:
            self.fanlar.remove(subject)
            return subject.remove_student(self)
        else:
            return f"Siz, {self.fullname} {subject.get_name()} faniga yozilmagansiz"
class Fan:
    def __init__(self, fan_nomi):
        self.name = fan_nomi.title()
        self.__number = 0
        self.__students = list()
    def __repr__(self):
        return self.name
    def get_name(self):
        return self.name
    def add_student(self, student_name):
        self.__students.append(student_name)
        self.__number += 1
        return f"{self.name} faniga {student_name} qo'shildi!"
    def __getitem__(self, index):
        return self.__students[index]
    def __setitem__(self, index, qiymat):
        if isinstance(qiymat, Talaba):
            student = self.__students[index]
            student.fanlar.remove(self)
            self.__students[index] = qiymat
        else:
            return f"Talaba klassiga oid obyekt kiriting"
    def __call__(self, *qiymat):
        if qiymat:
            self.__students += qiymat
            self.__number += len(qiymat)
        else:
            return self.__students
    def __add__(self, talaba):
        if isinstance(talaba, Talaba):
            self.__students.append(talaba)
            talaba.fanlar.append(self)
        else:
            return "Talaba klassiga oid talaba kiriting!"
    def __sub__(self, talaba):
        if isinstance (talaba, Talaba):
            self.__students.remove(talaba)
            talaba.fanlar.remove(self)
    def __len__(self):
        return len(self.__students)
    def remove_student(self, student_name):
        self.__students.remove(student_name)
        self.__number -= 1
        return f"{self.name} fanidan {student_name} ketdi!"
    def get_students(self):
        return self.__students    
manzil = Manzil(29, "Islom Karimov", "Navoiy", "Navoiy")
talaba1 = Talaba("Sardor", "Salimov", "Nfs2432432", 2000, manzil)
talaba2 = Talaba("Sobir", "Salimov", "NFS3210291", 2002, manzil)
talaba3 = Talaba("Afruza", "Salimova", "Nfg265646552", 2010, manzil)
talaba1.add_bosqich(2)
talaba2.add_bosqich()
print(talaba1<talaba2)
print(talaba2>=talaba3)
print(talaba1!=talaba3)
matem = Fan("Matematika")
rus_tili = Fan("Rus tili")
ona_tili = Fan("Ona tili")
english = Fan("Ingliz tili")
science = Fan("Science")
history = Fan("Tarix")
geography = Fan("Geografiya")
comp_science = Fan("Computer Science")
manzil = Manzil(29, "Islom Karimov", "Navoiy", "Navoiy")
print(talaba1.fanga_yozil(science))
print(talaba2.fanga_yozil(comp_science))
print(talaba3.fanga_yozil(matem))
print(talaba1.fanga_yozil(english))
print(talaba2.fanga_yozil(history))
print(talaba3.fanga_yozil(geography))
print(talaba1.fanlar)
print(talaba2.fanlar)
print(talaba3.fanlar)
comp_science[0] = talaba1
print(comp_science.get_students())
print(matem[:])
print(len(english))
comp_science + talaba2
comp_science + talaba3
print(comp_science.get_students())
print(talaba2.fanlar)
history - talaba2
print(talaba2.fanlar)
print(history.get_students())