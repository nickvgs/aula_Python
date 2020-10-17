a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input("Segundo bimestre: "))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input("terceiro bimestre: "))
if c > 10:
    c = int(input('Você digitou errado. Terceiro Semestre: '))
d = int(input("quarto bimestre: "))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4

print('media: {}'.format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#   print ('media: {}'.format (media))
#
# else:
#     print("alguma nota foi digitada incorretamente")

# a = int(input("Entre com o valor1: "))
# b = int(input("Entre com o valor2: "))
# resto_a = a%2
# resto_b = b%2
#
#
#
# if resto_a == 0 or not resto_b > 0:
#     print("foi digitado um número par")
# else:
#     print("nenhum número par digitado")
# print ("Fim do programa")
#
# a = int(input("Escreva o primeiro número : "))
# b = int(input("Escreva o segundo número: "))
# c = int(input("Escreva o terceiro número: "))
#
# if a > b and a > c:
#     print ("O maior número é {}" .format (a))
# elif b > a and b > c:
#     print("O maior número é {}".format (b))
# else:
#     print("o maior número é {}".format (c))
# print("final do programa")
