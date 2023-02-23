# criando duas variáveis

altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

# calculo do IMC
IMC = peso / (altura/100)**2 # elevado ao quadrado

print(IMC)

# criando parâmetros conforme cada comentário abaixo

if IMC > 17 and IMC < 18.4:
    print(f' Seu IMC é de {IMC}, e é classificado como Magreza leve ')

elif IMC > 16 and IMC < 16.9:
    print(f' Seu IMC é de {IMC}, e é classificado como Magreza moderada ')

elif IMC < 16:
    print(f' Seu IMC é de {IMC}, e é classificado como Magreza grave ')

elif IMC > 25 and IMC < 29.9:
    print(f' Seu IMC é de {IMC}, e é classificado como Sobrepeso ')

elif IMC > 30 and IMC < 34.9:
    print(f' Seu IMC é de {IMC}, e é classificado como Obesidade grau 1 ')

elif IMC > 35 and IMC < 39.9:
    print(f' Seu IMC é de {IMC}, e é classificado como Obesidade severa ')

elif IMC > 40:
    print(f' Seu IMC é de {IMC}, e é classificado como Obesidade mórbida ')

else:
    print("Gentileza começar a realizar atividades físicas, associado à uma alimentação balanceada! Obesidade mórbida")



 # magreza leve (entre 17 e 18,4);
 # magreza moderada (entre 16 e 16,9) ;
 # magreza grave (menor que 16);
 # sobrepeso (índice de 25 a 29,9);
 # obesidade grau 1 (30 a 34,9);
 # obesidade severa (35 a 39,9);
 # obesidade mórbida (acima de 40).