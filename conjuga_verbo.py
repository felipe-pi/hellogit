pessoas = ['Eu', 'Tu', 'Ele', 'Nos', 'Vos', 'Eles']
verboar = ['o', 'as', 'a', 'amos', 'amais', 'amam']
verboer = ['o', 'es', 'e', 'emos', 'eis', 'em']
verboir = ['o', 'es', 'e', 'imos', 'is', 'em']

i = 0

verbo_com_radical = input()
if verbo_com_radical[-2:] == 'ar':
    for pess in pessoas:
            print(pess, verbo_com_radical[:-2],verboar[i])
    i += 1
        
