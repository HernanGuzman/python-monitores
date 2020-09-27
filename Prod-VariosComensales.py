import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
semaphore = threading.Semaphore(1)

def productor(monitor):
    print("Voy a producir")
    for i in range(30):
        with monitor:          # hace el acquire y al final un release
            items.append(i)    # agrega un ítem
            monitor.notify()   # Notifica que ya se puede hacer acquire
        time.sleep(2) # simula un tiempo de producción


class Consumidor(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor

    def run(self):
        while (True):
            
            with self.monitor:          # Hace el acquire y al final un release    
                while len(items)<1:     # si no hay ítems para consumir
                    self.monitor.wait()  # espera la señal, es decir el notify
                semaphore.acquire()
                x = items.pop(0)     # saca (consume) el primer ítem
                semaphore.release()
            logging.info(f'Consumí {x}')
            time.sleep(1)

class Consumidor2(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor

    def run(self):
        while (True):
            
            with self.monitor:          # Hace el acquire y al final un release    
                while len(items)<1:
                    self.monitor.wait()
                semaphore.acquire()     # si no hay ítems para consumir
                x = items.pop(0)    
                semaphore.release()  # espera la señal, es decir el notify
                     # saca (consume) el primer ítem
            
            logging.info(f'Consumí {x}')
            time.sleep(1)


# la lista de ítems a consumir
items = []

# El monitor
items_monit = threading.Condition()

# un thread que consume
cons1 = Consumidor(items_monit)
cons1.start()

cons2 = Consumidor2(items_monit)
cons2.start()

# El productor
productor(items_monit)