import threading
import time

def Saudacao(nome, tempo):
    print(f"Olá, {nome}!")
    time.sleep(tempo)
    print(f"Tchau, {nome}.")

'''
Atribuindo valores na função de maneira simples
Saudacao("Gabriela", 2)
'''

# Atribuindo valores dentro de uma Thread
TA = threading.Thread(target = Saudacao, args = ("Gabriela", 5))
TB = threading.Thread(target = Saudacao, args = ("Lu", 2))

t0 = time.time()

'''
Lembrar que os comando .start() e .join() são FUNÇÕES, logo, necessitam terminar com ()

Todas as funções serão executadas simultâneamente
TA.start()
TB.start()
TA.join()
TB.join()
'''

# Primeiro a função TA() será executada e só depois da sua conclusão,
# a função TB() será iniciada.

TA.start()
TA.join()
TB.start()
TB.join()


tf = time.time()

deltaT = tf - t0

print(f"\nTempo de processamento: {deltaT}")
print("Fim da execução do código fonte.")