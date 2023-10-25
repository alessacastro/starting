salario = float(input("insira seu salario"))
consumo = float(input("insira seu consumo de energia em quilowatts"))
quilowatt = (salario/500)
conta = (quilowatt*consumo)
desconto = (conta*0.85)

print(" o preço do quilowatt é", quilowatt)
print("o valor a ser pago é", conta)
print("o valor a ser pago com desconto é de", desconto)

