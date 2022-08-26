#11
#juft = int(input('Juft son kiriting: '))
#if juft%2 == 0:
#    print('Rahmat!')
#else:
#    print('Bu son juft emas!')
#yosh = int(input('Yoshingiz nechchida?\n>>>'))
#if yosh<=4 or yosh>=60:
#    narh = 0
#elif yosh <= 18:
#    narh = 10000
#elif yosh < 18:
#    narh = 20000
#print(f'Sizga kirish {narh} so\'m')
#son1 = float(input('1-chi sonni kiriting: '))
#son2 = float(input('2-chi sonni kiriting: '))
#if son1==son2:
#    print(f'{son1} = {son2}')
#elif son1>son2:
#    print(f'{son1}>{son2}')
#elif son1<son2:
#    print(f'{son1}<{son2}')
#mahsulotlar = ['olma', 'anor', 'pepsi', 'fanta', 'muzqaymoq', 'sabzi', 'shokolad', 'tarvuz', 'non', 'sut']
#savat = []
#bor_mahsulotlar = []
#mavjud_emas = []
#for i in range(5):
#    savat.append(input(f'{i+1}-chi mahsulotni qo\'shing: '))
#for bla in savat:
#    if bla.lower() in mahsulotlar:
#        bor_mahsulotlar.append(bla)
#    elif bla.lower() not in mahsulotlar:
#       mavjud_emas.append(bla)
#if mavjud_emas:
#    print('Bizada manashula yoq:')
#    for bla in mavjud_emas:
#        print(bla.title())
#else:
#    print('Bizada hamma narsa bor!')
#loginlar = ['sardor', 'diyor', 'aziz', 'odil', 'avaz']
#login = input('Yangi login tanlang: ')
#if login in loginlar:
#    print('Login band!')
#else:
#    print(f'Xush kelibsiz, {login.title()}!')
butun_son = int(input('Istalgan butun son kiriting: '))
for i in range(2,11):
    if butun_son%i == 0:
        print(f'{butun_son} soni {i} ga qoldiqsiz bo\'linadi!')