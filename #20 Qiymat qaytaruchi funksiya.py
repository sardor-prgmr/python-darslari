# #1
# # def odam_info(ism, familiya, yosh, t_yil, t_joy='', email='', telefon_raqami=''):
# #     odam = {
# #         'ism':ism,
# #         'familiya':familiya,
# #         'yosh':yosh,
# #         'tug\'ulgan yil':t_yil,
# #         'tug\'ulgan joy':t_joy,
# #         'email':email,
# #         'telefon raqami':telefon_raqami
# #         }
# #     if email and telefon_raqami:
# #         print(f'{familiya.title()} {ism.title()} {t_yil} yilda {t_joy.title()}da tug\'ulgan. Uning yoshi {yosh} da, uning emaili: {email} va uning telefon raqami:{telefon_raqami}.')
# #     elif email:
# #         print(f'{familiya.title()} {ism.title()} {t_yil} yilda {t_joy.title()}da tug\'ulgan. Uning yoshi {yosh} da va uning emaili: {email}.')
# #     elif telefon_raqami:
# #         print(f'{familiya.title()} {ism.title()} {t_yil} yilda {t_joy.title()}da tug\'ulgan. Uning yoshi {yosh} da va uning telefon raqami:{telefon_raqami}.')
# #     else:
# #         print(f'{familiya.title()} {ism.title()} {t_yil} yilda {t_joy.title()}da tug\'ulgan. Uning yoshi {yosh} da.')
# #     return odam
# # print('Quyidagi mal\'umotlarni kiriting:')
# # ism = input('Ism: ')
# # familiya = input('Familiya: ')
# # yosh = int(input('Yosh: '))
# # t_yil = int(input('Tu\'gulgan yil: '))
# # t_joy = input('Tug\'ulgan joy: ')
# # email = input('Email adres(ixtiyoriy): ')
# # telefon_raqami = input('Telefon raqam(ixtiyoriy): ')
# # odam_info(ism, familiya, yosh, t_yil, t_joy, email, telefon_raqami)

# #2
# # def odam_info(ism, familiya, yosh, t_yil, t_joy='', email='', telefon_raqami=''):
# #     odam = {
# #         'ism':ism,
# #         'familiya':familiya,
# #         'yosh':yosh,
# #         't_yil':t_yil,
# #         't_joy':t_joy,
# #         'email':email,
# #         'telefon raqami':telefon_raqami
# #         }
# #     return odam
# # mijozlar = []
# # while True:
# #     print('Quyidagi mal\'umotlarni kiriting:')
# #     ism = input('Ism: ')
# #     familiya = input('Familiya: ')
# #     yosh = int(input('Yosh: '))
# #     t_yil = int(input('Tu\'gulgan yil: '))
# #     t_joy = input('Tug\'ulgan joy: ')
# #     email = input('Email adres(ixtiyoriy): ')
# #     telefon_raqami = input('Telefon raqam(ixtiyoriy): ')
# #     mijozlar.append(odam_info(ism, familiya, yosh, t_yil, t_joy, email, telefon_raqami))
# #     yanami = input('Yana odam kiritasizmi?(yes/no)\n>>> ')
# #     if yanami == 'no':
# #         break
# # for odam in mijozlar:
# #     if odam['email'] and odam['telefon raqami']:
# #         print(f"{odam['familiya'].title()} {odam['ism'].title()} {odam['t_yil']} yilda {odam['t_joy'].title()}da tug'ulgan. Uning yoshi {odam['yosh']} da, uning emaili: {odam['email']} va uning telefon raqami:{odam['telefon raqami']}.")
# #     elif odam['email']:
# #         print(f"{odam['familiya'].title()} {odam['ism'].title()} {odam['t_yil']} yilda {odam['t_joy'].title()}da tug'ulgan. Uning yoshi {odam['yosh']} da va uning emaili: {odam['email']}.")
# #     elif odam['telefon raqami']:
# #         print(f"{odam['familiya'].title()} {odam['ism'].title()} {odam['t_yil']} yilda {odam['t_joy'].title()}da tug'ulgan. Uning yoshi {odam['yosh']} da va uning telefon raqami:{odam['telefon_raqami']}.")
# #     else:
# #         print(f"{odam['familiya'].title()} {odam['ism'].title()} {odam['t_yil']} yilda {odam['t_joy'].title()}da tug'ulgan. Uning yoshi {odam['yosh']} da.")

# 3
# def kattasi(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max

#4
# def info_aylana(radius, pi=3.14159):
#     aylana = {
#         'radius':radius,
#         'diametr':radius*2,
#         'perimetr':radius*2*pi,
#         'yuza':pi*radius**2
#     }
#     return aylana

#5 Tub son topuvchi funksiya
# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for i in range(min, max + 1):
#         tub = True
#         if i == 1:
#             tub = False
#         elif i == 2:
#             tub = True
#         else:
#             for x in range(2, i):
#                 if i % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(i)

#     return tub_sonlar
# print(tub_sonlar_top(1, 997))


#6 Fibonachi topuvchi funksiya
# def fibonacci(n):
#     fibonachilar = []
#     for i in range(n):
#         if i == 0 or i == 1:
#             fibonachilar.append(1)
#         else:
#             fibonachilar.append(fibonachilar[-1] + fibonachilar[-2])
#     return fibonachilar
# a = fibonacci(10)
# print(a)


# for i in reversed(range(0, 100, 3)):
#     print(i)


# for i in range(0, -34, -3):
#     print(i)