# 1 mashq
# buyurtmalar = []
# while True:
#     a = input('Savatga nimadir qo\'shing: ')
#     buyurtmalar.append(a)
#     b = input('Yana mahsulot qo\'shasizmi?(ha/yo\'q): ')
#     if b != 'ha':
#         print('Siz')
#         for buyurtma in buyurtmalar:
#             print(F'{buyurtma.title().lstrip()}ni')
#         print('oldiz')
#         break

# 2 mashq
# e_bozor = {}
# while True:
#     mahsulot = input('Mahsulot nomini kiriting: ')
#     narh = int(input(f'{mahsulot}ni narhi qancha(so\'m)? '))
#     e_bozor[mahsulot] = narh
#     javob = input('Yana mahsulot qo\'shasizmi?(ha/yo\'q): ')
#     if javob != 'ha':
#         for mahsulot,narh in e_bozor.items():
#             print(f'{mahsulot.capitalize()}ning narhi {narh} so\'m')
#         break

#3 mashq
buyurtmalar = []
while True:
    a = input('Buyurtmalar ro\'yxatiga nimadir qo\'shing: ')
    buyurtmalar.append(a)
    b = input('Yana mahsulot qo\'shasizmi?(ha/yo\'q): ')
    if b != 'ha':
        break
e_bozor = {}
while True:
    mahsulot = input('Bozordagi mahsulot nomini kiriting: ')
    narh = int(input(f'{mahsulot}ni narhi qancha(so\'m)? '))
    e_bozor[mahsulot] = narh
    javob = input('Yana mahsulot qo\'shasizmi?(ha/yo\'q): ')
    if javob != 'ha':
        break
while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma.lower() in e_bozor:
        print(f'{buyurtma} - {e_bozor[mahsulot]} so\'m')
    else:
        print('Bizda {buyurtma} yo\'q')
