
# Importando blibiotecas do Sistema Operacional
import threading
import time

'''
t0 = time.time()

print(f"{t0}")
'''

# Definindo função Tarefa()
def Tarefa():
    print("Início...")
    time.sleep(3)
    print("Fim...")

# Início do Processamento: criando a thread que irá executar a função Tarefa()
T = threading.Thread(target = Tarefa)

# Iniciando a Thread
T.start()
# Thread deve aguardar a conclusão da Thread para continuar o processamento do código
T.join()

print("Thread principal finalizada")


'''
Apresentando uma situação onde o processamento ocorre de maneira paralela = Processamento Simultâneo

T = threading.Thread(target = Tarefa)

# Iniciando a Thread
T.start()
# T.join() --> linha de código ignorada

print("Thread principal finalizada")

--> Nessa situação, o código processará ao mesmo tempo 
'''