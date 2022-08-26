#09
ismlar = ['Sardor', 'Aziz', 'Odilbek', 'Shohruh', 'Diyor']
for ism in ismlar:
    print(f'Salom {ism}')
print(f'Kod {len(ismlar)} marta takrorlandi')
toq = list(range(1,100, 2))
for son in toq:
    print(f'{son} ning kubi {son**2} ga teng')
kinolar = []
print('5 ta eng sevimli kinolaringizni qaysi?')
for i in range(5):
    kinolar.append(input(f'{i+1} chi kino:'))
print(kinolar)
n_odam = int(input('Bugun nechta odam bilan gaplashdingiz?\n>>>'))
ismlar = []
for i in range(n_odam):
    ismlar.append(input(f'{i+1} chi odamning ismini kiriting:'))
print(ismlar)
    
    