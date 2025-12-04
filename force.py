from tkinter import Canvas, Tk, PhotoImage, Label, Entry, Button
import datetime 
from PIL import Image, ImageTk

def validar_entrada(texto_nuevo):
    if texto_nuevo == "":
        return True
    if texto_nuevo.isdigit() and len(texto_nuevo) <= 4:
        return True
    return False

def actualizar_fecha_hora():
    ahora = datetime.datetime.now()
    label_fecha_valor.config(text=ahora.strftime("%d/%m/%Y  %H:%M:%S"))
    ventana.after(1000, actualizar_fecha_hora)

def desencriptar_contraseña():
    contraseñaReal = entry_pass.get()

    # Validación básica
    if len(contraseñaReal) != 4 or not contraseñaReal.isdigit():
        label_decriped.config(text="Inválida")
        return
    
    # Simulación de fuerza bruta
    for i in range(10000):
        intento = f"{i:04d}"
        label_decriped.config(text=intento)
        ventana.update()  # refresca la UI para mostrar el conteo
        
        if intento == contraseñaReal:
            label_decriped.config(text=f"✔ {intento}")
            return


# ---------------------
#   VENTANA PRINCIPAL
# ---------------------
ventana = Tk()
ventana.geometry("600x400")
ventana.title("Simulación de ataque de fuerza bruta")
ventana.configure(bg="#f4f4f4")

# ---------------------
#   ICONO
# ---------------------
try:
    icon = PhotoImage(file="force.png")
    ventana.iconphoto(True, icon)
except:
    print("No se encontró la imagen de icono.")

# ---------------------
#   LOGO UTH
# ---------------------
try:
    uth = Image.open("uth.png").resize((50, 78))
    uthImage = ImageTk.PhotoImage(uth)
    
    label_uth = Label(ventana, image=uthImage, bg="#f4f4f4")
    label_uth.image = uthImage
    label_uth.place(x=10, y=10)

except Exception as e:
    print("No se encontró la imagen de UTH:", e)

# ---------------------
#   TÍTULO
# ---------------------
label_tittle = Label(
    ventana, 
    text="Simulación de ataque de fuerza bruta", 
    font=("Helvetica", 22, "bold"),
    bg="#f4f4f4"
)
label_tittle.pack(pady=20)

# ---------------------
#   ENTRADA PASSWORD
# ---------------------
label_pass = Label(ventana, text="Escriba su contraseña:", font=("Helvetica", 16), bg="#f4f4f4")
label_pass.place(x=50, y=110)

reg_validacion = ventana.register(validar_entrada)

entry_pass = Entry(
    ventana,
    font=("Helvetica", 16),
    show="•",
    validate="key",
    validatecommand=(reg_validacion, '%P')
)
entry_pass.place(x=300, y=110)

button_pass = Button(ventana, text="Desencriptar", font=("Helvetica", 16), command=desencriptar_contraseña)
button_pass.place(x=250, y=160)

# ---------------------
#   RESULTADO
# ---------------------
label_decript = Label(ventana, text="Contraseña desencriptada:", font=("Helvetica", 16), bg="#f4f4f4")
label_decript.place(x=50, y=230)

label_decriped = Label(ventana, text="0000", font=("Helvetica", 16), bg="#f4f4f4")
label_decriped.place(x=300, y=230)

# ---------------------
#   FECHA Y HORA
# ---------------------
label_fecha = Label(ventana, text="Fecha y hora actual:", font=("Helvetica", 16), bg="#f4f4f4")
label_fecha.place(x=50, y=280)

label_fecha_valor = Label(ventana, text="", font=("Helvetica", 16), bg="#f4f4f4")
label_fecha_valor.place(x=300, y=280)

# ---------------------
#   AUTOR
# ---------------------
label_autor = Label(
    ventana, 
    text="Creado por: Erick Daniel",
    font=("Helvetica", 14),
    bg="#f4f4f4"
)
label_autor.place(x=420, y=360)

# Iniciar actualización automática del tiempo
actualizar_fecha_hora()

ventana.mainloop()
