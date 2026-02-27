"""
lista = [10, 20, 30, 40]
lista.append("Erick")
nome = lista.pop()
lista.append(50)
del lista[-1]
lista.insert(0, True)

print(lista[2])
"""

"""
lista_A = [1, 2, 3, 4, 5]
lista_B = [6, 7, 8, 9, 10]

lista_C = lista_A + lista_B
lista_D = lista_A.extend(lista_B) #extend - Não retorna NADA, mexe diretamente na lists_A
print(lista_C)
print(lista_D) 
"""
"""
listaA = ["Luiz", "Maria", "Erick"]
listaB = listaA.copy()

listaA[0] = "Nada"
print(listaB)

listaA = ["Luiz", "Maria", "Erick"]
"""
"""
listaA = ["Luiz", "Maria", "Erick"]

for nome in listaA:
    print(nome)
"""
"""
lista = ["Luiz", "Maria", "Erick"]
lista.append("João")
lista.append("Joa")
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
"""
"""
#Desempacotamento + tuples (tuplas)
nomes = ["Luiz", "Maria", "Erick"]

nome = tuple(nomes)
print(nome)
Posso transformar listas em tuplas e tuplas em listas. tuple() / list()
"""
lista = ["Luiz", "Maria", "Erick"]
lista.append("João")

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])



