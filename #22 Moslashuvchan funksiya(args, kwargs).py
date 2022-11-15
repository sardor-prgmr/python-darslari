#1 *args
# def kopaytma_top(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
# print(kopaytma_top(1,2,3,4,5,6))


#2 *kwargs
# def talaba_top(ism, familiya, **malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familiya'] = familiya
#     return malumotlar
# print(talaba_top('Sardor', 'Salimov', yosh=13, yonaishi='IT', tug_kun='20.05.2009' , t_joy='Navoiy'))