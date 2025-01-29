import serial
import serial.tools.list_ports
import threading
import time

class BalanzaService:
    def __init__(self):
        self.cPeso = ""
        self.peso_actual = "----"
        self.trama_actual = ""
        self.timer_interval = 0.25
        self.oComm = serial.Serial()
        self.oComm.baudrate = 9600
        self.oComm.parity = serial.PARITY_NONE
        self.oComm.bytesize = serial.EIGHTBITS
        self.oComm.stopbits = serial.STOPBITS_ONE
        self.oComm.timeout = 0
        self.lectura_activa = False
        self._thread = None

    def listar_puertos(self):
        ports = serial.tools.list_ports.comports()
        return [p.device for p in ports]

    def iniciar(self, port_name):
        """
        Abre el puerto y arranca el hilo de lectura periódica.
        """
        if self.lectura_activa:
            return "Ya está iniciado."
        if not port_name:
            return "No se indicó puerto."

        try:
            self.oComm.port = port_name
            self.oComm.open()
            self.lectura_activa = True
            self._thread = threading.Thread(target=self._lectura_loop, daemon=True)
            self._thread.start()
            return f"Puerto {port_name} abierto. Lectura iniciada."
        except Exception as e:
            return f"Error al abrir puerto: {str(e)}"

    def detener(self):
        """
        Detiene la lectura, cierra el puerto, resetea valores.
        """
        self.lectura_activa = False
        if self.oComm.is_open:
            self.oComm.close()
        self.cPeso = ""
        self.peso_actual = "----"
        self.trama_actual = ""
        return "Lectura detenida y puerto cerrado."

    def _lectura_loop(self):
        """
        Hilo que se ejecuta cada 250 ms para leer del puerto.
        """
        while self.lectura_activa:
            try:
                in_waiting = self.oComm.in_waiting
                if in_waiting > 0:
                    data = self.oComm.read(in_waiting)
                    chunk = data.decode('latin-1', errors='ignore')
                    self.cPeso += chunk

                if len(self.cPeso) >= 30:
                    self.trama_actual = self.cPeso
                    pos = self.cPeso.find('\x02')
                    if pos != -1:
                        start_idx = pos + 4
                        weight = self.cPeso[start_idx:start_idx+6]
                        self.peso_actual = weight
                    else:
                        self.peso_actual = "----"

                    self.cPeso = ""

            except Exception as e:
                pass

            time.sleep(self.timer_interval)
