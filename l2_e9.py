salario = float(input("salário"))
n = int(input("anos de casa"))
if n > 5:
    bonus = salario*0.2
else:
    bonus = salario*0.1
print("o bonus a ser recebido pelo funcionário é de", bonus)