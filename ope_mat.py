num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

operacao = input("Qual operação deseja realizar(+,-,x, /)")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(abs(num1 - num2))
elif operacao == 'x':
    print(abs(num1 * num2))
elif operacao == '/':
    print(abs(num1 / num2))
else:
    print("Operação invalida")