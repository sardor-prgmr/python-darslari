# lugat = {'integer':'Butun son',
#     'float':'Kasr son',
#     'string':'Matn',
#     'variable':'o\'zgaruvchi',
#     'list':'ro\'yxat',
#     'tuple':'o\'zgarmas ro\'yxat',
#     'loop':'tsikl',
#     'if':'agar',
#     'else':'aks holda',
#     'elif':'aks holda, agar'
#     }
# for key, value in sorted(lugat.items()):
#     print(f'{key.title()} - {value.capitalize()}')


# davlatlar = {'o\'zbekiston':'Toshkent',
#     'rossiya':'moskva',
#     'angliya':'london',
#     'portugaliya':'lissabon',
#     'xitoy':'pekin',
#     'argentina':'buenos-ayres',
#     'aqsh':'washington d. c.',
#     'italiya':'rim'
# }
# print('Dunyo davlatlari: ')
# for davlat in sorted(davlatlar):
#     if davlat == 'aqsh':
#         print(davlat.upper())
#     else:
#         print(davlat.title())
# print('\nDavlatlarning poytaxtllari: ')
# for i in sorted(davlatlar.values()):
#     print(i.title())
# country = input('Qaysi davlatni poytaxtini bilmoqchisiz: ').lower()
# capital = davlatlar.get(country)
# if country not in davlatlar:
#     print('Kechirasiz bizda bunaqa ma\'lumot yo\'q.')
# else:
#     print(f'{country.upper()}ning poytaxti {capital.title()} shahri.')


# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }
# buyurtmalar = []
# for i in range(3):
#     buyurtmalar.append(input(f'{i+1}-chi taom: ').lower())
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f'{buyurtma} {menu[buyurtma]} so\'m')
#     else:
#         print(f'Kechirasiz, bizda {buyurtma} yoq')


