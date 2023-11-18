# my code
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


def entrada(mensagem, entry_var):
    def validate_input(entry_var):
        try:
            x = float(entry_var.get())
            return x
        except ValueError:
            resultado_var.set("Entrada inválida, somente valores numéricos")

    return validate_input(entry_var)

def calcular_imc():
    altura = entrada_altura(entry_altura)
    peso = entrada_peso(entry_peso)

    imc_resultado = peso / (altura ** 2)

    for limite, condicao in condicoes_imc.items():
        if imc_resultado < limite:
            resultado_var.set(f"Condição: {condicao}\nIMC: {imc_resultado:.2f}")
            break

def entrada_altura(entry_var):
    return entrada("Digite altura (em metros): ", entry_var)

def entrada_peso(entry_var):
    return entrada("Digite peso (em kg): ", entry_var)


# GPT layout 

# GUI setup
app = tk.Tk()
app.title("Calculadora de IMC")
app.geometry("400x300")

# Ícone da aplicação na barra de tarefas
icon_image = Image.open("icon/icon.png")  # Substitua pelo caminho real do seu ícone
icon_photo = ImageTk.PhotoImage(icon_image)
app.iconphoto(True, icon_photo)

# Labels
label_altura = tk.Label(app, text="Altura (m):", font=("Arial", 12, "bold"))
label_peso = tk.Label(app, text="Peso (kg):", font=("Arial", 12, "bold"))

# Entry widgets
entry_altura_var = tk.StringVar()
entry_altura = tk.Entry(app, textvariable=entry_altura_var, font=("Helvetica", 12))

entry_peso_var = tk.StringVar()
entry_peso = tk.Entry(app, textvariable=entry_peso_var, font=("Helvetica", 12))

# Button
calcular_button = tk.Button(app, text="Calcular IMC", command=calcular_imc, font=("Helvetica", 12))

# Result label
resultado_var = tk.StringVar()
resultado_label = tk.Label(app, textvariable=resultado_var, font=("Helvetica", 14), pady=10)

# Layout
label_altura.grid(row=0, column=0, pady=10, sticky=tk.E)
label_peso.grid(row=1, column=0, pady=10, sticky=tk.E)
entry_altura.grid(row=0, column=1, pady=10, padx=(0, 10))
entry_peso.grid(row=1, column=1, pady=10, padx=(0, 10))
calcular_button.grid(row=2, column=0, columnspan=2, pady=15)
resultado_label.grid(row=3, column=0, columnspan=2)

# Centering the form
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Dictionary with IMC conditions
condicoes_imc = {
    18.5: "MAGREZA",
    25.0: "NORMAL",
    30.0: "SOBREPESO",
    35.0: "OBESIDADE",
    40.0: "OBESIDADE GRAVE"}

app.mainloop()
