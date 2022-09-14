# kitob = 'Yaxshi ko\'rgan kitobizni yozing '
# kitob += '(agar chiqmoqchi buseiz "stop"ni bosing): '
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(kitob)
#     if qiymat != 'stop':
#         print(qiymat)
# print('Dastur tugadi!')


# savol = 'Nechi yoshsiz? '
# while True:
#     qiymat = input(savol)  
#     if qiymat == 'exit' or qiymat == 'quit':
#         print('Dastur tugadi!'),
#         break
#     yosh = int(qiymat)
#     if yosh < 7:
#         pul = 2000
#     elif yosh >= 7 and yosh<=18:
#         pul = 3000
#     elif yosh > 18 and yosh<=65:
#         pul = 10000
#     elif yosh > 65:
#         pul = 0
#     if pul == 0:
#         print('Sizga chipta bepul!')
#     else:
#         print(f'Sizga chipta {pul} so\'m')



# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         print('Dastur tugadi!')
#         break
#     if float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")