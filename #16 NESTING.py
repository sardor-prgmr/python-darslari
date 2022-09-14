# ronaldo = {'tyil':'1985',
#     'hozir':'2022',
#     'ism':'Cristiano Ronaldo dos Santos Aveiro',
#     'tjoy':'Portugaliya davlati, Funshal shahri'
# }
# messi = {'tyil':'1987',
#     'hozir':'2022',
#     'ism':'Lionel Andrés Messi',
#     'tjoy':'Argentina davlati, Rosariya shahri'
# }
# neymar = {'tyil':'1992',
#     'hozir':'2022',
#     'ism':'Neymar da Silva Santos Júnior',
#     'tjoy':'Braziliya davlati, San Paulu shahri'
# }
# maguire = {'tyil':'1993',
#     'hozir':'2022',
#     'ism':'Jacob Harry Maguire',
#     'tjoy':'Angliya davlati, Sheffield shahri'
# }
# futbolchilar = [ronaldo, messi, neymar, maguire]
# for futbolchi in futbolchilar:
#     ism = futbolchi["ism"]
#     tyil = int(futbolchi["tyil"])
#     tjoy = futbolchi["tjoy"]
#     hozir = int(futbolchi["hozir"])
#     print(f'{ism} {tyil}-da {tjoy}da tug\'ulgan. U {hozir-tyil} til umr ko\'rgan.') 



# kinolar = {
#           'Sardor': ['Thor', 'doktor strange', 'garri potter'],
#           'Sobir': ['qasoskorlar', 'maska', 'поймай меня если сможешь'],
#           'Azim': ['spiderman', 'titanic', 'shaytanat'],
#           'Aziz': ['mr.bin', 'железный человек', 'forsaj']
#           }
# for ism,kinolar in kinolar.items():
#     print(f'\n{ism}ning sevimli kinolari: ')
#     for kino in kinolar:
#         print(kino.title())


# davlatlar = {
#     'o\'zbekiston':{'poytaxt':"toshkent",
#                     'hududi':448978,
#                     'aholisi':33000000,
#                     'pul birligi':"so'm"
#                     },
#     'aqsh':{'poytaxt':"vashington",
#                     'hududi':9631418,
#                     'aholisi':327_000_000,
#                     'pul birligi':"dollar"
#             },
#     'angliya':{'poytaxt':"london",
#                 'hududi':130279,
#                 'aholisi':55_980_000,
#                 'pul birligi':"funt sterling"
#             }
#     }
# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['hududi']} kv.km"
#           f"\nAholisi: {info['aholisi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")
