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
class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar = []
    __talabalar_soni = 0
    def __init__(cls, self,ism,familiya,passport,tyil,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        self.__id = uuid4()
        cls.__talabalar.append(self.fullname)
        cls.__talabalar_soni += 1
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.__id
    @classmethod
    def get_talabalar_royxati(cls):
        return cls.__talabalar
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
    
    
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
