#calculando se um ano qualquer é bissexto .
# da para calcular o ano atual digitando apenas '0' 

from datetime import date

ano = int(input('digite o ano:'))

if ano == 0 :
    
    ano = date.today().year
    print(ano)
    
elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) :

    print(' ESSE ANO É BISSEXTO !')

else:
    print('ESSE ANO NÃO É BISSEXTO !')
