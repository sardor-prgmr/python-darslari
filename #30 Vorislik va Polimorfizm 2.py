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
class Footballer(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, klub, terma_jamoa, klub_raqam, terma_jamoa_raqam, fifa_reyting, goals, assists, position, hozirgi_yil = 2023):
        super().__init__(ism, familiya, passport, tyil)
        self.fullname = f"{ism} {familiya}"
        self.club = klub
        self.national_team = terma_jamoa
        self.club_number = klub_raqam
        self.national_team_number = terma_jamoa_raqam
        self.fifa_raiting = fifa_reyting
        self.goals = goals
        self.assists = assists
        self.position = position
        self.now = hozirgi_yil
    def get_info(self):
        info = f"""{self.ism} {self.familiya} {self.tyil} da tug'ulgan.
Klubi: {self.club}, {self.club_number}chi raqam ostida o'ynaydi.
Terma jamoasi: {self.national_team}, {self.national_team_number}chi raqam ostida o'ynaydi.
Fifa reytingi: {self.fifa_raiting}. Karyerasi davomida urgan gollari: {self.goals}, qilgan asistlari: {self.assists}.
Pozitsiyasi: {self.position}"""
        return info
    def add_goal(self, gollar_soni, qaysi_klubga_qarshi):
        self.goals += gollar_soni
        return f"{self.fullname} ning gollari soni {self.goals} ga yetdi, chunki u {qaysi_klubga_qarshi}ga qarshi {gollar_soni}ta gol urdi!"
    def add_assist(self, assistlar_soni, qaysi_klubga_qarshi):
        self.assists += assistlar_soni
        return f"{self.fullname} ning assistlari soni {self.assists} ga yetdi, chunki u {qaysi_klubga_qarshi}ga qarshi {assistlar_soni}ta assist qildi!"
    def new_club(self, club, price, term):
        if club.lower() != self.club.lower():
            return f"Rasman. {self.fullname} {club} klubiga {term} yilgacha kontrakt tuzdi. Transfer narhi {price}"
        else:
            return f"Rasman. {self.fullname} {club} klubi bilan kontraktini {term} yilgacha uzaytirdi."

class Real_Madrid(Footballer):
    def __init__(self, ism, familiya, passport, tyil, klub, terma_jamoa, klub_raqam, terma_jamoa_raqam, fifa_reyting, goals, assists, position, nechta_ychl, travma, liverpoolga_qarshi_tushadimi, goals_against_liverpool, hozirgi_yil=2023):
        super().__init__(ism, familiya, passport, tyil, klub, terma_jamoa, klub_raqam, terma_jamoa_raqam, fifa_reyting, goals, assists, position, hozirgi_yil)
        self.how_many_CL = nechta_ychl
        self.travma = travma
        self.play = liverpoolga_qarshi_tushadimi
        self.goals_to_liverpool = goals_against_liverpool
    def get_infos(self):
        return super().get_info() + f"YChL lar soni: {self.how_many_CL}. Travma bormi?: {self.travma}. \nLiverpoolga qarshi {self.play}"
    def gol_urdi(self, goals):
        self.goals_to_liverpool += goals
        return f"{self.fullname} ning Liverpoolga urgan gollari soni {self.goals_to_liverpool} ga yetdi, chunki u mersisaydlarga qarshi {goals}ta gol urdi!"

cris = Footballer("Cristiano", "Ronaldo", "Nfs2289343", 1985, "Man United", "Portugaliya", "7", "7", 91, 819, 266, "orthodox striker")
print(cris.add_assist(2, "Barcelona"))
print(cris.add_goal(7, "Argentina"))
print(cris.new_club("Al Nasr", 0, "2025"))

benzema = Real_Madrid("Karim", "Benzema", "NFS234234", 1987, "Real Madrid", "Fransiya", "9", "9", 93, 432, 187, "striker", 5, "yo'q", "ha", 4, 2022)
print(benzema.get_info())
print(benzema.gol_urdi(3))