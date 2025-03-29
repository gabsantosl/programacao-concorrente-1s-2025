import threading
import time

# Recurso Compartilhado (Varíavel Universal)
Contador = 0 

L = threading.Lock()

def Incrementar():
    global Contador
    for _ in range(1000):
        L.acquire()
        try:
            time.sleep(0.000001)
            x = x + 1
            Contador = x
        finally:
            L.release()

TA = threading.Thread(target = Incrementar)        
TB = threading.Thread(target = Incrementar)        
TC = threading.Thread(target = Incrementar)    

t0 = time.time()

TA.start()
TB.start()
TC.start()

TA.join()
TB.join()
TC.join()

print(f"\nContador: {Contador}")

tf = time.time()

deltaT = tf - t0

print(f"\nTempo de processamento: {deltaT}")
print("Fim do processamento do Código Fonte.\n")