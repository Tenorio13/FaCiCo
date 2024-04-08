import tkinter as tk
from tkinter import ttk
import util.generic as utl
import mysql.connector

class App:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesión')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#0a2102')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 1350, 780)
        
        logo = utl.leer_imagen("./imagenes/logo.png", (500, 450))
        
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=430, relief=tk.SOLID, padx=20, pady=20,bg='#0b2d1c')
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#0b2d1c')
        label.place(x=10, y=10, relwidth=1, relheight=1)
        
        # Formulario
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        # Título
        frame_form_top = tk.Frame(frame_form, height=10, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Formulario de Registro", font=('Times', 35), fg="#000000", bg='#fcfcfc', pady=20)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        # Campos del formulario
        frame_form_fill = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        etiqueta_nombre = tk.Label(frame_form_fill, text="Nombre Completo", font=('Times', 20), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20, pady=5)
        self.nombre = ttk.Entry(frame_form_fill, font=('Times', 18))
        self.nombre.pack(fill=tk.X, padx=20, pady=5)
        
        etiqueta_num_cuenta = tk.Label(frame_form_fill, text="Número de Cuenta", font=('Times',20), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_num_cuenta.pack(fill=tk.X, padx=20, pady=5)
        self.num_cuenta = ttk.Entry(frame_form_fill, font=('Times', 18))
        self.num_cuenta.pack(fill=tk.X, padx=20, pady=5)
        self.num_cuenta.config(validate="key", validatecommand=(self.num_cuenta.register(self.validate_num_cuenta), "%P"))
        
        etiqueta_servicio = tk.Label(frame_form_fill, text="Servicio Solicitado", font=('Times', 20), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_servicio.pack(fill=tk.X, padx=20, pady=5)
        opciones_servicio = ["Equipos de Computo", "Impresiones", "Escaneo"]
        self.servicio = ttk.Combobox(frame_form_fill, values=opciones_servicio, font=('Times', 18))
        self.servicio.pack(fill=tk.X, padx=20, pady=5)
        
        etiqueta_equipo = tk.Label(frame_form_fill, text="Número de Equipo", font=('Times', 20), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_equipo.pack(fill=tk.X, padx=20, pady=5)
        self.opciones_equipo = [str(i) for i in range(1, 26)]
        self.equipo_var = tk.StringVar()
        self.equipo = ttk.Combobox(frame_form_fill, textvariable=self.equipo_var, values=self.opciones_equipo, font=('Times', 14))
        self.equipo.pack(fill=tk.X, padx=20, pady=5)
        
        etiqueta_licenciatura = tk.Label(frame_form_fill, text="Licenciatura", font=('Times', 20), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_licenciatura.pack(fill=tk.X, padx=20, pady=5)
        opciones_licenciatura = ["Psicología", "Educación", "Trabajo social", "Cultura Física y Deporte", "Otros"]
        self.licenciatura = ttk.Combobox(frame_form_fill, values=opciones_licenciatura, font=('Times', 18))
        self.licenciatura.pack(fill=tk.X, padx=20, pady=5)
        
        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 20), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        opciones_usuario = ["Alumno", "Maestro", "Administrador", "Externo"]
        self.usuario = ttk.Combobox(frame_form_fill, values=opciones_usuario, font=('Times', 18))
        self.usuario.pack(fill=tk.X, padx=20, pady=5)
        
        # Botón Enviar
        enviar_button = tk.Button(frame_form_fill, text="Enviar", command=self.enviar_formulario, font=('Times', 20), bg='#0b2d1c', fg='white')
        enviar_button.pack(pady=(20, 0), anchor="center")
        
        self.ventana.mainloop()
        
    def validate_num_cuenta(self, value):
        # Permitir cadena vacía (borrar caracteres)
        if value == "":
            return True
        return value.isdigit() and len(value) <= 10
    
    def enviar_formulario(self):
        nombre = self.nombre.get()
        num_cuenta = self.num_cuenta.get()
        servicio = self.servicio.get()
        equipo = self.equipo.get()
        licenciatura = self.licenciatura.get()
        usuario = self.usuario.get()

        # Conexión a la base de datos
        mydb = mysql.connector.connect(
            host="localhost",  # Cambia localhost por la dirección IP del servidor si es necesario
            port="3306",  # Puerto predeterminado para MySQL
            user="root",
            password="123456",
            database="formulario_db"
        )
        cursor = mydb.cursor()

        # Insertar datos en la tabla
        sql = "INSERT INTO usuarios (nombre_completo, num_cuenta, servicio_solicitado, num_equipo, licenciatura, tipo_usuario) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nombre, num_cuenta, servicio, equipo, licenciatura, usuario)
        cursor.execute(sql, val)
        mydb.commit()

        print("Formulario enviado con éxito")

        # Restablecer campos del formulario
        self.nombre.delete(0, tk.END)
        self.num_cuenta.delete(0, tk.END)
        self.servicio.set('')
        self.equipo.set('')
        self.licenciatura.set('')
        self.usuario.set('')

if __name__ == "__main__":
    app = App()
