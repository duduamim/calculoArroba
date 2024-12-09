import tkinter as tk
from calculos import calculo_valor_arroba  # importa a função de cálculo

# função chamada ao clicar no botão "Calcular"
def calcular():
    try:
        peso_bovino = float(entry_peso.get())
        preco_arroba = float(entry_preco.get())

        peso_arroba, valor_calc = calculo_valor_arroba(peso_bovino, preco_arroba)

        valor_final = f"R$ {valor_calc:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        peso_arroba_format = f"{peso_arroba:.2f}"

        label_resultado.config(
            text=f"Peso em arrobas: {peso_arroba_format} arrobas\nValor total: {valor_final}",
            fg="#333333"
        )
    except ValueError:
        label_resultado.config(text="Erro: Insira valores válidos.", fg="#FF4D4D")

# função para limpar os campos de entrada e o resultado
def limpar():
    entry_peso.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    label_resultado.config(text="", fg="#333333")

# configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Valor da Arroba")
root.geometry("500x500")
root.configure(bg="#F0F4F8")

# estilo claro e focado
font_title = ("Arial", 18, "bold")
font_label = ("Arial", 14)
font_button = ("Arial", 14, "bold")
font_result = ("Arial", 14, "bold")
widget_width = 25

# frame central para agrupar os elementos
frame = tk.Frame(root, bg="#FFFFFF", padx=20, pady=20, relief="solid", bd=1)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame

# título do programa
tk.Label(
    frame,
    text="Calculadora de Arroba",
    font=font_title,
    bg="#FFFFFF",
    fg="#2C3E50"
).grid(row=0, column=0, columnspan=2, pady=(10, 20))

# campo para entrada do peso
tk.Label(frame, text="Peso do bovino (kg):", font=font_label, bg="#FFFFFF", fg="#2C3E50").grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry_peso = tk.Entry(frame, font=font_label, width=widget_width, relief="groove", bg="#F9F9F9", fg="#000000")
entry_peso.grid(row=1, column=1, padx=10, pady=10)

# campo para entrada do preço
tk.Label(frame, text="Preço da arroba (R$):", font=font_label, bg="#FFFFFF", fg="#2C3E50").grid(row=2, column=0, sticky="e", padx=10, pady=10)
entry_preco = tk.Entry(frame, font=font_label, width=widget_width, relief="groove", bg="#F9F9F9", fg="#000000")
entry_preco.grid(row=2, column=1, padx=10, pady=10)

# botão para calcular
btn_calcular = tk.Button(
    frame,
    text="Calcular",
    command=calcular,
    font=font_button,
    bg="#3498DB",
    fg="#FFFFFF",
    activebackground="#2980B9",
    relief="raised",
    bd=2,
    width=18
)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=(20, 10))

# botão para limpar
btn_limpar = tk.Button(
    frame,
    text="Limpar",
    command=limpar,
    font=font_button,
    bg="#E74C3C",
    fg="#FFFFFF",
    activebackground="#C0392B",
    relief="raised",
    bd=2,
    width=18
)
btn_limpar.grid(row=4, column=0, columnspan=2, pady=10)

# rótulo para exibir o resultado
label_resultado = tk.Label(frame, text="", font=font_result, bg="#FFFFFF", fg="#2C3E50", wraplength=400, justify="center")
label_resultado.grid(row=5, column=0, columnspan=2, pady=20)

# atalhos de teclado
root.bind('<Return>', lambda event: calcular())
root.bind('<Control-q>', lambda event: root.quit())

# loop da interface
root.mainloop()
