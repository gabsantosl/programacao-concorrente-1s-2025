import threading 
import random

# Função principal do QuickSort 
'''
def: criação de uma função
arr: array -> estrutura de dados que armazena uma coleção de elementos do mesmo tipo
pivot: valor a ser armazenado para uso em uma função. Nesse caso,
o primeiro pivot é o ultimo numero a ser gerado ([-1] -> inverte)
a ordenação dos algoritmos acontece a partir do valor do pivot.
ex: ultimo numero gerado foi 29, pivot = 29, 40 > 29 logo vai para a direita
21 < 29 logo vai para a esquerda.
A palavra *args (abreviação de arguments ) é utilizada quando precisamos passar vários 
valores para função sem saber ao certo quantos serão
'''

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô
    return quicksort(left) + [pivot] + quicksort(right)

# Função para gerar números aleatórios

def gerar_numeros_aleatorios(n=10, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função principal para testar o QuickSort

if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios()
    
    print("Primeiros 10 números antes da ordenação:", numeros)
    numeros_ordenados = quicksort(numeros)    
    print("Primeiros 10 números após a ordenação:", numeros_ordenados)