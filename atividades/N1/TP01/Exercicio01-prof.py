import random
import threading 
import time

# Função principal do QuickSort 

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô

    # Separando as duas sequências de algoritmos
    left_List = [0]    
    right_List = [0]

    # Uma Thread para cada sequência
    left_Thread = threading.Thread(target = quicksort, args=(left_List))
    right_Thread = threading.Thread(target = quicksort, args=(right_List))

    # Execucação das Threads
    left_Thread.start()
    right_Thread.start()
    left_Thread.join()
    right_Thread.join()

    return left_List[0] + [pivot] + right_List[0]

# Função para gerar números aleatórios

def gerar_numeros_aleatorios(n=10, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função principal para testar o QuickSort

if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios()
    
    print("Primeiros 10 números antes da ordenação: ", numeros)

    start_time = time.time()
    valores = [0]

    quicksort(numeros)
    numeros_ordenados = valores[0]    

    print("Primeiros 10 números após a ordenação: ", numeros_ordenados)
    print("Tempo utilizado na ordenação: ", time.time)