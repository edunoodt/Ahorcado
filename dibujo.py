#nombre=input('Ingrese su Nombre =>  ')
#chancesStr=(input('ingrese las chances '))
def horca(chances,nombre):
    for i in range(20):
        print()
    print('             IIIIIIIIIIIIIIIIIIIIIIII')
    print('             IIIIIIIIIIIIIIIIIIIIIIII')
    print('             III                  III')
    print('             III                   :')
    print('             III                   :')
    if chances<1:
        print('             III')
        print('             III')
        print('             III')
    else:
        print('             III                  _:_')
        print('             III                 /- -\ ')
        print('             III                 \_-_/     <==== ',nombre)
    if chances<2:
        print('             III')
    else:
        print('             III                   |')
        if chances<3:
            print('             III                   |')
        elif chances<4:
            print('             III                   |\___')
        else:
            print('             III               ___/|\___')
    if chances<2:
        print('             III')
    else:
        print('             III                   |')
    if chances<5:
        print('             III')
    elif chances<6:
        print('             III                    \ ')
    else:
        print('             III                  / \ ')
    if chances<5:
        print('             III')
    elif chances<6:
        print('             III                     \ ')
    else:
        print('             III                 /   \ ')
    if chances<5:
        print('             III')
    elif chances<6:
        print('             III                      |')
    else:
        print('             III                |     |')
    if chances<5:
        print('             III')
    elif chances<6:
        print('             III                      |')
    else:
        print('             III                |     |        <==== AHORCADO!!!!!!')
    if chances<5:
        print('             III')
    elif chances<6:
        print('             III                      |__')
    else:
        print('             III              __|     |__')

    print('             III')
    print('             III')
    print('             III')
    print('      '+'----------------')
    print('     '+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124))
    print(' -----                 -----')
    print(chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124)+chr(124))
    print(' ---------------------------')
#        chancesStr = (input('ingrese las chances '))
