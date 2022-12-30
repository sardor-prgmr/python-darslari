class Avto:
    def __init__(self, korobka, model, rang, narh, max_tezlik, xavfsizlik, korinish, ishlash, kilometr=0):
        self.korobka = korobka
        self.model = model
        self.colour = rang
        self.price = narh
        self.max_speed = max_tezlik
        self.safety = xavfsizlik
        self.image = korinish
        self.performance = ishlash
        self.kilometers = kilometr
    def get_korobka(self):
        return self.korobka
    def get_model(self):
        return self.model
    def get_colour(self):
        return self.colour
    def get_price(self):
        return self.price
    def get_maxspeed(self):
        return self.max_speed
    def get_safety(self):
        return self.safety
    def get_image(self):
        return self.image
    def get_performance(self):
        return self.performance
    def get_kilometers(self):
        return self.kilometers
    def get_full_info(self):
        return f"{self.image} ko'rinishga ega {self.colour} rangli {self.model} - {self.korobka} korobka, eng baland tezligi - {self.max_speed}, ammo shunga qaramay {self.safety} vavfsizlikka ega. {self.performance} ishlaydigan bu moshinaning narhi {self.price} va u {self.kilometers} km yurgan!"
    def get_info(self):
        return f"{self.colour} {self.model}"
    def update_km(self, km):
        self.kilometers =+ km
        return self.kilometers
class Avtosalon:
    def __init__(self, salon_nomi, manzili, sotuvdagi_avtomobillar, tel_raqami, email, sayt, etajlar_soni, korinishi, xodimlar_soni, avtomobillar_soni):
        self.name = salon_nomi
        self.adress = manzili
        self.avtosale = list(sotuvdagi_avtomobillar)
        self.phone_number = tel_raqami
        self.email = email
        self.website = sayt
        self.floornumber = etajlar_soni
        self.image = korinishi
        self.people = xodimlar_soni
        self.avto_number = avtomobillar_soni
        self.avtosaless = []
    def add_avto(self, avto):
        self.avtosaless.append(avto)
        self.avto_number += 1
    def get_avtolar(self):
        self.avtosale += [avto.get_info() for avto in self.avtosaless]
        return self.avtosale
    def get_avto(self):
        self.avtosales = [avto.get_info() for avto in self.avtosaless]
        return self.avtosales
avto1 = Avto("avto", "Lamborghini Aventador", "sabzi rang", "100000000000$", 400, "normal", "juda chiroyli", "zo'r")
avto2 = Avto("avto", "Bugatti Veyron", "ko'k", "200000000000$", 450, "normal", "chiroyli", "daxshat")
moshinchalar = ["ko'k BMW", "qora Rolls Royce", "qizil Lamborghini Hurakan"]
sasasa = Avtosalon("SaSaSa", "Toshkent shahri", moshinchalar, "+998946943070", "salimovsardor035@gmail.com", "sasasa.com", 3, "jida chiroyli", 234, 3)
sasasa.add_avto(avto1)
sasasa.add_avto(avto2)
print(sasasa.get_avto())
print(sasasa.get_avtolar())