#1 Masala
# def t_yilni_hisobla(ism, yosh, joriy_yil=2022):
#     '''Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya'''
#     print(f'{ism.title()}, siz {joriy_yil-yosh} yilda tug\'ilgansiz!')
# ism = input('Ismingiz nima? ')
# yosh = int(input('Yoshingiz nechchida? '))
# t_yilni_hisobla(ism, yosh)


#2 Masala
# def kv_kub_hisobla(son):
#     print(f'{son} ning kvadrati {son**2}\
#         \n{son} ning kubi {son**3}')
# son = float(input('Istalgan son kiriting: '))
# kv_kub_hisobla(son)


#3 Masala
# def toq_justligini_aniqla(son):
#     a = son % 2
#     if a == 0:
#         print('Bu son juft!')
#     else:
#         print('Bu son toq!')
# son = int(input('Istalgan butun son kiriting: '))
# toq_justligini_aniqla(son)


#4 Masala
# def kattasini_top(son, son1):
#     if son>son1:
#         print(son)
#     elif son<son1:
#         print(son1)
#     else:
#         print('Sonlar teng!')
# son = float(input('Istalgan son kiriting: '))
# son1 = float(input('Istalgan son kiriting: '))
# kattasini_top(son, son1)


#7 Masala
# def tekshir(son):
#     for i in range(9):
#         a = son % (i+2)
#         if a == 0:
#             print(f'{son} {i+2} ga qoldiqsiz bo\'linadi!')
#         else:
#             print(f'{son} ning {i+2} ga bo\'lgandagi qoldig\'i {a} ga teng!')
# son = int(input('Istalgan butun son kiriting: '))
# tekshir(son)