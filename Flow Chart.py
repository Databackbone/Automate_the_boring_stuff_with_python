print('Hello Flow Chart')
#Boolean types commit



def questions(erraten):
    my_age = int(input('wie alt bin ich? 30  '))
    my_cat = input('tipe in Bernd  ')

    if my_age > 18 and my_cat == 'Bernd':
        print('Ganz genau meine Katze heiß Bernd')
        erraten = True
    else:
        print('Das ist leider nicht richtig versuche es nochmal')
    return erraten
erraten = False
while not erraten:
     erraten = questions(erraten)

