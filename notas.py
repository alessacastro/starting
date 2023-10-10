def lernotas():
        n = float(input('Insira sua nota aqui:'))
        return n
def calcularmedia(n1,n2):
        media = (n1 + n2)/2
        print("Nota 1: ", n1) 
        print("Nota 2: ", n2)      
        if media >= 7:
                print("Aprovado")
        else:
                print("Reprovado")
                
a = lernotas()
b = lernotas()
calcularmedia(a,b)