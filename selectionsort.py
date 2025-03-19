def selection_sort_basico(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            print(f"Troca na iteração {i}: {array}")
        else:
            print(f"Sem troca na iteração {i}: {array}")

def selection_sort_otimizado(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        trocou = False
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
                trocou = True
        if trocou:
            array[i], array[min_index] = array[min_index], array[i]
            print(f"Troca na iteração {i}: {array}")
        else:
            print(f"Lista já ordenada! Encerrando na iteração {i}: {array}")
            break
