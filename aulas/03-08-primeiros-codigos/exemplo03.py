
# Importando blibiotecas do Sistema Operacional
import threading
import time

# Definindo função Tarefa()
def Tarefa():
    print("Início...")
    time.sleep(5)
    print("Fim...")

t0 = time.time()

TA = threading.Thread(target = Tarefa)
TB = threading.Thread(target = Tarefa)

# Todas as funções serão executadas simultâneamente
t0 = time.time()
TA.start()
TB.start()
TA.join()
TB.join()

'''
Primeiro a função TA() será executada e só depois da sua conclusão,
a função TB() será iniciada.

t0 = time.time()
TA.start()
TA.join()
TB.start()
TB.join()
'''

tf = time.time()

deltaT = tf - t0

# Tempo total gasto no processamento do Código Fonte, incluindo todas as suas funções, sejam elas paralelas ou não
print(f"\nTempo de processamento: {deltaT}")
# Código fonte só será encerrado quando todas as funções forem finalizadas 
print("Thread principal finalizada")