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
        self.ConsumidoComensal1 = False
        
    def run(self):
        while ( not self.ConsumidoComensal1):
            if len(itemsCons2) == 2:#CONSULTO SI EL COMENSAL NO ESTA COMIENDO
                semaphore.acquire()
                with self.monitor:              
                    while len(items)<1:     
                        self.monitor.wait() 
                    x = items.pop(0)     
                    semaphore.release()
                logging.info(f'Consumí {x}')
                time.sleep(1)
                self.ConsumidoComensal1 = True

class Consumidor2(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor
        self.ConsumidoComensal2 = False

    def run(self):
        while ( not self.ConsumidoComensal2):
            if len(itemsCons2) == 2: #CONSULTO SI NO HA COMENSADO A COMER EL COMENSAL 2
                semaphore.acquire() #SINO COMENSO A COMER TOMO EL SAMAFORO PARA QUE CONSUMA SOLO EL COMENSAL 2
            with self.monitor: #TOMO EL MONITOR PARA CONSUMIR           
                while len(items)<1:#CONSULTO SI HAY PLATOS PARA CONSUMIR 
                    self.monitor.wait() #SINO HAY PLATOS ESPERO HASTA QUE EL PRODUCTOR REALICE LOS PLATOS Y AVISE
                x = items.pop(0)#SI HAY PLATOS PARA CONSUMIR CONSUMO EL PRIMER PLATO
                itemsCons2.pop(0)#DESCUENTO UN PLATO DE LA CANTIDAD QUE DEBE COMER SEGUIDOS EL COMENSAL 2
                if len(itemsCons2) == 0:#CONSULTO SI SE CONSUMIERON LA CANTIDAD DE PLATOS SEGUIDOS
                    itemsCons2.append(1)#SI YA SE CONSUMIERON TODOS LOS PLATOS SEGUIDOS LLENO LA LISTA NUEVAMENTE
                    itemsCons2.append(2)
                    semaphore.release()  #SUELTO EL SEMAFORO PARA QUE EL COMENSAL 1 PUEDA CONSUMIR
                    self.ConsumidoComensal2 = True
            
            logging.info(f'Consumí {x}')
            time.sleep(1)


# la lista de ítems a consumir
items = []

# la lista de platos consumidor 2
itemsCons2 = []
itemsCons2.append(1)
itemsCons2.append(2)



# El monitor
items_monit = threading.Condition()

# monitor para controlar los dos platos del consumidor 2
items_Comensal2 = threading.Condition()

# un thread que consume
cons1 = Consumidor(items_monit)
cons1.start()

cons2 = Consumidor2(items_monit)
cons2.start()

# El productor
productor(items_monit)