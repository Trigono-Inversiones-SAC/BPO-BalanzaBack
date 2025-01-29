import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports

class BalanzaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Balanza Gigante (Python)")

        # Variable para acumular la trama recibida
        self.cPeso = ""

        # ---------------------------
        # 1. INTERFAZ DE USUARIO
        # ---------------------------
        lbl_puerto = tk.Label(self, text="Puerto:")
        lbl_puerto.pack()

        self.cbxPuerto = ttk.Combobox(self, values=self.get_serial_ports())
        self.cbxPuerto.pack()

        self.btn_iniciar = tk.Button(self, text="Iniciar", command=self.toggle_connection)
        self.btn_iniciar.pack()

        lbl_peso = tk.Label(self, text="Peso:")
        lbl_peso.pack()

        self.txtPeso = tk.Entry(self)
        self.txtPeso.pack()

        lbl_trama = tk.Label(self, text="Trama:")
        lbl_trama.pack()

        self.txtTrama = tk.Entry(self, width=50)
        self.txtTrama.pack()

        # ---------------------------
        # 2. CONFIGURACIÓN SERIAL
        # ---------------------------
        self.oComm = serial.Serial()
        self.oComm.baudrate = 9600
        self.oComm.parity = serial.PARITY_NONE
        self.oComm.bytesize = serial.EIGHTBITS
        self.oComm.stopbits = serial.STOPBITS_ONE
        self.oComm.timeout = 0  # Lectura no bloqueante (se puede usar 0 o un pequeño timeout)

        # Emulación del Timer (cada 250 ms)
        self.timer_interval = 250
        self.timer_active = False

    def get_serial_ports(self):
        """
        Devuelve una lista de puertos seriales disponibles en el sistema.
        """
        ports = serial.tools.list_ports.comports()
        return [p.device for p in ports]

    def toggle_connection(self):
        """
        Maneja la lógica del botón Iniciar/Detener.
        Abre o cierra el puerto serial y activa o desactiva el 'timer'.
        """
        accion = self.btn_iniciar['text'].strip().upper()
        if accion == "INICIAR":
            try:
                selected_port = self.cbxPuerto.get()
                if not selected_port:
                    messagebox.showinfo("Info", "Seleccione un puerto.")
                    return

                # Configuramos y abrimos el puerto
                self.oComm.port = selected_port
                print(f"[DEBUG] Abriendo puerto: {selected_port}")
                self.oComm.open()

                # Arrancamos la "lectura" periódica
                self.timer_active = True
                self.after(self.timer_interval, self.oTimer_Tick)

                self.btn_iniciar['text'] = "Detener"
                print("[DEBUG] Puerto abierto y Timer iniciado.")

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el puerto: {e}")
                print(f"[ERROR] {e}")

        else:  # "DETENER"
            try:
                print("[DEBUG] Deteniendo lectura y cerrando puerto.")
                self.timer_active = False
                if self.oComm.is_open:
                    self.oComm.close()
                    print("[DEBUG] Puerto cerrado correctamente.")

                self.btn_iniciar['text'] = "Iniciar"
                # Restablecemos el campo peso
                self.txtPeso.delete(0, tk.END)
                self.txtPeso.insert(0, "0")
                # Borramos cPeso en caso de querer reiniciar limpio
                self.cPeso = ""

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cerrar el puerto: {e}")
                print(f"[ERROR] {e}")

    def oTimer_Tick(self):
        """
        Función llamada periódicamente (cada 250 ms).
        Acumula los bytes leídos en 'cPeso'. 
        Cuando cPeso >= 30 caracteres, parsea para extraer 6 dígitos tras el carácter ASCII 2.
        """
        if self.timer_active and self.oComm.is_open:
            try:
                # Cantidad de bytes en el buffer de entrada
                in_waiting = self.oComm.in_waiting
                if in_waiting > 0:
                    # Lee todo lo que haya en el buffer (similar a ReadExisting)
                    data = self.oComm.read(in_waiting)
                    # Decodifica (modo 'latin-1' o 'cp1252', depende de tu balanza)
                    chunk = data.decode('latin-1', errors='ignore')
                    self.cPeso += chunk

                    print(f"[DEBUG] Datos recibidos: {chunk}")

                # Si ya superamos los 30 caracteres, interpretamos la trama
                if len(self.cPeso) >= 30:
                    print(f"[DEBUG] Trama completa (>=30 chars): {self.cPeso}")
                    # Mostramos la trama en el Entry de Trama
                    self.txtTrama.delete(0, tk.END)
                    self.txtTrama.insert(0, self.cPeso)

                    # Buscamos el carácter ASCII 2 (\x02)
                    pos = self.cPeso.find('\x02')
                    if pos != -1:
                        # En VB: nPos = InStr(...) + 4
                        # InStr es 1-based; Python .find() es 0-based => equivalencia pos+4
                        start_idx = pos + 4
                        # Extraemos 6 caracteres
                        weight = self.cPeso[start_idx:start_idx+6]

                        print(f"[DEBUG] Peso extraído: {weight}")

                        # Mostramos el peso
                        self.txtPeso.delete(0, tk.END)
                        self.txtPeso.insert(0, weight)
                    else:
                        print("[DEBUG] No se encontró el carácter ASCII 2 en la trama.")
                        self.txtPeso.delete(0, tk.END)
                        self.txtPeso.insert(0, "----")

                    # Limpiamos cPeso
                    self.cPeso = ""

                else:
                    # Si no hay datos, mostramos '----'
                    if len(self.cPeso) == 0:
                        self.txtPeso.delete(0, tk.END)
                        self.txtPeso.insert(0, "----")

            except Exception as e:
                messagebox.showerror("Error", f"Error de lectura: {e}")
                print(f"[ERROR] {e}")

        # Vuelve a programar la siguiente llamada al timer
        if self.timer_active:
            self.after(self.timer_interval, self.oTimer_Tick)


if __name__ == "__main__":
    app = BalanzaApp()
    app.mainloop()