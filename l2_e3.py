n = int(input("insira seu salário para calcular seu desconto do INSS"))
for n in range(n, n+1):
    if n <= 600:
        print("isento")
    if 600 < n <= 1200:
        x = n*0.2
    if 1200 < n <= 2000:
        x = n * 0.25
    if n > 2000:
       x = n*0.3
print("seu desconto do INSS é de", x)

