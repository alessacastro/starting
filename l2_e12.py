salario = float(input("insira seu salário bruto"))
n = float(input("insira o valor da prestação"))
if n > salario*0.3:
    print("empréstimo não concedido")
else:
    print("empréstimo concedido")
