cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
login = input('Login ismingizni kiriting: ')
if login.lower() == 'admin':
    print(f"Xush kelibsiz, {login.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f'Xush kelibsiz, {login}!')
print('Ikkita son kiriting!')
son1 = float(input('1-chi sonni kiriting: '))
son2 = float(input('2-chi sonni kiriting: '))
if son1 == son2:
    print(f'Sonlar teng: {son1}={son2}')
son = float(input('Istalgan son kiriting: '))
print('Musbat son') if son>=0 else print('Manfiy son')
import math
i_son = float(input('Istalgan son kiriting: '))
if i_son >= 0:
    print(sqrt(i_son))
else:
    print(f'Musbat son kiriting!')
