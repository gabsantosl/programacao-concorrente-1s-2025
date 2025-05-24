import threading

B = threading.Barrier(3)

def Trabalho(ID):
    print(f"\nThread {ID} iniciando.")
    threading.Event().wait(1)
    print(f"\nThread {ID} chegou na barreira.")
    B.wait
    print(f"\nThread {ID} passou pela barreira.")

threads = [threading.Thread(target = Trabalho, args = (i, )) for i in range(4)]
for t in threads : t.start()
for t in threads : t.join()
