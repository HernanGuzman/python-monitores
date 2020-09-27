import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


class Juagador1(threading.Thread):
    def __init__(self, monitor, accion, cantidad):
        super().__init__()
        self.monitor = monitor
        self.accion = accion
        self.cantidad = cantidad
        
    def run(self):
        if self.accion == 'ingresar':
            with self.monitor:
                for i in range(self.cantidad):
                    cantBolitas.append(i)   
                logging.info(f'Jugador 1: Ingresé {self.cantidad} bolitas')   
                self.monitor.notify()
        else:
            with self.monitor:
                if len(cantBolitas) < self.cantidad:
                    logging.info(f'Jugador 1: No hay {self.cantidad} bolitas para sacar. Asi que espero!')
                    self.monitor.wait() 
                for i in range(self.cantidad):
                    cantBolitas.pop(0)
                logging.info(f'Jugador 1: Saqué {self.cantidad} bolitas')    

class Juagador2(threading.Thread):
    def __init__(self, monitor, accion, cantidad):
        super().__init__()
        self.monitor = monitor
        self.accion = accion
        self.cantidad = cantidad
        
    def run(self):
        if self.accion == 'ingresar':
            with self.monitor:
                for i in range(self.cantidad):
                    cantBolitas.append(i)
                logging.info(f'Jugador 2: Ingresé {self.cantidad} bolitas')    
                self.monitor.notify()
        else:
            with self.monitor:
                if len(cantBolitas) < self.cantidad:
                    logging.info(f'Jugador 2: No hay {self.cantidad} bolitas para sacar. Asi que espero!')
                    self.monitor.wait() 
                for i in range(self.cantidad):
                    cantBolitas.pop(0)
                logging.info(f'Jugador 2: Saqué {self.cantidad} bolitas')  

class Juagador3(threading.Thread):
    def __init__(self, monitor, accion, cantidad):
        super().__init__()
        self.monitor = monitor
        self.accion = accion
        self.cantidad = cantidad
        
    def run(self):
        if self.accion == 'ingresar':
            with self.monitor:
                for i in range(self.cantidad):
                    cantBolitas.append(i)  
                logging.info(f'Jugador 3: Ingresé {self.cantidad} bolitas')  
                self.monitor.notify()
        else:
            with self.monitor:
                if len(cantBolitas) < self.cantidad:
                    logging.info(f'Jugador 3: No hay {self.cantidad} bolitas para sacar. Asi que espero!')
                    self.monitor.wait() 
                for i in range(self.cantidad):
                    cantBolitas.pop(0)
                logging.info(f'Jugador 3: Saqué {self.cantidad} bolitas')  
        




# la lista de ítems a consumir
cantBolitas = []



# El monitor
items_monit = threading.Condition()



# Ingreso 5 bolitas por el jugador 1
jug1 = Juagador1(items_monit, 'ingresar', 5)
jug1.start()

# sacar 3 bolitas por el jugador 2
jug2 = Juagador2(items_monit, 'sacar', 2)
jug2.start()

# Ingreso 10 bolitas por el jugador 3
jug3 = Juagador3(items_monit, 'ingresar', 10)
jug3.start()

# sacar 8 bolitas por el jugador 1
jug1 = Juagador1(items_monit, 'sacar', 8)
jug1.start()

# sacar 10 bolitas por el jugador 2
jug2 = Juagador2(items_monit, 'sacar', 10)
jug2.start()

# sacar 10 bolitas por el jugador 2
jug1 = Juagador1(items_monit, 'ingresar', 20)
jug1.start()




