from selectionsort import selection_sort_basico, selection_sort_otimizado

### MELHOR CASO (lista já ordenada)
print("===== MELHOR CASO =====")
lista1 = [0, 1, 2, 3, 4, 5]
print("\n--- Versão Básica ---")
print("Lista original:", lista1)
selection_sort_basico(lista1)
print("Lista ordenada:", lista1)

lista2 = [0, 1, 2, 3, 4, 5]
print("\n--- Versão Otimizada ---")
print("Lista original:", lista2)
selection_sort_otimizado(lista2)
print("Lista ordenada:", lista2)


### PIOR CASO (lista em ordem decrescente)
print("\n\n===== PIOR CASO =====")
lista3 = [9, 7, 5, 3, 1, 0]
print("\n--- Versão Básica ---")
print("Lista original:", lista3)
selection_sort_basico(lista3)
print("Lista ordenada:", lista3)

lista4 = [9, 7, 5, 3, 1, 0]
print("\n--- Versão Otimizada ---")
print("Lista original:", lista4)
selection_sort_otimizado(lista4)
print("Lista ordenada:", lista4)
