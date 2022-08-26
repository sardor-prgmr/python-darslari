kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
print(kocha + ' ko\'chasi, ' +  mahalla + ' mahallasi,' + \
      tuman + ' tumani, ' + viloyat + ' viloyati ')
print('Iltioms quyidagi ma\'lumotlarni kiriring:')
kocha = input('Ko\'changiz:')
mahalla = input('Mahallangiz:')
tuman = input('Tumaningiz:')
viloyat = input('Viloyatingiz:')
manzil = (f'{kocha} kochasi, {mahalla} mahallasi, \
{tuman} tumani {viloyat} viloyati'.title())
print(manzil)
print(kocha + ' ko\'chasi,\n' +  mahalla + ' mahallasi,\n' + \
      tuman + ' tumani,\n' + viloyat + ' viloyati')
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())      